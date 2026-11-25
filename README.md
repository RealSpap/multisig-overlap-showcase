# multisig-overlap

![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-blue) ![Code: MIT](https://img.shields.io/badge/code-MIT-blue)
![Protocols checked (All parts)](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FRealSpap%2Fmultisig-overlap-showcase%2Fmain%2Fbadge-data-total.json)
[![Check your Safe: free tool](https://img.shields.io/badge/check%20your%20safe-free%20tool-orange)](https://realspap.github.io/tools/check-your-safe.html)

**The headline finding:** the widest single signer key found sits on 5 independent protocols at once, and one Safe governs the core L1 contracts of 5 Superchain chains. Measured across 428 protocol entries on 25 chains (Ethereum mainnet plus 24 others), each checked directly on-chain.

The same question, checked at three scales: Ethereum mainnet, Optimism's Superchain, and Arbitrum with 10 more L2s and sidechains. Details and every address are in [docs](docs/part-1-mainnet.md).

## Redo it

```bash
git clone https://github.com/RealSpap/multisig-overlap-showcase && cd multisig-overlap-showcase && python3 scripts/prove.py
```

No key, no account, public RPC endpoints, Python 3 only. It checks that the table below, the headline sentence and the protocol badges agree, then re-reads the Safes listed in [FACTS.md](FACTS.md) (network and chain ID, a named block, owners and threshold now and at that block). Every line says OK, DIFFERENCE or UNREAD; an endpoint that does not answer is UNREAD, never a pass. It proves that the published facts match the chain when you run it. It does not prove who holds a key.

## At a glance

| | Part 1: Mainnet | Part 2: Superchain | Part 3: Other L2s | Total |
|---|---|---|---|---|
| Protocols checked | 214 | 105 | 109 (across 11 chains) | 428 (sum of the three Parts; a protocol present in several Parts counts once per Part) |
| Multisigs checked | 395 candidate addresses tested, 328 confirmed real Safes | 265 distinct multisig addresses across 255 deployments (311 Gnosis Safe readings plus 11 custom-multisig readings) | 185 confirmed real Safes | 778 confirmed multisig addresses (328 + 265 + 185, summed per Part) |
| Chains covered | Ethereum mainnet | 13 | 11 | 25 |

The counting rule and the full table are in [docs/method.md](docs/method.md). `scripts/prove.py` fails if the protocol and multisig counts, the headline and the badges disagree. Each update is a dated release: [how to be notified](docs/about.md#get-notified).

## What is inside

| Where | What |
|---|---|
| [docs/part-1-mainnet.md](docs/part-1-mainnet.md), [part-2-superchain.md](docs/part-2-superchain.md), [part-3-arbitrum-and-other-l2.md](docs/part-3-arbitrum-and-other-l2.md) | The findings by scale |
| [docs/method.md](docs/method.md), [docs/limits.md](docs/limits.md) | Method, confidence vocabulary, what is not shown |
| [docs/about.md](docs/about.md) | Access to the tool, about this research, licence details |
| [FACTS.md](FACTS.md), [facts](facts) | Replayable facts, each with network, chain ID, block and expiry |
| [docs/tracked-safes-modules.md](docs/tracked-safes-modules.md), [facts/tracked-safes.tsv](facts/tracked-safes.tsv) | How many of the Safes I follow have a module, with the list and a script that recounts them |
| [docs/same-keys-other-threshold.md](docs/same-keys-other-threshold.md) | One Safe address with the same four owners and two thresholds, with the commands that read it |
| [CONTINUE.md](CONTINUE.md) | How to carry on if I stop |

## Limits

These are structural observations about publicly visible key configurations, not allegations about any person or team. No individual is named: a signer who is a person appears under a neutral label or by address. More in [docs/limits.md](docs/limits.md).

## Help and licence

Found a signer set that changed? Open an issue with the chain, the address and the block. See [CONTRIBUTING](.github/CONTRIBUTING.md). Findings: [CC BY 4.0](LICENSE). Scripts: MIT ([LICENSE-CODE](LICENSE-CODE)). Cite with [CITATION.cff](CITATION.cff). Updates are published as dated releases ([feed](https://github.com/RealSpap/multisig-overlap-showcase/releases.atom)).
