# multisig-overlap

![License](https://img.shields.io/badge/license-all%20rights%20reserved-blue)
![Status](https://img.shields.io/badge/status-active%20research-brightgreen)
![Identities found (mainnet)](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FRealSpap%2Fmultisig-overlap-showcase%2Fmain%2Fbadge-data-mainnet.json)
![Protocols tracked (Superchain)](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FRealSpap%2Fmultisig-overlap-showcase%2Fmain%2Fbadge-data-superchain.json)
![Follow](https://img.shields.io/badge/follow-%40RealSpap-000000?logo=x)

**The headline finding:** the same question, checked at two scales. On Ethereum mainnet, 8 named individuals hold multisig signer keys across 2 or more unrelated DeFi protocols at once, identified across 41 protocols checked directly on-chain. Extended to Optimism's Superchain, the same pattern recurs 6 more times: one brand-new named individual (aavechan.eth), two of the original 8 turning up again on new chains, and two chain-operator entities concentrating upgrade keys across multiple chains at once. Separately, 30+ protocols reuse the identical Gnosis Safe signer set on multiple chains at once, so spreading exposure across a protocol's chain deployments doesn't actually diversify against key compromise. [Mainnet findings](#part-1-mainnet) · [Superchain findings](#part-2-superchain) · [Contact for licensing / custom research](https://x.com/RealSpap)

**Want this method run on your protocol, or a custom research pass? License it: DM [@RealSpap](https://x.com/RealSpap) on X.**

## At a glance

| | Mainnet | Superchain |
|---|---|---|
| Protocols checked | 41 | 79 |
| Safes checked | 71 signer slots tested, 65 confirmed as real Safe contracts | 200 Safes across 166 deployments |
| Chains covered | Ethereum mainnet | 13 |
| Shared-key findings | 8 named identities holding signer power on 2+ protocols | 6 documented cross-protocol or cross-chain signer-sharing cases, plus 30+ protocols sharing an identical signer set across chains |
| Research depth | 41-protocol scope, each of the 8 findings independently verified on-chain | 31 research passes, still growing |
| Live verification | Yes, on-chain event replay | Dashboard only; on-chain event replay planned for a future pass |

Every major DeFi protocol discloses its own emergency and governance multisig signers, usually in its own docs. Nobody aggregates that across protocols or chains, so nobody could previously answer: if one person's key, or one shared signer set, were compromised, how many independent protocols or chains would be affected at the same time? This research answers that at two scales: first across 41 major protocols on Ethereum mainnet, then across Optimism's Superchain specifically, where the same protocol is often deployed on a dozen chains at once.

## Access to the tool

The verification method behind this research is available under a commercial license, not published in this repository. The findings below were produced with it and are independently reproducible by anyone with the same access; this repo documents the results, not the mechanism. Reach out via [RealSpap on X](https://x.com/RealSpap) for licensing.

## Disclaimer

This report presents an independent, factual analysis of publicly available on-chain data (smart contract code, multisig signer sets, governance transactions) as of the date noted in the Status/Method sections below. Statements about which addresses or individuals hold administrative, multisig, or governance keys are based solely on on-chain records and publicly disclosed information cited inline; they are not allegations of wrongdoing, and no claim of illegal conduct, fraud, or misconduct is made or implied. Concentration of control or key-holder identity is reported as an observed structural fact, not as a moral or legal judgment on the individuals named. Findings reflect a snapshot in time; on-chain configurations, signer sets, and governance parameters can and do change after publication, and this report is not updated automatically to reflect such changes. This is independent research, not commissioned or audited by any protocol discussed, and it does not constitute legal, financial, or investment advice. Any individual or entity named in this report who believes information about them is inaccurate or outdated is invited to contact the author via [X](https://x.com/RealSpap) with supporting evidence; corrections will be issued promptly and transparently. Readers should independently verify all cited addresses, transactions, and figures before relying on them.

## Part 1: Mainnet

### Method

Last verified: 2026-09-09

41 protocols' multisig contracts (Gnosis Safe) checked directly on-chain via `getOwners()`: no API key, no third-party indexer, pure RPC reads against a public Ethereum node. 71 signer slots tested, 65 confirmed as real Safe contracts.

### Findings

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

Matthew Graham and TokenLogic reappear in Part 2 below: the same footprint that starts here on Gearbox and TokenLogic's own Ethereum Safe extends onto three of Aave's Superchain Safes as well.

### Live verification

[dune.com/s_pap/multisig-overlap](https://dune.com/s_pap/multisig-overlap): a self-computing query that skips the point-in-time snapshot entirely and replays the actual on-chain event history of all 65 Safe contracts, recomputing current ownership fresh every time it runs.

**Get notified**, no account needed on this repo: click Watch, then Custom, then Releases only, on this repo's GitHub page for a per-pass update feed. On Dune, star the dashboard to keep it in your own list, or set a scheduled alert on the query for a ping the moment a tracked Safe's owner set actually changes on-chain, not just when this repo gets updated.

The live query relies on parsing on-chain event history rather than static contract reads. Some older Safes were created before their deployment transaction logged the data a pure event-based rebuild needs, so 2 of the 8 identities (Julien Bouteloup's second seat and c2tp.eth's Convex seat) are instead confirmed by a direct `getOwners()` read, independently cross-checked by manually reading the relevant transaction logs on Etherscan.

### Open data (Mainnet)

The live query's own result table is queryable directly through [Dune's Query API](https://docs.dune.com/api-reference/api-overview) by anyone with a free Dune API key, no scraping needed: pull the same 8 identities the same way this page does, recomputed fresh on every call.

### What's checked next (Mainnet)

41 protocols is a pilot, not a finished survey. Open a GitHub Issue on this repo to suggest the next protocol to check; a thumbs-up on an existing suggestion counts as a vote (this sets research priority only; checks are still run under the same licensed method, not opened to contributors). The Superchain-specific follow-up already covers 79 more protocols: see Part 2 below.

### Caveats (Mainnet)

- One of the 8 identities (Julien Bouteloup's second seat) and one seat behind another (c2tp.eth's Convex seat) don't reproduce through live event replay, because they sit on Safe versions old enough that their creation transactions don't log the data a pure event-based rebuild needs; both are confirmed by a direct `getOwners()` read instead. See Live verification above.
- 41 protocols is a pilot, not a finished survey (see What's checked next). A protocol not listed here hasn't been checked, not confirmed clean.
- Three of the eight identified signers (Egorov, c2tp, Kazemian) sit together on Prisma Finance's multisig by Prisma's own deliberate, publicly disclosed design choice to recruit established founders for credibility, not a hidden concentration; treating that case the same as the other five would overstate how coordinated the overlap actually is.
- One candidate address needed a correction from a sibling project in this research program. Ethena's `Owner_Multisig_3of11` is a real, confirmed 10-signer Safe, but an independent check in `defi-admin-key-risk` found it does not match the actual `owner()` of either EthenaMinting V2 or the USDe token (both a 24-hour Timelock instead), nor EthenaMinting V1's actual owner (a separate 5-of-10 Safe). The Safe is real; what it currently controls at Ethena, if anything, is unconfirmed.

## Part 2: Superchain

Extension of Part 1 to Optimism's Superchain (OP Mainnet, Base, Mode, Unichain, Ink, Soneium, Lisk, Celo, Zora Network, World Chain, Fraxtal, Derive Chain, and BOB so far). Part 1 asks "does the same person hold emergency keys on multiple, unrelated protocols at once?" This part asks a Superchain-specific variant: "does the same signer set control a protocol's admin multisig on multiple chains at once, and does anyone share keys across genuinely different Superchain protocols?"

### Method

200 Gnosis Safe multisig contracts across 166 protocol/chain deployments, checked directly on-chain: no API key, no third-party indexer, pure RPC reads against public nodes. Every address was collected from a primary source (official docs or GitHub repo) and independently re-verified on-chain before being used. This also covers who controls the 13 tracked chains themselves at the L1 (Ethereum mainnet) level, not just the dapps deployed on them: a real Gnosis Safe was confirmed as the ProxyAdminOwner on all 13, with World Chain's separate SystemConfigOwner the sole exception, a bare EOA rather than a Safe.

### The exposure leaderboard

Every case below is one of the six findings detailed further down, sorted by how many Safe deployments a single signer, or a single shared Safe, actually touches. These are the numbers already stated in the findings below, just gathered in one place first.

| Rank | Who | Reach | Category |
|---|---|---|---|
| 1 | Matthew Graham / TokenLogic | 3 protocols, 3 chains, 5 Safes (across this project and Part 1) | Cross-protocol individual |
| 2 | `0x8f02b4a4...` (Pablo Veyrat) | 2 protocols (Morpho Blue, Angle), 6 Superchain Safes, plus both protocols' Ethereum mainnet Safes | Cross-protocol individual |
| 3 | Optimism Foundation / Security Council Safe | 5 of 13 Superchain chains share the identical ProxyAdminOwner Safe | Chain governance |
| 4 | Conduit (RaaS operator) | Signers recur across at least 4 nominally independent chains' own governance Safes | Chain governance |
| 5 | `aavechan.eth` | 2 protocols (QiDao/Mai Finance, Aave), 3 Safe deployments | Cross-protocol individual |
| 6 | `0x9A73D57B...` | 2 protocols (Compound III, Resolv), 3 Safe deployments | Cross-protocol individual |

### Findings

**Four separate cases of one signer holding real power across genuinely unrelated protocols:**

1. `0x8f02b4a44Eacd9b8eE7739aa0BA58833DD45d002` is an owner of both Morpho Blue's governance Safe (**Base, World Chain, and now Fraxtal too**) and Angle Protocol's Guardian Safe (**Optimism, Base, and Celo**), six separate Safe deployments in total. Morpho and Angle have no institutional relationship. The same address also sits on both protocols' Ethereum mainnet Safes (already on record in Part 1 for Angle), so a single compromised key here threatens Morpho and Angle simultaneously, across mainnet and six Superchain deployments. It's identified with **high confidence as Pablo Veyrat, co-founder of Angle Protocol and Merkl**, named explicitly with this exact address by Morpho Association's own governance forum post proposing him as a multisig signer.
   *What this means in practice: a depositor treating Morpho Blue and Angle as independent risk exposures is wrong. One compromised key ends both at once, on six chains simultaneously.*

2. **Matthew Graham / TokenLogic**, already named in Part 1 as an owner of both Gearbox's Technical Multisig and TokenLogic's own Safe on Ethereum, is now also confirmed as an owner of three of Aave's role-specific Safes (Merkl rewards distribution, a "Robot Guardian" automation role, and TokenLogic's own execution Safe), deployed at the identical addresses on both Ink and Celo. A second TokenLogic team member from that same Ethereum Safe is confirmed alongside him on both chains. This is the widest documented footprint of any named individual across this research: three protocols, three chains, five Safes.
   *What this means in practice: this is the single widest blast radius identified across this research. A key held by one small team now touches Gearbox, TokenLogic, and Aave at once.*

3. **aavechan.eth**, an ENS-verified, Basescan-labeled Aave ecosystem operator, is confirmed as an owner of both QiDao/Mai Finance's Base and now Fraxtal Guardian Safes and Aave's Celo "Masiv" Safe: three separate Safe deployments across two independently-run protocols with no institutional relationship, caught by the script's own cross-reference logic rather than assumed.
   *What this means in practice: an independent Aave-ecosystem operator, not Aave itself, also holds a guardian key on an unrelated lending protocol.*

4. `0x9A73D57BB1fB280C5672A13f655675De25F13b70` is an owner of both Compound III's Base Pause Guardian Safe and Resolv's Base and Soneium Token Owner Safes. Compound III and Resolv have no institutional relationship. Found by the same cross-reference logic once Resolv's Safes were added to the registry, not assumed in advance.
   *What this means in practice: a pause-guardian key for one blue-chip lending protocol doubles as a token-owner key for an unrelated stablecoin issuer.*

5. **5 of the 13 tracked chains (Optimism, Mode, Ink, Soneium, Zora) delegate their entire L1 chain-governance authority, the ProxyAdminOwner role able to upgrade nearly any part of that chain's L1 bridge/rollup contracts, to the identical Gnosis Safe**: a nested 2-of-2 between the Optimism Foundation and the Security Council. Unichain's own separate Safe shares 2 of its 3 signers with that same pair. This isn't one protocol deployed six times: these are six independently branded chains, several run day-to-day by entirely separate companies, that have each chosen to hand core upgrade rights to the same small, centrally Optimism-Foundation-operated group.
   *What this means in practice: this is the single largest concentration in the dataset. One Safe's signers can upgrade the core L1 contracts of 6 of the 13 chains this project tracks.*

6. **Conduit**, the Rollup-as-a-Service operator behind Mode and Derive Chain, controls both chains' core chain-governance role through the identical Safe. Four of that Safe's 11 signers individually also sit on Zora Network's and/or BOB's own separate chain-governance Safes: the same infrastructure-provider personnel holding upgrade rights across at least four nominally independent chains at once.
   *What this means in practice: several chains presented to users as independently operated share upgrade-key personnel with a common infrastructure vendor, not just with each other.*

Separately, one more pseudonymous signer (`0xb291232F480F41c75802C4a60F1D2AC03404Afef`) shows up on Aave's core Protocol Guardian Safe on Optimism, Base, Soneium, and Celo, and also on a distinct 3-person cluster controlling four of Aave's Ink and Celo Safes: a single Aave ecosystem operator trusted with keys across at least six separate Safe formations.

Beyond those cases, the sample also confirms a **Superchain-specific pattern**: several protocols run the exact same signer set across multiple chains at once.

| Protocol | Signal |
|---|---|
| **Silo Finance** | Literally the same Safe contract address deployed on Optimism, Base, and Ink; the Ink instance has one extra owner beyond the 5 shared with the other two |
| **Aave V3** | Several Safe contract addresses (Protocol Guardian and four role-specific Safes) deployed identically across up to five chains: Optimism, Base, Soneium, Ink, and Celo |
| **Beefy Finance** | Same 6 owners now across six separately-deployed Safes: Optimism, Base, Mode, Unichain, Lisk, and Fraxtal (no live Safe on Celo; the address book itself sets it to the zero address) |
| **Angle Protocol** | Same 3 owners across three separately-deployed Safes: Optimism, Base, and Celo. One of these 3 is the Morpho overlap above |
| **Extra Finance** | Same 3 owners on two separately-deployed Safes (one per chain) |
| **Overnight Finance** | 4 of 5 owners shared between the two chains' Safes |
| **Contango / Rodeo Finance** | Both its CoreMultisig and OperatorMultisig Safes run fully identical signer sets on Optimism and Base. The OperatorMultisig is even deployed at the literal same contract address on both chains |
| **Zora** | Its three Safes (Optimism, Base, and Zora Network) are separate deployments that share signers pairwise, but no single signer set is fully identical across all three |
| **ether.fi** | Almost fully identical 7-signer Controller Safe across five chains (Optimism, Base, Mode, Unichain, and Ink), with Base and Ink deployed at the literal same contract address; Unichain swaps in one different signer |
| **Renzo Protocol** | Identical 5-signer admin Safe spans six chains (Optimism, Base, Mode, Unichain, Ink, and World Chain), with Optimism and Base at the literal same contract address; Ink adds one extra signer on top of the same 5 |
| **Morpho Blue** | Its DAO Safe now spans three chains, Base, World Chain, and Fraxtal, with the identical 9 owners on all three, including the address already linked to the Angle Protocol overlap above |
| **QiDao / Mai Finance** | Its Base and Fraxtal Guardian Safes return the identical 6 owners, including the address already linked to the Aave overlap above |
| **Yearn Finance** | Its Optimism ("oChad") and Base ("bChad") multisigs return the identical 5 owners |
| **Puffer Finance** | Its Base and Soneium multisigs share 2 of their respective 13 and 6 owners: a partial overlap, not a full-identical-set one |
| **1inch** | Its Aggregation Router V6 owner Safe returns the identical 5 owners at a 3-of-5 threshold on Optimism, Base, and Unichain |
| **CoW Protocol** | Its admin Safe is deployed at the literal same address on Optimism and Ink (identical 9 owners, 4-of-9); Base is a separate Safe with those same 9 plus one extra, at 4-of-10 |
| **ParaSwap / Velora** | Its V5 admin Safe returns the identical 12 owners at a 6-of-12 threshold on both Base and Optimism |
| **Odos** | Its Router V3 owner Safe is deployed at the literal same address on Optimism, Base, and Unichain, and Mode has its own address, with different owner counts and thresholds per chain (1-of-6, 1-of-5, 2-of-6, and 2-of-7 respectively). A single signer holds the threshold on two of these chains, not a clean identical-set case |
| **Velodrome (Optimism) / Aerodrome (Base)** | 4 of their Emergency Council members overlap. Expected, not a new finding: Aerodrome is Velodrome's own sister deployment on Base, same team by design |
| **API3** | Its "manager multisig" is deployed at the literal same contract address with the identical 8 owners on seven chains (Optimism, Base, Mode, Unichain, Soneium, World Chain, and Fraxtal), the widest spread in the dataset, ahead of Renzo Protocol |
| **deBridge** | Its admin multisig (holding `DEFAULT_ADMIN_ROLE` on its core contracts) returns the identical 8 owners at a 5-of-8 threshold on both Optimism and Base, at two different Safe addresses |
| **Chainlink Data Feeds** | Its ETH/USD feed owner Safe returns the identical 9 owners at a 4-of-9 threshold on four chains (Optimism, Unichain, Soneium, and Celo), at four different Safe addresses per chain; the same feed's owner on Base and Ink is not a Safe at all |
| **Curve Finance** | Its Emergency DAO Safe is deployed at the literal same contract address with the identical 9 owners at a 5-of-9 threshold on six chains at once (Base, Celo, Fraxtal, Ink, Optimism, and Unichain), the widest same-address propagation in this dataset |
| **Ethena** | Its multisig returns the identical 10 owners at a 5-of-10 threshold on four chains (Optimism, Base, Mode, and Fraxtal), with Optimism and Fraxtal at the literal same contract address |
| **Frax Finance** | Its OFT-owner Safes return an identical 6-signer, 3-of-6 committee on six chains (Base, Mode, Ink, Unichain, World Chain, and Optimism), distinct from its own Comptroller-role Safes on Fraxtal and Optimism, which share only a partial subset of that committee |
| **Resolv** | Its Base and Soneium Safes share 4 of their respective 6 owners: a partial overlap, not a full-identical-set one |
| **Euler V2** | Its DAO Safe is deployed at a different address on each of three chains (Base, BOB, and Unichain), with the identical 8 owners and 4-of-8 threshold on all three |
| **Venus Protocol** | Its Guardian Safe is confirmed on Optimism (3-of-6), Base (3-of-7), and Unichain (3-of-6, at the literal same contract address as Base), with 6 of Optimism's owners also present on Base and Unichain |
| **OpenSea / Seaport** | The owner of OpenSea's own default Seaport conduit (not the Seaport protocol itself, which has no owner anywhere) is the identical 7-signer, 5-of-7 Safe on five chains at once (Optimism, Base, Zora Network, Unichain, and Soneium), each at a different Safe address |
| **Manifold** | Its Marketplace V2 owner is the identical 3-signer, 2-of-3 Safe on Optimism and Base, at two different Safe addresses |
| **Farcaster** | Its core registry Safe (IdRegistry, KeyRegistry, IdGateway, KeyGateway, SignedKeyRequestValidator, plus StorageRegistry's admin roles) is the identical 10-signer, 3-of-10 Safe on both Optimism and Base, at the literal same contract address; a separate 8-signer, 2-of-8 Safe controls RecoveryProxy alone, sharing 7 of its 8 signers with the main Safe |
| **Hyperlane** | Its Mailbox and ProxyAdmin owner is the identical 10-signer, 6-of-10 Safe on both Optimism and Base, at the literal same contract address; on ten other deployed chains that same admin surface is relayed cross-chain through an Interchain Account proxy rather than living locally as a Safe |
| **World ID** | Its WorldIDRouter and WorldIDVerifier owner is the identical Safe address on both World Chain and Optimism, but with two different signer sets: 5 owners, 2-of-5, on World Chain, and 7 owners, 2-of-7, on Optimism, with World Chain's 5 forming a proper subset of Optimism's 7 |
| **Superfluid** | Its protocol governance Safe is the identical 4-signer, 2-of-4 Safe on all three chains where it's deployed at all: Optimism, Base, and Celo, reached through a different governance proxy contract per chain but resolving to the same owner everywhere |
| **Zora (protocol) / Zora Network (chain)** | 3 of Zora Network's own 10-signer L1 chain-governance Safe are the identical individuals already in this table above as Zora-the-protocol's Factory_Upgrade_Gate_Owner signers on Base, Optimism, and Zora Network itself. Expected, not a new institutional link: Zora Inc. operates both the protocol and the chain |
| **Frax Finance / Fraxtal** | Fraxtal's entire 5-signer L1 chain-governance Safe is the identical signer set as Frax Finance's own Comptroller and OFT_Owner roles already tracked across seven chains. Expected, not a new institutional link: Frax operates its own chain |

The practical read: a user spreading exposure across a protocol's deployments on different Superchain chains to "diversify" isn't actually diversifying against key compromise if it's the same multisig signing off everywhere. One compromised key set can hit every chain simultaneously. That's a different risk shape than Part 1's "unrelated founders sharing keys" story, but the Morpho/Angle, Matthew Graham/TokenLogic, aavechan.eth, and Compound III/Resolv cases show both risk shapes combine in practice.

This dataset has grown through 31 research passes so far, each one adding a new protocol category, a new chain, or re-checking an existing finding.

### Dashboard

[dune.com/s_pap/multisig-overlap-public](https://dune.com/s_pap/multisig-overlap-public): same findings, same wording as this README.

**Get notified of new passes**, no account needed on this repo: click Watch, then Custom, then Releases only, on this repo's GitHub page. Every research pass gets tagged as a release with the same text as its CHANGELOG entry. On Dune, star the dashboard to have it in your own list, or set a scheduled alert on the query for a ping when a tracked Safe's owner set changes.

### Open data (Superchain)

The dashboard's own table above is queryable directly through [Dune's Query API](https://docs.dune.com/api-reference/api-overview) by anyone with a free Dune API key, no scraping needed.

### What's checked next (Superchain)

Not a finished survey by design (see Status below). Open a GitHub Issue on this repo to suggest the next protocol or chain to check; a thumbs-up on an existing suggestion counts as a vote (this sets research priority only; checks are still run under the same licensed method, not opened to contributors).

### Verification

Every claim in this research is backed by a primary-source citation, tracked against a falsification test and a confidence level, and checked against a mechanical grounding lexical-grounding tool before publication. On the Superchain side, 92/92 hypotheses pass clean on both checks. The method: collect from a primary source (official docs or GitHub repo), re-verify on-chain, cross-check against every address already in the registry, log the falsification test that would disprove the claim. Same discipline across both parts of this research.

### Status

Last verified: 2026-09-09

200 Safes across 166 deployments and 79 protocols, not a finished survey. The most recent pass turned to who controls the 13 tracked chains themselves rather than the dapps on them: a real Gnosis Safe confirmed as ProxyAdminOwner on all 13, 5 of them sharing the identical Optimism Foundation/Security Council Safe and 2 more (Mode, Derive) sharing an identical Safe operated by Conduit whose signers recur on Zora's and BOB's own chain-governance Safes too. A second thread into centralized stablecoin issuers (USDC, USDT, PYUSD) found a complete negative: none of the three is controlled by a Gnosis Safe on any tracked chain.

### Caveats (Superchain)

- Point-in-time snapshot across all findings; Safe owner sets, thresholds, and operator-set status can change after this was checked.
- 200 Safes across 166 deployments and 79 protocols is not a finished survey (see What's checked next); a protocol or chain not listed here hasn't been checked, not confirmed clean.
- Several same-signer-set findings above are expected, not new institutional links, when the same team knowingly operates multiple deployments (for example Zora Inc. operating both Zora the protocol and Zora Network the chain, or Frax operating Fraxtal), each such case is labeled inline as "expected" rather than presented as a surprising finding.
- A negative result was also checked and is reported here for completeness: none of the three centralized stablecoin issuers checked (USDC, USDT, PYUSD) is controlled by a Gnosis Safe on any tracked chain.

This is independent research, not commissioned, audited, or endorsed by any protocol, chain, or individual named above. Everything stated is held to the confidence level the on-chain data actually supports.

## License

All rights reserved. This repository documents the results; the tool itself is available under a commercial license, see above.
