# multisig-overlap

![License](https://img.shields.io/badge/license-all%20rights%20reserved-blue)
![Status](https://img.shields.io/badge/status-active%20research-brightgreen)
![Follow](https://img.shields.io/badge/follow-%40RealSpap-000000?logo=x)

**The headline finding:** 8 named individuals hold multisig signer keys across 2+ unrelated DeFi protocols at once, identified across 41 protocols checked directly on-chain. 7 of the 8 identities reproduce live from raw blockchain event history alone, not just a point-in-time snapshot. [Full findings below](#findings) · [Live dashboard](https://dune.com/s_pap/multisig-overlap) · [Contact for licensing / custom research](https://x.com/RealSpap)

| | |
|---|---|
| **The question** | if one person's emergency key were compromised, how many unrelated DeFi protocols would be affected at once |
| **Scope checked** | 41 protocols, 65 candidate Gnosis Safe contracts, read directly on-chain |
| **What stands out** | 8 people hold signer power on 2 or more protocols; 7 of 8 reproduce live from raw event history, not a snapshot |
| **Proof it runs** | every identity backed by a primary-source citation, checked against a falsification test and a mechanical grounding tool |

Every major DeFi protocol discloses its own emergency and governance multisig signers, usually in its own docs. Nobody aggregates this across protocols, so nobody could previously answer: if this one person's key were compromised, how many independent protocols would be affected at the same time?

Extended to Optimism's Superchain in a follow-up project: [multisig-overlap](https://github.com/RealSpap/multisig-overlap-showcase).

## Access to the tool

The verification method behind this research is available under a commercial license, not published in this repository. The findings below were produced with it and are independently reproducible by anyone with the same access; this repo documents the results, not the mechanism. Reach out via [RealSpap on X](https://x.com/RealSpap) for licensing.

## Method

41 protocols' multisig contracts (Gnosis Safe) checked directly on-chain via `getOwners()`: no API key, no third-party indexer, pure RPC reads against a public Ethereum node. 65 candidate addresses tested, 71 unique signer slots recovered.

## Findings

8 addresses hold signer power on 2+ independent protocols. All 8 are identified by name or known pseudonym, each backed by a primary-source citation:

| Identity | Protocols | Role |
|---|---|---|
| **Ernesto Boado** (BGD Labs) | Lido + Balancer | Infrastructure/security provider working with multiple protocols |
| **Pablo Veyrat** | Angle (his own protocol) + Morpho | Founder of Angle Protocol |
| **Michael Egorov** | Abracadabra + Yearn + Prisma | Founder of Curve Finance |
| **c2tp.eth** | Convex (his own protocol) + Prisma + Votium | Pseudonymous creator of Convex Finance |
| **Julien Bouteloup** | Abracadabra + StakeDAO (his own protocol) | Founder of StakeDAO / Rekt News, early Curve team |
| **"Tommy"** | Votium (his own protocol) + Convex | Known representative of Votium |
| **Sam Kazemian** (high confidence, not independently name-confirmed) | Frax (his own protocol) + Prisma | Founder of Frax Finance |
| **Matthew Graham** | Gearbox + TokenLogic (his own service) | Founder of TokenLogic |

Three of the eight (Egorov, c2tp, Kazemian) sit together on Prisma Finance's emergency multisig, a deliberate, publicly disclosed design choice by Prisma to recruit established protocol founders for credibility, not a hidden concentration. The other five are more organic: independent protocols with no obvious institutional link to each other.

## Live verification

[dune.com/s_pap/multisig-overlap](https://dune.com/s_pap/multisig-overlap): a self-computing query that skips the point-in-time snapshot entirely and replays the actual on-chain event history of all 65 Safe contracts, recomputing current ownership fresh every time it runs.

7 of the 8 identities reproduce live straight from raw chain data this way. Getting there took two event types: the standard `AddedOwner`/`RemovedOwner` events, plus `SafeSetup`, which Safe v1.3.0+ emits once at creation with the full founding owner list. `AddedOwner` itself is never emitted for owners set at genesis, so without `SafeSetup` a Safe's original signers are invisible to pure event replay. Confirmed directly on Prisma Finance's creation transaction: 2 logs total, one `SafeSetup`, zero `AddedOwner`.

One identity, Julien Bouteloup, doesn't reproduce this way. Not because he's any less real, he's confirmed the same way as everyone else, a direct live `getOwners()` read, but because his second seat sits on a Safe running v1.1.1, old enough that its creation transaction emits nothing describing its owners, only a bare `ProxyCreation`. Convex's own multisig has the identical limitation, which is why c2tp.eth's Convex seat also doesn't show up live even though Votium and Prisma both do. Both gaps were confirmed by reading the actual transaction logs on Etherscan, not assumed from a pattern.

## Verification

Every identity claim is backed by a primary-source citation, tracked against a falsification test and a confidence level, and checked against a mechanical grounding lexical-grounding tool before publication.

## License

All rights reserved. This repository documents the method and results; the tool itself is available under a commercial license, see above.
