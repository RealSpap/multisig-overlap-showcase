# multisig-overlap

![License](https://img.shields.io/badge/license-all%20rights%20reserved-blue)
![Status](https://img.shields.io/badge/status-active%20research-brightgreen)
![Identities found](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FRealSpap%2Fmultisig-overlap-showcase%2Fmain%2Fbadge-data.json)
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


## Disclaimer

This report presents an independent, factual analysis of publicly available on-chain data (smart contract code, multisig signer sets, governance transactions) as of the date noted in Status/Method above. Statements about which addresses or individuals hold administrative, multisig, or governance keys are based solely on on-chain records and publicly disclosed information cited inline; they are not allegations of wrongdoing, and no claim of illegal conduct, fraud, or misconduct is made or implied. Concentration of control or key-holder identity is reported as an observed structural fact, not as a moral or legal judgment on the individuals named. Findings reflect a snapshot in time; on-chain configurations, signer sets, and governance parameters can and do change after publication, and this report is not updated automatically to reflect such changes. This is independent research, not commissioned or audited by the protocols discussed, and it does not constitute legal, financial, or investment advice. Any individual or entity named in this report who believes information about them is inaccurate or outdated is invited to contact the author via [X](https://x.com/RealSpap) with supporting evidence; corrections will be issued promptly and transparently. Readers should independently verify all cited addresses, transactions, and figures before relying on them.

## Method

41 protocols' multisig contracts (Gnosis Safe) checked directly on-chain via `getOwners()`: no API key, no third-party indexer, pure RPC reads against a public Ethereum node. 65 candidate addresses tested, 71 unique signer slots recovered.

## Findings

8 addresses hold signer power on 2+ independent protocols, sorted by how many protocols each one touches. All 8 are identified by name or known pseudonym, each backed by a primary-source citation:

| Rank | Identity | Protocols | Reach | Role |
|---|---|---|---|---|
| 1 | **Michael Egorov** | Abracadabra + Yearn + Prisma | 3 protocols | Founder of Curve Finance |
| 1 | **c2tp.eth** | Convex (his own protocol) + Prisma + Votium | 3 protocols | Pseudonymous creator of Convex Finance |
| 3 | **Ernesto Boado** (BGD Labs) | Lido + Balancer | 2 protocols | Infrastructure/security provider working with multiple protocols |
| 3 | **Pablo Veyrat** | Angle (his own protocol) + Morpho | 2 protocols | Founder of Angle Protocol |
| 3 | **Julien Bouteloup** | Abracadabra + StakeDAO (his own protocol) | 2 protocols | Founder of StakeDAO / Rekt News, early Curve team |
| 3 | **"Tommy"** | Votium (his own protocol) + Convex | 2 protocols | Known representative of Votium |
| 3 | **Sam Kazemian** (high confidence, not independently name-confirmed) | Frax (his own protocol) + Prisma | 2 protocols | Founder of Frax Finance |
| 3 | **Matthew Graham** | Gearbox + TokenLogic (his own service) | 2 protocols | Founder of TokenLogic |

*What this means in practice: Egorov and c2tp.eth each sit on 3 independent protocols' emergency keys at once. A single compromised key for either one puts 3 unrelated protocols' funds at risk simultaneously, not 1.*

Three of the eight (Egorov, c2tp, Kazemian) sit together on Prisma Finance's emergency multisig, a deliberate, publicly disclosed design choice by Prisma to recruit established protocol founders for credibility, not a hidden concentration. The other five are more organic: independent protocols with no obvious institutional link to each other.

## Live verification

[dune.com/s_pap/multisig-overlap](https://dune.com/s_pap/multisig-overlap): a self-computing query that skips the point-in-time snapshot entirely and replays the actual on-chain event history of all 65 Safe contracts, recomputing current ownership fresh every time it runs.

**Get notified**, no account needed on this repo: click Watch, then Custom, then Releases only, on this repo's GitHub page for a per-pass update feed. On Dune, star the dashboard to keep it in your own list, or set a scheduled alert on the query for a ping the moment a tracked Safe's owner set actually changes on-chain, not just when this repo gets updated.

7 of the 8 identities reproduce live from raw chain data this way. Getting there took two event types: the standard `AddedOwner`/`RemovedOwner` events, plus `SafeSetup`, which Safe v1.3.0+ emits once at creation with the full founding owner list. `AddedOwner` itself is never emitted for owners set at genesis, so without `SafeSetup` a Safe's original signers are invisible to pure event replay. Confirmed directly on Prisma Finance's creation transaction: 2 logs total, one `SafeSetup`, zero `AddedOwner`.

One identity, Julien Bouteloup, doesn't reproduce this way. Not because he's any less real, he's confirmed the same way as everyone else, a direct live `getOwners()` read, but because his second seat sits on a Safe running v1.1.1, old enough that its creation transaction emits nothing describing its owners, only a bare `ProxyCreation`. Convex's own multisig has the identical limitation, which is why c2tp.eth's Convex seat also doesn't show up live even though Votium and Prisma both do. Both gaps were confirmed by reading the actual transaction logs on Etherscan, not assumed from a pattern.

## Open data

The live query's own result table is queryable directly through [Dune's Query API](https://docs.dune.com/api-reference/overview/query-api) by anyone with a free Dune API key, no scraping needed: pull the same 8 identities the same way this page does, recomputed fresh on every call.

## What's checked next

41 protocols is a pilot, not a finished survey. Open a GitHub Issue on this repo to suggest the next protocol to check; a thumbs-up on an existing suggestion counts as a vote. The Superchain-specific follow-up already covers 79 more: [multisig-overlap](https://github.com/RealSpap/multisig-overlap-showcase).

## Verification

Every identity claim is backed by a primary-source citation, tracked against a falsification test and a confidence level, and checked against a mechanical grounding lexical-grounding tool before publication.

## License

All rights reserved. This repository documents the method and results; the tool itself is available under a commercial license, see above.
