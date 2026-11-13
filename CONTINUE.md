# If this project stops

This repository is meant to stay useful, and checkable, if nobody updates it any more.

- **Everything is plain text.** The findings are in README.md, the replayable facts in FACTS.md and facts/public-facts.json. Nothing needs a tool, an account or a server to be read.
- **Checking needs Python 3 only.** `python3 scripts/prove.py` re-reads the listed Safes on public RPC endpoints and says OK, DIFFERENCE or UNREAD for each line. `python3 scripts/prove.py --selftest` runs offline.
- **A fact expires.** Each fact in FACTS.md carries an expiry date, 14 days after it was read. After that date it is not vouched for until someone reads it again. A DIFFERENCE means the Safe has changed since the named block: the line is out of date, not necessarily wrong when it was written.
- **To refresh a fact by hand:** run the two `cast` commands printed under it in FACTS.md (drop `--block` and its number to read the current state), copy the threshold and the owner list into facts/public-facts.json with the new block number, block hash, read date and expiry, run `python3 scripts/prove.py --write-facts-md`, then run `python3 scripts/prove.py` and keep the lines that say OK.
- **The counts** in the README table and in the badge files are kept in step by `scripts/sync_badges.py`; `scripts/prove.py` fails if the table, the headline sentence and the four protocol badges disagree.
- **Licence.** The findings are CC BY 4.0 and the code is MIT: anyone may fork this repository and continue it, with credit.
- **What is not here.** The tooling that ran the original checks is private. Every Safe listed in FACTS.md can be re-read by hand with the Safe functions `getOwners()` and `getThreshold()` at the address and chain printed there. The README carries many more readings, some with shortened addresses, and not every multisig it covers is a Safe.
