#!/usr/bin/env python3
"""Count Safes with an enabled module, and Safes with a Roles-type module, on Ethereum mainnet (chainId 1).

Standard library only, read-only (eth_call, eth_getCode, eth_blockNumber), no key.
A read that fails is UNREAD, never zero: unread Safes and unread module kinds are reported next to the counts.
"Roles-type" = the module code (or the implementation behind an EIP-1167 clone) contains the selector of
execTransactionWithRole / execTransactionWithRoleReturnData. It says nothing about the project name.

  python3 scripts/count_modules.py --safes facts/tracked-safes.tsv --out count.json                 # live read, pinned to the head it reads first
  python3 scripts/count_modules.py --safes facts/tracked-safes.tsv --block 12345678 --out count.json # pinned to a block you name (archive nodes only)
  python3 scripts/count_modules.py --selftest                                                      # offline checks, no network

--safes: a JSON list of addresses, or {"rows": [{"address": ..., "kind": "safe"}, ...]} (only kind "safe" is read),
or a text file with one address per line, or a tab-separated file whose first column is the address (a header line is skipped).
--block: read every Safe at that block instead of the head. A node that refuses archive reads gives an unread, never a zero.
"""
import argparse
import datetime
import http.client
import json
import sys
import time
import urllib.request

CHAIN, CHAIN_ID = "ethereum", 1
NODES = ["https://ethereum-rpc.publicnode.com", "https://eth.drpc.org", "https://eth-mainnet.public.blastapi.io", "https://rpc.mevblocker.io"]
SENT = "0x0000000000000000000000000000000000000001"
ZERO = "0x" + "00" * 20
GET_MODULES = "cc2f8452"  # getModulesPaginated(address,uint256)
# execTransactionWithRole(address,uint256,bytes,uint8,uint16|bytes32,bool) and ...ReturnData(...): keccak-256, first 4 bytes
ROLES_SELS = ["6928e74b", "c6fe8747", "b0c19912", "2b99e506"]
CLONE_PREFIX = "0x363d3d373d3d3d363d73"  # EIP-1167 minimal proxy, 20-byte implementation follows
PAGE = 10
MAX_PAGES = 5


def rpc(url, method, params):
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": params}).encode()
    req = urllib.request.Request(url, body, {"content-type": "application/json", "user-agent": "module-count/1"})
    try:
        raw = urllib.request.urlopen(req, timeout=30).read()
    except http.client.IncompleteRead as e:  # some nodes cut the body: keep what arrived, JSON parsing decides
        raw = e.partial
    d = json.loads(raw)
    if not isinstance(d, dict) or "result" not in d or d.get("error"):
        raise RuntimeError(str(d)[:80])
    return d["result"]


class Reader:
    def __init__(self, nodes, call=rpc, tries=2, pause=1.0, gap=0.0):
        self.nodes, self.call, self.tries, self.pause, self.gap = nodes, call, tries, pause, gap
        self.turn = 0

    def __call__(self, method, params):
        last = None
        self.turn += 1  # start each call on the next node: spreads the load, so no single public node answers 429
        k = self.turn % len(self.nodes)
        for url in self.nodes[k:] + self.nodes[:k]:
            for _ in range(self.tries):
                try:
                    time.sleep(self.gap)  # public nodes answer 429 above a few requests per second
                    return self.call(url, method, params)
                except Exception as e:  # noqa: BLE001 - retry, then the caller marks the item unread
                    last = repr(e)
                    time.sleep(self.pause)
        raise RuntimeError(last)


def modules_of(read, safe, tag="latest"):
    out, start = [], SENT
    for _ in range(MAX_PAGES):
        data = "0x" + GET_MODULES + start[2:].rjust(64, "0") + PAGE.to_bytes(32, "big").hex()
        v = read("eth_call", [{"to": safe, "data": data}, tag])
        w = [v[2:][i:i + 64] for i in range(0, len(v) - 2, 64)]
        # ABI (address[] array, address next): head = [0x40, next], tail = [len, items...]. Anything else is unread, never "no module".
        if len(w) < 3 or int(w[0], 16) != 0x40:
            raise RuntimeError("unexpected answer")
        n = int(w[2], 16)
        if len(w) != 3 + n or n > PAGE:
            raise RuntimeError("unexpected answer length")
        out += ["0x" + x[-40:] for x in w[3:]]
        if n < PAGE or ("0x" + w[1][-40:]).lower() in (SENT, ZERO):
            return out
        start = out[-1]  # continue after the last module returned (the node's own `next` is not trusted)
    raise RuntimeError("more than %d modules" % (PAGE * MAX_PAGES))


def is_roles(read, module, tag="latest"):
    """True/False from the code; an empty answer ("0x") is an unread, not a "no". Floor: only EIP-1167 clones are followed
    (not ERC-1967 proxies, PUSH0 clones or clones with arguments), so a Roles module behind those would count as "no"."""
    code = read("eth_getCode", [module, tag])
    if len(code) <= 2:
        raise RuntimeError("empty code")
    if len(code) == 92 and code.startswith(CLONE_PREFIX):
        code = read("eth_getCode", ["0x" + code[22:62], tag])
        if len(code) <= 2:
            raise RuntimeError("empty implementation code")
    return any(s in code for s in ROLES_SELS)


def count(read, safes, rounds=4, round_pause=20, block=None):
    head = block if block is not None else int(read("eth_blockNumber", []), 16)
    tag = hex(head)  # every read is pinned to this block, so the figure is dated to a block
    safes = list(dict.fromkeys(a.lower() for a in safes))
    withmod, errs, todo = {}, {}, list(safes)
    for rnd in range(rounds):  # public nodes answer 429 under load: failed reads are retried after a pause, then stay unread
        if rnd:
            time.sleep(round_pause)
        failed = []
        for a in todo:
            try:
                m = modules_of(read, a, tag)
            except Exception as e:  # noqa: BLE001
                errs[a] = str(e)[:80]
                failed.append(a)
                continue
            errs.pop(a, None)
            if m:
                withmod[a] = m
        todo = failed
    unread = [[a, errs[a]] for a in todo]
    kinds = {m: None for m in sorted({x.lower() for ms in withmod.values() for x in ms})}
    kerrs = {}
    for rnd in range(rounds):
        if rnd:
            time.sleep(round_pause)
        for m in [m for m, v in kinds.items() if v is None]:
            try:
                kinds[m] = is_roles(read, m, tag)
                kerrs.pop(m, None)
            except Exception as e:  # noqa: BLE001
                kerrs[m] = str(e)[:80]
    roles = [a for a, ms in withmod.items() if any(kinds[x.lower()] for x in ms)]
    unk = [a for a, ms in withmod.items() if any(kinds[x.lower()] is None for x in ms)]
    agg = {
        "chain": CHAIN, "chainId": CHAIN_ID, "head_block": head,
        "read_at_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "pinned_block": head, "safes_in_set": len(safes), "safes_read": len(safes) - len(unread), "safes_unread": len(unread),
        "with_module": len(withmod), "with_roles_type_module": len(roles), "module_kind_unread_safes": len(unk),
        "distinct_modules": len(kinds), "distinct_roles_type": sum(1 for v in kinds.values() if v),
        "roles_selectors": ROLES_SELS,
    }
    detail = {"unread": unread, "with_module": withmod, "roles_type_safes": roles, "module_kind": kinds, "module_kind_errors": kerrs}
    return agg, detail


def load_safes(path):
    txt = open(path).read()
    try:
        d = json.loads(txt)
    except ValueError:
        return [x.split("\t")[0].strip() for x in txt.splitlines() if x.strip().startswith("0x")]
    rows = d["rows"] if isinstance(d, dict) else d
    return [r["address"] for r in rows if r.get("kind") == "safe"] if rows and isinstance(rows[0], dict) else list(rows)


# ---------- offline self-test (fake node, no network) ----------
def _word(x):
    return x.rjust(64, "0")


def _page(mods, nxt):
    return "0x" + _word("40") + _word(nxt[2:]) + _word(format(len(mods), "x")) + "".join(_word(m[2:]) for m in mods)


def selftest():
    assert ROLES_SELS == ["6928e74b", "c6fe8747", "b0c19912", "2b99e506"], ROLES_SELS  # keccak-256 first 4 bytes, checked once by hand
    A, B, C, D = ("0x" + c * 40 for c in "abcd")
    MOD_ROLES, MOD_PLAIN, MOD_CLONE, MOD_BAD, MOD_CLONE_BADIMPL, MOD_LONG, MOD_EMPTY = ("0x" + c * 40 for c in "1234567")
    IMPL, IMPL_BAD = "0x" + "9" * 40, "0x" + "8" * 40
    state = {A: [MOD_ROLES], B: [MOD_PLAIN], C: [], D: "FAIL"}  # D: its node read fails, so unread and not "no module"
    clone = lambda impl: CLONE_PREFIX + impl[2:] + "5af43d82803e903d91602b57fd5bf3"
    codes = {MOD_ROLES: "0x6080" + ROLES_SELS[0] + "00", MOD_PLAIN: "0x6080aabbccdd", MOD_CLONE: clone(IMPL),
             IMPL: "0x60" + ROLES_SELS[1] + "00", MOD_BAD: "FAIL", MOD_CLONE_BADIMPL: clone(IMPL_BAD), IMPL_BAD: "FAIL",
             MOD_LONG: clone(IMPL) + "00", MOD_EMPTY: "0x"}
    calls = []

    def fake(url, method, params):
        calls.append(url)
        if method == "eth_blockNumber":
            return "0x64"
        assert params[-1] == "0x64" or method == "eth_blockNumber", params  # reads are pinned to the head read first
        if method == "eth_getCode":
            c = codes[params[0]]
            if c == "FAIL":
                raise RuntimeError("node down")
            return c
        a = params[0]["to"]
        if state[a] == "FAIL":
            raise RuntimeError("node down")
        ms = state[a]
        return _page(ms, SENT if len(ms) < PAGE else ms[-1])

    read = Reader(["x"], fake, tries=1, pause=0)
    fast = dict(rounds=2, round_pause=0)
    agg, det = count(read, [A, B, C, D], **fast)
    assert agg["safes_in_set"] == 4 and agg["safes_read"] == 3 and agg["safes_unread"] == 1, agg
    assert agg["with_module"] == 2 and agg["with_roles_type_module"] == 1, agg  # unread D is not counted as "no module"
    assert agg["pinned_block"] == 100, agg
    # the same address in two spellings is one Safe
    assert count(read, [A, A.upper().replace("0X", "0x")], **fast)[0]["safes_in_set"] == 1
    # every selector is detected, in the module code itself
    for sel in ROLES_SELS:
        codes[MOD_ROLES] = "0x6080" + sel + "00"
        assert count(read, [A], **fast)[0]["with_roles_type_module"] == 1, sel
    codes[MOD_ROLES] = "0x6080" + ROLES_SELS[0] + "00"
    # clone: the implementation's code decides; an unreadable implementation is unknown, not plain
    state[A] = [MOD_CLONE]
    assert count(read, [A], **fast)[0]["with_roles_type_module"] == 1
    state[A] = [MOD_CLONE_BADIMPL]
    agg, det = count(read, [A], **fast)
    assert agg["module_kind_unread_safes"] == 1 and agg["with_roles_type_module"] == 0 and det["module_kind"][MOD_CLONE_BADIMPL] is None, agg
    # a code of another length is not treated as a clone; an empty code is unknown
    state[A] = [MOD_LONG]
    agg, det = count(read, [A], **fast)
    assert agg["with_roles_type_module"] == 0 and det["module_kind"][MOD_LONG] is False, agg
    state[A] = [MOD_EMPTY]
    assert count(read, [A], **fast)[0]["module_kind_unread_safes"] == 1
    codes[IMPL_BAD] = "0x"  # clone whose implementation answers an empty code: unknown too
    state[A] = [MOD_CLONE_BADIMPL]
    assert count(read, [A], **fast)[0]["module_kind_unread_safes"] == 1
    codes[IMPL_BAD] = "FAIL"
    state[B] = [MOD_BAD]
    agg, det = count(read, [B], **fast)
    assert agg["module_kind_unread_safes"] == 1 and det["module_kind"][MOD_BAD] is None, agg
    # a transient failure (429) is retried in a later round and then counted
    state[A], state[B], seen = [MOD_ROLES], [MOD_PLAIN], set()

    def flaky(url, method, params):
        key = (method, str(params))
        if key not in seen and method != "eth_blockNumber":
            seen.add(key)
            raise RuntimeError("429")
        return fake(url, method, params)

    agg, det = count(Reader(["x"], flaky, tries=1, pause=0), [A, B], **fast)
    assert agg["safes_unread"] == 0 and agg["with_module"] == 2 and agg["with_roles_type_module"] == 1 and agg["module_kind_unread_safes"] == 0, agg
    # malformed answers are unread, never "no module"
    for bad in ("0x" + _word("40") + _word("1"), "0x" + _word("40") + _word("1") + _word("3") + _word("5"),  # too short / n=3 with 1 item
                "0x" + _word("20") + _word("1") + _word("0"), "0x" + _word("40") + _word("1") + _word("0") + _word("5")):  # bad offset / extra word
        try:
            modules_of(Reader(["x"], lambda u, m, p, bad=bad: bad, tries=1, pause=0), A)
        except RuntimeError:
            continue
        raise AssertionError("accepted malformed answer %r" % bad)
    # pagination: a full page continues after its last module, and the node's `next` is not followed
    many = ["0x%040x" % (0x100 + i) for i in range(PAGE + 3)]
    pages = {SENT: many[:PAGE], many[PAGE - 1]: many[PAGE:]}

    def paged(url, method, params):
        start = "0x" + params[0]["data"][10:74][-40:]
        ms = pages[start]
        return _page(ms, "0x" + "77" * 20 if len(ms) == PAGE else SENT)

    assert modules_of(Reader(["x"], paged, tries=1, pause=0), A) == many
    # a full page whose `next` is the end marker stops (zero address)
    assert modules_of(Reader(["x"], lambda u, m, p: _page(many[:PAGE], ZERO), tries=1, pause=0), A) == many[:PAGE]
    # a named block is used as given: no head is read, and every read is pinned to it
    calls.clear()
    state[A] = [MOD_ROLES]
    agg, det = count(read, [A], block=100, **fast)
    assert agg["pinned_block"] == 100 and agg["with_module"] == 1, agg
    # the list file may be tab-separated with a header
    import os, tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".tsv", delete=False) as f:
        f.write("address\tnetwork\n" + A + "\tEthereum mainnet\n" + B + "\tEthereum mainnet\n")
    assert load_safes(f.name) == [A, B], load_safes(f.name)
    os.unlink(f.name)
    # nodes take turns: with 2 nodes each one serves about half of the calls
    calls.clear()
    rr = Reader(["n1", "n2"], fake, tries=1, pause=0)
    for _ in range(10):
        rr("eth_blockNumber", [])
    assert calls.count("n1") == calls.count("n2") == 5, calls
    print("selftest: ok")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--safes")
    p.add_argument("--out")
    p.add_argument("--detail", help="optional file for the per-address detail (keep it private)")
    p.add_argument("--block", type=int, help="pin every read to this block (needs archive nodes; the default nodes then leave out the one that refuses archive reads)")
    p.add_argument("--nodes", help="comma-separated JSON-RPC URLs (default: four public nodes)")
    p.add_argument("--selftest", action="store_true")
    a = p.parse_args()
    if a.selftest:
        return selftest()
    if not a.safes:
        p.error("--safes is required (or --selftest)")
    nodes = a.nodes.split(",") if a.nodes else (NODES[1:] if a.block is not None else NODES)
    agg, det = count(Reader(nodes, gap=0.1), load_safes(a.safes), block=a.block)
    if a.out:
        json.dump(agg, open(a.out, "w"), indent=1)
    if a.detail:
        json.dump(det, open(a.detail, "w"), indent=1)
    print(json.dumps(agg, indent=1))


if __name__ == "__main__":
    sys.exit(main())
