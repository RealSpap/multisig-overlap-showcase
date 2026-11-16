# Contributing

This repository publishes a measurement: which signer keys and Safes recur across DeFi protocols and chains. Every way of helping ends in something anyone can re-read, not in an opinion. Replies are best effort, with no promised delay.

## Five first tasks

Each needs only Python 3 and a public RPC endpoint.

1. **Run the check.** `python3 scripts/prove.py` re-reads the Safes of FACTS.md on public RPC endpoints. Tell me about any DIFFERENCE or UNREAD line, with the date you ran it.
2. **Replay one fact.** `python3 scripts/prove.py --fact curve-emergency-dao-ethereum` replays one fact of facts/public-facts.json on its own.
3. **Replay one fact by hand.** Run the two `cast` commands printed under a fact in FACTS.md and compare the owners and the threshold with facts/public-facts.json.
4. **Check one identity claim.** Pick an entry marked High confidence in the docs and check its address against the protocol's own documentation; tell me if the address is not in the source it cites.
5. **Report a change.** If a Safe of FACTS.md has different owners since its named block, open an issue with the chain, the address and the block.

## What I do not accept

- A change to a finding without evidence anyone can re-read (a transaction hash, a block number, an address with the call to make, a public document).
- Anything that holds a private key, a seed phrase, a password or private data.
- Statements about the character or intent of a named person.
- Promotional additions.

## Running the checks

```bash
python3 scripts/check_structure.py
```

It refuses a new entry at the root, a forbidden file name, a README over 80 lines or holding a dash.
