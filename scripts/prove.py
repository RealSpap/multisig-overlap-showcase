#!/usr/bin/env python3
"""One command that replays what this repository publishes. No key, no account, public RPC endpoints and the files of this clone only, standard library only, about a minute.

    python3 scripts/prove.py                 # from a clone of the repository
    python3 scripts/prove.py --fact ID       # replay one fact of facts/public-facts.json (ID is its "id")
    python3 scripts/prove.py --selftest      # offline: plants falsified values and checks that each one comes out as a DIFFERENCE or UNREAD

Every line says OK, DIFFERENCE or UNREAD. An RPC error, a missing file or an empty answer is UNREAD, never a zero and never a pass.
Exit 0: everything read and equal. Exit 1: at least one DIFFERENCE. Exit 2: nothing differs but something was UNREAD. Exit 3: the script itself failed or was called wrongly.

What it replays:
  1. the "At a glance" table of README.md (protocols per Part, multisig addresses per Part, their sums), the headline sentence and the four protocol badges (badge-data-total.json, badge-data-mainnet-protocols.json, badge-data-superchain.json, badge-data-part3.json). Nothing else in the README is compared;
  2. the six-field facts of facts/public-facts.json (network and chainId, named block, owners and threshold of a Safe, a signer shared by several Safes):
     the chain id each endpoint reports, the hash and time of the named block, the owners and threshold of every Safe read now AND at its named block, and for a shared signer that the address has no contract code.
     Two endpoints per network are asked. The chain id and the Safe now must be answered by both and agree, otherwise UNREAD (or DIFFERENCE if they disagree). The named block and the Safe at that block need one answer (an endpoint may not keep old state) and no endpoint may contradict the file.
     A fact whose Safe has changed since its block is a DIFFERENCE: the published line has expired and must be re-read, which is the point of the check;
  3. that FACTS.md says what facts/public-facts.json says.

What it does NOT prove: that a signer is one person, or who holds a key (an address shared by two Safes is a fact about addresses); that a Safe not listed in
facts/public-facts.json is as published (README.md carries many more readings than the facts file replays); anything about an endpoint that did not answer (those lines say UNREAD).
"""
import concurrent.futures as cf, datetime, json, os, re, sys, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..")
OK, DIFF, UNREAD = "OK", "DIFFERENCE", "UNREAD"
_ERR = {}   # last error seen per endpoint, printed under an UNREAD so that the cause is visible
SEL_OWNERS, SEL_THRESHOLD = "0xa0e67e2b", "0xe75235b8"   # getOwners(), getThreshold() of a Safe
# network name -> (chain id, public RPC endpoints). Two endpoints per network, both are asked.
NETWORKS = {
    "ethereum": (1, ["https://ethereum-rpc.publicnode.com", "https://rpc.mevblocker.io"]),
    "optimism": (10, ["https://mainnet.optimism.io", "https://optimism-rpc.publicnode.com"]),
    "base": (8453, ["https://mainnet.base.org", "https://base-rpc.publicnode.com"]),
    "arbitrum": (42161, ["https://arb1.arbitrum.io/rpc", "https://arbitrum-one-rpc.publicnode.com"]),
}
NAMES = {"ethereum": "Ethereum mainnet", "optimism": "Optimism", "base": "Base", "arbitrum": "Arbitrum One"}
FIELDS = ("id", "claim", "network", "chain_id", "address", "block", "threshold", "owners", "replay", "cast", "expires_utc", "read", "read_by")
ADDR = re.compile(r"^0x[0-9a-f]{40}$")
DEADLINE = time.time() + 100
_UA = {"content-type": "application/json", "User-Agent": "multisig-overlap-prove/1"}


# ---------------------------------------------------------------- reads (the only part that touches the network)
def rpc(url, method, params, tries=3):
    """One JSON-RPC call -> the result, or None unless the endpoint answered this call with a result (an error or a timeout is None, never a value)."""
    body = json.dumps({"jsonrpc": "2.0", "id": 7, "method": method, "params": params}).encode()
    for i in range(tries):
        if i and time.time() > DEADLINE: return None   # past the time budget no retry starts: the read ends UNREAD
        try:
            r = json.load(urllib.request.urlopen(urllib.request.Request(url, body, _UA), timeout=25))
            if isinstance(r, dict) and r.get("id") == 7 and r.get("result") is not None: return r["result"]
            _ERR[url] = "answered without a result for " + method
        except Exception as e: _ERR[url] = "%s: %s" % (type(e).__name__, str(e)[:60])
        time.sleep(1 + i)
    return None


def decode_threshold(h):
    """getThreshold() answer -> int, or None when it is not exactly one 32-byte word (an empty answer is not a Safe)."""
    if not isinstance(h, str) or not re.fullmatch(r"0x[0-9a-fA-F]{64}", h): return None
    v = int(h, 16)
    return v if v >= 1 else None   # a Safe's threshold is at least 1


def decode_owners(h):
    """getOwners() answer (ABI: offset, length, items) -> sorted lowercase addresses, or None when the encoding does not hold together."""
    if not isinstance(h, str) or not re.fullmatch(r"0x(?:[0-9a-fA-F]{64})+", h): return None
    w = [h[2 + i:2 + i + 64] for i in range(0, len(h) - 2, 64)]
    if int(w[0], 16) != 32 or len(w) < 2: return None
    n = int(w[1], 16)
    if len(w) != 2 + n or n == 0: return None
    if any(int(x[:24], 16) != 0 for x in w[2:]): return None
    owners = sorted("0x" + x[24:] for x in (y.lower() for y in w[2:]))
    return owners if len(set(owners)) == len(owners) else None


def read_safe(url, address, block):
    """-> {"threshold", "owners"} read on one endpoint at `block` (a hex tag, or "latest"), or None."""
    t = rpc(url, "eth_call", [{"to": address, "data": SEL_THRESHOLD}, block])
    o = rpc(url, "eth_call", [{"to": address, "data": SEL_OWNERS}, block])
    t, o = decode_threshold(t), decode_owners(o)
    return None if t is None or o is None else {"threshold": t, "owners": o}


def read_network(net, chain_block_numbers, addresses):
    """Everything one network needs: per endpoint the chain id, the hash of each named block, and the Safes now.
    -> {url: {"chain_id", "blocks": {number: hash}, "now": {address: reading or None}}}."""
    out = {}
    for url in NETWORKS[net][1]:
        cid = rpc(url, "eth_chainId", [])
        blocks = {}
        for n in chain_block_numbers:
            # the header is small; some endpoints do not serve it, then the whole block is asked for (several nodes sit behind one URL and some answer null for a block the others have: ask again)
            b = rpc(url, "eth_getHeaderByNumber", [hex(n)], tries=2) or rpc(url, "eth_getBlockByNumber", [hex(n), False], tries=6)
            blocks[n] = {"hash": b.get("hash"), "time": int(b["timestamp"], 16)} if isinstance(b, dict) and b.get("hash") and b.get("timestamp") else None
        now = {a: read_safe(url, a, "latest") for a in addresses}
        out[url] = {"chain_id": int(cid, 16) if isinstance(cid, str) and cid.startswith("0x") else None, "blocks": blocks, "now": now}
    return out


def read_pinned(net, address, number):
    """The Safe at the named block on each endpoint (archive state: an endpoint that does not keep it answers None)."""
    return {u: read_safe(u, address, hex(number)) for u in NETWORKS[net][1]}


# ---------------------------------------------------------------- pure comparisons (tested offline, with planted falsified values)
def valid_time(t):
    try: datetime.datetime.strptime(str(t), "%Y-%m-%dT%H:%M:%SZ"); return True
    except ValueError: return False


def check_schema(doc):
    """The six-field rule, as a pure function of the facts file. -> list of problems (empty when the file is well formed)."""
    bad = []
    for f in doc.get("facts", []):
        fid = f.get("id", "?")
        for k in FIELDS:
            if k not in f or f[k] in (None, "", []): bad.append("%s: field %s is missing" % (fid, k))
        net = f.get("network")
        if net not in NETWORKS: bad.append("%s: unknown network %r" % (fid, net))
        elif f.get("chain_id") != NETWORKS[net][0]: bad.append("%s: chain_id %r is not the chain id of %s (%d)" % (fid, f.get("chain_id"), net, NETWORKS[net][0]))
        if not ADDR.match(str(f.get("address", ""))): bad.append("%s: address is not lowercase 0x + 40 hex" % fid)
        b = f.get("block") or {}
        if not isinstance(b.get("number"), int) or not re.fullmatch(r"0x[0-9a-f]{64}", str(b.get("hash", ""))) or not valid_time(b.get("time_utc")): bad.append("%s: block needs number, hash and time_utc (YYYY-MM-DDTHH:MM:SSZ)" % fid)
        elif valid_time(doc.get("read_utc")) and doc["read_utc"] < b["time_utc"]: bad.append("%s: read_utc is earlier than its block" % fid)
        m = re.search(r"threshold (\d+) of (\d+) owners", str(f.get("claim", "")))
        if not m or int(m.group(1)) != f.get("threshold") or int(m.group(2)) != len(f.get("owners") or []): bad.append("%s: the claim does not say threshold %s of %s owners as the fields do" % (fid, f.get("threshold"), len(f.get("owners") or [])))
        if str(f.get("address", "")) not in str(f.get("cast", "")) or "--block %s" % (b.get("number")) not in str(f.get("cast", "")): bad.append("%s: the cast command does not name the address and the block of the fact" % fid)
        if f.get("read") not in ("read", "unread"): bad.append("%s: read must be read or unread" % fid)
        if f.get("read") == "unread" and not f.get("unread_reason"): bad.append("%s: an unread fact must say why it could not be read" % fid)
        if len(f.get("owners") or []) and (not isinstance(f.get("threshold"), int) or f["threshold"] > len(f["owners"]) or f["threshold"] < 1): bad.append("%s: threshold %r with %d owners" % (fid, f.get("threshold"), len(f["owners"])))
        if f.get("owners") and f["owners"] != sorted(set(f["owners"])): bad.append("%s: owners must be sorted lowercase and distinct" % fid)
        try: datetime.datetime.strptime(str(f.get("expires_utc", "")), "%Y-%m-%d")
        except ValueError: bad.append("%s: expires_utc must be a real date, YYYY-MM-DD" % fid)
    if not valid_time(doc.get("read_utc")): bad.append("read_utc must be YYYY-MM-DDTHH:MM:SSZ")
    if not doc.get("facts"): bad.append("the facts file lists no fact")
    ids = [f.get("id") for f in doc.get("facts", [])]
    if len(ids) != len(set(ids)): bad.append("duplicate fact ids")
    where = [(f.get("network"), f.get("address")) for f in doc.get("facts", [])]
    if len(where) != len(set(where)): bad.append("two facts name the same address on the same network")
    by_id = {f.get("id"): f for f in doc.get("facts", [])}
    for o in doc.get("overlaps", []):
        oid = o.get("id", "?")
        for k in ("id", "claim", "network", "chain_id", "signer", "safes"):
            if o.get(k) in (None, "", []): bad.append("overlap %s: field %s is missing" % (oid, k))
        if not ADDR.match(str(o.get("signer", ""))): bad.append("overlap %s: signer is not lowercase 0x + 40 hex" % oid)
        if o.get("network") in NETWORKS and o.get("chain_id") != NETWORKS[o["network"]][0]: bad.append("overlap %s: chain_id does not match its network" % oid)
        if o.get("signer_is_eoa") is not True: bad.append("overlap %s: signer_is_eoa must be true (the claim says externally owned)" % oid)
        if len(set(o.get("safes") or [])) < 2: bad.append("overlap %s: a shared signer needs at least two Safes" % oid)
        for s in o.get("safes", []):
            if s not in by_id: bad.append("overlap %s names the unknown fact %s" % (oid, s))
            elif by_id[s].get("network") != o.get("network"): bad.append("overlap %s: fact %s is on another network" % (oid, s))
    return bad


def cmp_chain_id(net, reads):
    want = NETWORKS[net][0]; got = [r["chain_id"] for r in reads.values()]; seen = [g for g in got if g is not None]
    if any(g != want for g in seen): return DIFF, "%s: an endpoint reports chain id %s, expected %d" % (net, seen, want)
    if len(seen) < len(got): return UNREAD, "%s: only %d of %d endpoints answered eth_chainId" % (net, len(seen), len(got))
    return OK, "%s: chain id %d on %d of %d endpoints" % (net, want, len(seen), len(got))


def cmp_block(net, number, want_hash, want_time, reads):
    """The named block: its hash and its time (UTC, to the second) must be what the file says on every endpoint that returns it; one answer is enough."""
    got = [r["blocks"].get(number) for r in reads.values()]
    got = [g for g in got if g]
    if not got: return UNREAD, "%s block %d: no endpoint returned it" % (net, number)
    for g in got:
        if g["hash"].lower() != want_hash.lower(): return DIFF, "%s block %d: the chain says %s, the file says %s" % (net, number, g["hash"], want_hash)
        t = datetime.datetime.fromtimestamp(g["time"], datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        if t != want_time: return DIFF, "%s block %d: the chain says %s, the file says %s" % (net, number, t, want_time)
    return OK, "%s block %d: hash %s... and time %s on %d endpoint(s)" % (net, number, want_hash[:12], want_time, len(got))


def cmp_now(fact, readings, pinned, today=None):
    """readings: {url: reading or None} of the Safe now, from every endpoint asked. pinned: the same at the named block.
    The published line is OK only when it equals the Safe now (both endpoints) and the Safe at its own block (at least one endpoint, none contradicting)."""
    same = lambda r: r["threshold"] == fact["threshold"] and r["owners"] == fact["owners"]
    now = [r for r in readings.values() if r]
    if any(r != now[0] for r in now): return DIFF, "%s: the endpoints disagree with each other" % fact["id"]
    pin = [r for r in pinned.values() if r]
    if any(r != pin[0] for r in pin): return DIFF, "%s: the endpoints disagree about the Safe at block %d" % (fact["id"], fact["block"]["number"])
    if pin and not same(pin[0]): return DIFF, "%s: the published line does not match the Safe at its own block %d" % (fact["id"], fact["block"]["number"])
    if now and not same(now[0]):
        r = now[0]; what = []
        if r["threshold"] != fact["threshold"]: what.append("threshold %d now, %d published" % (r["threshold"], fact["threshold"]))
        gone, new = sorted(set(fact["owners"]) - set(r["owners"])), sorted(set(r["owners"]) - set(fact["owners"]))
        if gone: what.append("%d owner(s) left" % len(gone))
        if new: what.append("%d owner(s) joined" % len(new))
        return DIFF, "%s: %s%s" % (fact["id"], ", ".join(what), "; the published line was true at block %d, so it has expired" % fact["block"]["number"] if pin else "; the named block could not be read to tell whether it was ever true")
    if len(now) < len(readings): return UNREAD, "%s: only %d of %d endpoints answered getThreshold() and getOwners() now" % (fact["id"], len(now), len(readings))
    if not pin: return UNREAD, "%s: no endpoint could serve the Safe at block %d (old state may be pruned)" % (fact["id"], fact["block"]["number"])
    r = now[0]
    late = " (past its expiry %s, still equal)" % fact["expires_utc"] if today and today > fact["expires_utc"] else ""
    return OK, "%s: %d-of-%d, same owners now (%d endpoints) and at block %d (%d endpoint(s))%s" % (fact["id"], r["threshold"], len(r["owners"]), len(now), fact["block"]["number"], len(pin), late)


def cmp_overlap(o, facts_by_id, now):
    """A signer shared by several Safes: every named Safe, read now, must list the signer. `now` is {fact id: reading or None}."""
    miss, unread = [], []
    for sid in o["safes"]:
        r = now.get(sid)
        if r is None: unread.append(sid); continue
        if o["signer"] not in r["owners"]: miss.append(sid)
    if miss: return DIFF, "%s: signer %s...%s is not an owner of %s" % (o["id"], o["signer"][:8], o["signer"][-4:], ", ".join(miss))
    if unread: return UNREAD, "%s: not read: %s" % (o["id"], ", ".join(unread))
    return OK, "%s: signer %s...%s is an owner of all %d Safes" % (o["id"], o["signer"][:8], o["signer"][-4:], len(o["safes"]))


def cmp_eoa(o, codes):
    """The signer of an overlap is an externally owned address when the endpoints return no contract code for it. codes: {url: hex string or None}."""
    got = [c for c in codes.values() if isinstance(c, str)]
    if not got: return UNREAD, "%s: no endpoint returned the code of the signer" % o["id"]
    if any(c not in ("0x", "0x0") for c in got): return DIFF, "%s: the signer has contract code, it is not an externally owned address" % o["id"]
    return OK, "%s: the signer has no contract code on %d endpoint(s)" % (o["id"], len(got))


ROW = lambda name, text: re.search(r"^\| %s \|(.+)\|\s*$" % name, text, re.M)


def parse_readme_counts(text):
    """The 'At a glance' table of README.md -> the numbers it states, None for a number it does not state in the expected form (a short row is not a crash)."""
    pc, mc = ROW("Protocols checked", text), ROW("Multisigs checked", text)
    cell = lambda m, i: m.group(1).split("|")[i].strip() if m and i < len(m.group(1).split("|")) else ""
    first = lambda m, i: (lambda x: int(x.group(1)) if x else None)(re.match(r"(\d+)", cell(m, i)))
    find = lambda m, i, pat: (lambda x: int(x.group(1)) if x else None)(re.search(pat, cell(m, i)))
    c = {"p1": first(pc, 0), "p2": first(pc, 1), "p3": first(pc, 2), "ptotal": first(pc, 3),
         "m1": find(mc, 0, r"(\d+) confirmed real Safes"), "m2": find(mc, 1, r"^(\d+) distinct multisig"), "m3": find(mc, 2, r"^(\d+) confirmed real Safes"), "mtotal": find(mc, 3, r"^(\d+) confirmed multisig addresses")}
    h = re.search(r"Measured across (\d+) protocol entries", text)
    c["headline"] = int(h.group(1)) if h else None
    return c


def cmp_readme(c, badges):
    """Counts of the README against each other, the headline and the badge files. badges: {"total", "mainnet", "superchain", "part3"} (ints or None)."""
    miss = [k for k in ("p1", "p2", "p3", "ptotal", "m1", "m2", "m3", "mtotal", "headline") if c.get(k) is None]
    if miss: return UNREAD, "README.md: could not read %s in the expected form" % ", ".join(miss)
    bad = []
    if c["p1"] + c["p2"] + c["p3"] != c["ptotal"]: bad.append("protocols %d + %d + %d is not %d" % (c["p1"], c["p2"], c["p3"], c["ptotal"]))
    if c["m1"] + c["m2"] + c["m3"] != c["mtotal"]: bad.append("multisig addresses %d + %d + %d is not %d" % (c["m1"], c["m2"], c["m3"], c["mtotal"]))
    if c["headline"] != c["ptotal"]: bad.append("headline says %d protocol entries, the table says %d" % (c["headline"], c["ptotal"]))
    for k, want in (("total", c["ptotal"]), ("mainnet", c["p1"]), ("superchain", c["p2"]), ("part3", c["p3"])):
        if badges.get(k) is None: return UNREAD, "badge file for %s not readable" % k
        if badges[k] != want: bad.append("badge %s says %d, the README says %d" % (k, badges[k], want))
    if bad: return DIFF, "; ".join(bad)
    return OK, "README: %d + %d + %d = %d protocols, %d + %d + %d = %d multisig addresses, headline and four badges agree" % (c["p1"], c["p2"], c["p3"], c["ptotal"], c["m1"], c["m2"], c["m3"], c["mtotal"])


def read_stamp(utc):
    """2026-11-13T15:48:51Z -> 'read at 15:48Z on 13 November 2026' (the form used in FACTS.md)."""
    d = datetime.datetime.strptime(utc, "%Y-%m-%dT%H:%M:%SZ")
    return "read at %02d:%02dZ on %d %s %d" % (d.hour, d.minute, d.day, d.strftime("%B"), d.year)


def facts_markdown(doc):
    """FACTS.md, rebuilt from the JSON. The file is committed so that it can be read without any tool; prove.py checks that it still says what the JSON says."""
    L = ["# Public facts", "",
         "Generated from facts/public-facts.json with python3 scripts/prove.py --write-facts-md. Each fact has six fields: the claim, the network with its chain id, a named block, the replay command, an expiry date and whether it was read.", "",
         "A fact is a statement about addresses on one network at one block. It stays true only until one of its owners or its threshold changes. After its expiry date it is not vouched for until it is read again. The full owner lists are in facts/public-facts.json.", ""]
    for f in doc["facts"]:
        net = "%s (chain id %d)" % (NAMES.get(f["network"], f["network"]), f["chain_id"])
        L += ["## " + f["id"], "", "- Claim: " + f["claim"], "- Address: `%s` on %s" % (f["address"], net),
              "- Block: number %d on %s, hash `%s`, %s" % (f["block"]["number"], net, f["block"]["hash"], f["block"]["time_utc"]),
              "- Read: %s" % (("yes, %s, %s" % (read_stamp(doc["read_utc"]), f["read_by"])) if f["read"] == "read" else "no, " + f["unread_reason"]),
              "- Expires: %s" % f["expires_utc"], "- Replay: `%s`" % f["replay"], "- Same read with cast on %s: `%s`" % (net, f["cast"]), ""]
    if doc.get("overlaps"):
        L += ["## Signers shared by several Safes", ""]
        for o in doc["overlaps"]:
            L += ["- %s: %s. Signer `%s` on %s (chain id %d), Safes %s, %s. An address does not say who holds it, so whether one person holds the key cannot be read from the chain." % (o["id"], o["claim"], o["signer"], NAMES.get(o["network"], o["network"]), o["chain_id"], ", ".join(o["safes"]), read_stamp(doc["read_utc"]))]
        L += [""]
    return "\n".join(L)


# ---------------------------------------------------------------- the run
def load(path):
    try:
        with open(path, encoding="utf-8") as fh: return fh.read()
    except OSError: return None


def run(only=None, today=None):
    lines = []
    add = lambda v, d: lines.append((v, d))
    readme = load(os.path.join(ROOT, "README.md"))
    if only is None:
        if readme is None: add(UNREAD, "README.md not readable")
        else:
            badges = {}
            for k, fn in (("total", "badge-data-total.json"), ("mainnet", "badge-data-mainnet-protocols.json"), ("superchain", "badge-data-superchain.json"), ("part3", "badge-data-part3.json")):
                t = load(os.path.join(ROOT, fn))
                try: badges[k] = int(json.loads(t)["message"]) if t else None
                except (ValueError, KeyError, TypeError): badges[k] = None
            add(*cmp_readme(parse_readme_counts(readme), badges))
    raw = load(os.path.join(ROOT, "facts", "public-facts.json"))
    if raw is None: add(UNREAD, "facts/public-facts.json not readable"); return lines
    try: doc = json.loads(raw)
    except ValueError: add(DIFF, "facts/public-facts.json is not valid JSON"); return lines
    problems = check_schema(doc)
    add(DIFF if problems else OK, "facts file: " + ("; ".join(problems[:6]) if problems else "%d facts, %d overlaps, six fields each, chain ids match" % (len(doc["facts"]), len(doc.get("overlaps", [])))))
    if problems: return lines
    md = load(os.path.join(ROOT, "FACTS.md"))
    if only is None:
        add(*((UNREAD, "FACTS.md not readable") if md is None else ((OK, "FACTS.md says what the JSON says") if md.rstrip() == facts_markdown(doc).rstrip() else (DIFF, "FACTS.md differs from the JSON: run python3 scripts/prove.py --write-facts-md"))))
    facts = [f for f in doc["facts"] if only is None or f["id"] == only]
    if only and not facts: add(DIFF, "no fact has the id %s" % only); return lines
    nets = sorted({f["network"] for f in facts})
    def one(net):
        fs = [f for f in facts if f["network"] == net]
        return net, read_network(net, sorted({f["block"]["number"] for f in fs}), sorted({f["address"] for f in fs}))
    with cf.ThreadPoolExecutor(len(nets) or 1) as ex: reads = dict(ex.map(one, nets))
    now = {}
    for net in nets:
        add(*cmp_chain_id(net, reads[net]))
        for n in sorted({f["block"]["number"] for f in facts if f["network"] == net}):
            h = {f["block"]["hash"] for f in facts if f["network"] == net and f["block"]["number"] == n}
            for hh in h:
                tt = next(f["block"]["time_utc"] for f in facts if f["network"] == net and f["block"]["number"] == n and f["block"]["hash"] == hh)
                add(*cmp_block(net, n, hh, tt, reads[net]))
    for f in facts:
        rd = {u: r["now"].get(f["address"]) for u, r in reads[f["network"]].items()}
        add(*cmp_now(f, rd, read_pinned(f["network"], f["address"], f["block"]["number"]), today))
        got = [r for r in rd.values() if r]
        now[f["id"]] = got[0] if len(got) == len(rd) and all(r == got[0] for r in got) else None
    if only is None:
        for o in doc.get("overlaps", []):
            add(*cmp_overlap(o, {f["id"]: f for f in facts}, now))
            add(*cmp_eoa(o, {u: rpc(u, "eth_getCode", [o["signer"], "latest"]) for u in NETWORKS[o["network"]][1]}))
    return lines


def report(lines):
    for v, d in lines: print("%-10s %s" % (v, d))
    n = {k: sum(1 for v, _ in lines if v == k) for k in (OK, DIFF, UNREAD)}
    print("\n%d OK, %d DIFFERENCE, %d UNREAD" % (n[OK], n[DIFF], n[UNREAD]))
    if n[UNREAD]: print("An UNREAD is not a pass and not a difference: public endpoints rate-limit and drop requests, run it again.")
    if n[UNREAD] and _ERR: print("last error per endpoint: " + "; ".join("%s %s" % (u.split("//")[1].split("/")[0], e) for u, e in sorted(_ERR.items())))
    return 1 if n[DIFF] else (2 if n[UNREAD] else 0)


# ---------------------------------------------------------------- self-test: every planted falsehood must come out as DIFFERENCE or UNREAD, never OK
def selftest():
    A = "0x" + "11" * 20; B = "0x" + "22" * 20; C = "0x" + "33" * 20
    H = "0x" + "ab" * 32
    fact = {"id": "t", "claim": "x on Base: threshold 2 of 2 owners.", "network": "base", "chain_id": 8453, "address": A, "read_by": "r",
            "block": {"number": 5, "hash": H, "time_utc": "2026-11-13T12:00:00Z"}, "threshold": 2, "owners": sorted([B, C]), "replay": "r",
            "cast": "cast call %s \"getThreshold()(uint256)\" --rpc-url u --block 5" % A, "expires_utc": "2026-11-27", "read": "read"}
    good = {"threshold": 2, "owners": sorted([B, C])}
    ok = lambda r: r[0] == OK
    two = lambda x, y=None: {"u": x, "v": x if y is None else y}
    t = []
    t.append(("equal reading now and at the block is OK", ok(cmp_now(fact, two(good), {"u": good, "v": None}))))
    t.append(("planted threshold 1 now is a DIFFERENCE", cmp_now(fact, two(dict(good, threshold=1)), {"u": good})[0] == DIFF))
    t.append(("a swapped owner now is a DIFFERENCE", cmp_now(fact, two(dict(good, owners=sorted([B, A]))), {"u": good})[0] == DIFF))
    t.append(("no answer now is UNREAD, not a pass", cmp_now(fact, two(None), {"u": good})[0] == UNREAD))
    t.append(("one endpoint of two empty is UNREAD, not a pass", cmp_now(fact, {"u": good, "v": None}, {"u": good})[0] == UNREAD))
    t.append(("two endpoints that disagree are a DIFFERENCE", cmp_now(fact, two(good, dict(good, threshold=1)), {"u": good})[0] == DIFF))
    t.append(("changed since the block says it expired", "expired" in cmp_now(fact, two(dict(good, threshold=1)), {"u": good})[1]))
    t.append(("a Safe equal now but different at the named block is a DIFFERENCE", cmp_now(fact, two(good), {"u": dict(good, owners=sorted([B, A]))})[0] == DIFF))
    t.append(("a block that cannot be served leaves it UNREAD", cmp_now(fact, two(good), {"u": None, "v": None})[0] == UNREAD))
    t.append(("endpoints that disagree at the block are a DIFFERENCE", cmp_now(fact, two(good), {"u": good, "v": dict(good, threshold=1)})[0] == DIFF))
    blk = lambda h, ts=1794571200: {"u": {"blocks": {5: {"hash": h, "time": ts}}}}
    t.append(("the right block hash and time are OK", ok(cmp_block("base", 5, H, "2026-11-13T12:00:00Z", blk(H)))))
    t.append(("a wrong block hash is a DIFFERENCE", cmp_block("base", 5, H, "2026-11-13T12:00:00Z", blk("0x" + "cd" * 32))[0] == DIFF))
    t.append(("a wrong block time is a DIFFERENCE", cmp_block("base", 5, H, "2025-11-13T12:00:00Z", blk(H))[0] == DIFF))
    t.append(("a missing block is UNREAD", cmp_block("base", 5, H, "2026-11-13T12:00:00Z", {"u": {"blocks": {5: None}}})[0] == UNREAD))
    t.append(("the wrong chain id is a DIFFERENCE", cmp_chain_id("base", {"u": {"chain_id": 1}, "v": {"chain_id": 8453}})[0] == DIFF))
    t.append(("an unanswered chain id is UNREAD", cmp_chain_id("base", {"u": {"chain_id": None}, "v": {"chain_id": None}})[0] == UNREAD))
    t.append(("one of two chain ids unanswered is UNREAD", cmp_chain_id("base", {"u": {"chain_id": 8453}, "v": {"chain_id": None}})[0] == UNREAD))
    t.append(("both chain ids right is OK", ok(cmp_chain_id("base", {"u": {"chain_id": 8453}, "v": {"chain_id": 8453}}))))
    o = {"id": "o", "claim": "c", "network": "base", "chain_id": 8453, "signer": B, "signer_is_eoa": True, "safes": ["t", "u"]}
    t.append(("a signer missing from the Safe is a DIFFERENCE", cmp_overlap(o, {}, {"t": {"threshold": 1, "owners": [C]}, "u": good})[0] == DIFF))
    t.append(("an unread Safe leaves the overlap UNREAD", cmp_overlap(o, {}, {"t": None, "u": good})[0] == UNREAD))
    t.append(("a signer present everywhere is OK", ok(cmp_overlap(o, {}, {"t": good, "u": good}))))
    fact2 = dict(fact, id="u", address=B)
    fact2["cast"] = fact["cast"].replace(A, B)
    doc = {"read_utc": "2026-11-13T12:05:00Z", "facts": [fact, fact2], "overlaps": [o]}
    t.append(("a well formed facts file has no problem", check_schema(doc) == []))
    for k in ("block", "expires_utc", "replay", "read", "chain_id", "owners", "threshold", "address", "claim", "network", "cast", "read_by"):
        d = dict(doc, facts=[{x: y for x, y in fact.items() if x != k}], overlaps=[])
        t.append(("a fact without %s is refused" % k, bool(check_schema(d))))
    only = lambda **kw: dict(doc, facts=[dict(fact, **kw)], overlaps=[])
    t.append(("chain id 1 on base is refused", bool(check_schema(only(chain_id=1)))))
    t.append(("an unread fact without a reason is refused", bool(check_schema(only(read="unread")))))
    t.append(("an uppercase address is refused", bool(check_schema(only(address="0x" + "AB" * 20)))))
    t.append(("a claim that disagrees with the threshold field is refused", bool(check_schema(only(claim="x on Base: threshold 4 of 2 owners.")))))
    t.append(("a claim that disagrees with the owner count is refused", bool(check_schema(only(claim="x on Base: threshold 2 of 9 owners.")))))
    t.append(("a block time in the wrong year is refused when it is after read_utc", bool(check_schema(only(block=dict(fact["block"], time_utc="2027-01-01T00:00:00Z"))))))
    t.append(("a block time that is not a time is refused", bool(check_schema(only(block=dict(fact["block"], time_utc="yesterday"))))))
    t.append(("an expiry that is not a date is refused", bool(check_schema(only(expires_utc="2026-99-99")))))
    t.append(("a cast command for another address is refused", bool(check_schema(only(cast=fact["cast"].replace(A, B))))))
    t.append(("a cast command for another block is refused", bool(check_schema(only(cast=fact["cast"].replace("--block 5", "--block 6"))))))
    t.append(("an empty facts file is refused", bool(check_schema(dict(doc, facts=[], overlaps=[])))))
    t.append(("two facts on the same address and network are refused", bool(check_schema(dict(doc, facts=[fact, dict(fact, id="w")], overlaps=[])))))
    t.append(("a missing read_utc is refused", bool(check_schema({k: v for k, v in doc.items() if k != "read_utc"}))))
    o2 = lambda **kw: dict(doc, overlaps=[dict(o, **kw)])
    t.append(("an overlap over two Safes of its network is well formed", check_schema(o2()) == []))
    t.append(("an overlap naming no fact is refused", bool(check_schema(o2(safes=["t", "zz"])))))
    t.append(("an overlap on one Safe only is refused", bool(check_schema(o2(safes=["t"])))))
    t.append(("an overlap naming the same Safe twice is refused", bool(check_schema(o2(safes=["t", "t"])))))
    t.append(("an overlap on another network than its Safes is refused", bool(check_schema(o2(network="ethereum", chain_id=1)))))
    t.append(("an overlap without a network is refused", bool(check_schema(dict(doc, overlaps=[{k: v for k, v in o.items() if k != "network"}])))))
    t.append(("an overlap with signer_is_eoa false is refused", bool(check_schema(o2(signer_is_eoa=False)))))
    t.append(("an overlap without signer_is_eoa is refused", bool(check_schema(dict(doc, overlaps=[{k: v for k, v in o.items() if k != "signer_is_eoa"}])))))
    t.append(("a signer with contract code is a DIFFERENCE", cmp_eoa(o, {"u": "0x6080"})[0] == DIFF))
    t.append(("a signer without code on all endpoints is OK", ok(cmp_eoa(o, {"u": "0x", "v": "0x"}))))
    t.append(("an unanswered code read is UNREAD", cmp_eoa(o, {"u": None})[0] == UNREAD))
    t.append(("an empty getThreshold answer is not a Safe", decode_threshold("0x") is None))
    t.append(("a threshold of zero is not a Safe", decode_threshold("0x" + "0" * 64) is None))
    t.append(("an empty getOwners answer is not a Safe", decode_owners("0x") is None))
    enc = "0x" + "%064x" % 32 + "%064x" % 2 + "0" * 24 + B[2:] + "0" * 24 + C[2:]
    t.append(("a well formed owner list decodes", decode_owners(enc) == sorted([B, C])))
    t.append(("an owner list with a wrong length is refused", decode_owners(enc[:-64]) is None))
    t.append(("an owner list with a repeated owner is refused", decode_owners("0x" + "%064x" % 32 + "%064x" % 2 + "0" * 24 + B[2:] + "0" * 24 + B[2:]) is None))
    text = "| Protocols checked | 214 | 105 | 109 (across 11 chains) | 428 (sum) |\n| Multisigs checked | 395 tested, 328 confirmed real Safes | 265 distinct multisig addresses across 255 | 185 confirmed real Safes | 778 confirmed multisig addresses (328 + 265 + 185) |\nMeasured across 428 protocol entries on 25 chains"
    c = parse_readme_counts(text); bd = {"total": 428, "mainnet": 214, "superchain": 105, "part3": 109}
    t.append(("a consistent README is OK", ok(cmp_readme(c, bd))))
    t.append(("a wrong total is a DIFFERENCE", cmp_readme(dict(c, ptotal=429), bd)[0] == DIFF))
    t.append(("a wrong headline is a DIFFERENCE", cmp_readme(dict(c, headline=411), bd)[0] == DIFF))
    t.append(("a stale badge is a DIFFERENCE", cmp_readme(c, dict(bd, total=411))[0] == DIFF))
    t.append(("an unreadable badge is UNREAD", cmp_readme(c, dict(bd, part3=None))[0] == UNREAD))
    t.append(("a README without the table is UNREAD", cmp_readme(parse_readme_counts("nothing"), bd)[0] == UNREAD))
    t.append(("a table row with too few cells is UNREAD, not a crash", cmp_readme(parse_readme_counts("| Protocols checked | 1 | 2 |\n"), bd)[0] == UNREAD))
    t.append(("FACTS.md is rebuilt from the JSON", "## t" in facts_markdown(dict(doc, facts=[dict(fact, read_by="r")], overlaps=[]))))
    t.append(("the read stamp has the form used in FACTS.md", read_stamp("2026-11-13T15:48:51Z") == "read at 15:48Z on 13 November 2026"))
    failed = [name for name, passed in t if not passed]
    for name, passed in t: print("%-6s %s" % ("ok" if passed else "FAILED", name))
    print("\n%d checks, %d failed" % (len(t), len(failed)))
    return 1 if failed else 0


USAGE = "usage: python3 scripts/prove.py [--fact ID | --selftest | --write-facts-md]"

if __name__ == "__main__":
    a = sys.argv[1:]
    try:
        if a == ["--selftest"]: sys.exit(selftest())
        if a == ["--write-facts-md"]:
            p = os.path.join(ROOT, "facts", "public-facts.json")
            with open(os.path.join(ROOT, "FACTS.md"), "w", encoding="utf-8") as fh: fh.write(facts_markdown(json.load(open(p, encoding="utf-8"))) + "\n")
            sys.exit(0)
        if a and not (len(a) == 2 and a[0] == "--fact"): print(USAGE); sys.exit(3)
        sys.exit(report(run(a[1] if a else None, datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"))))
    except SystemExit: raise
    except Exception as e:   # a crash is not a DIFFERENCE: exit 3, so that exit 1 keeps meaning "the published facts differ from the chain"
        print("prove.py failed before it could judge: %s: %s" % (type(e).__name__, e)); sys.exit(3)
