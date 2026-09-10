# multisig-overlap

![License](https://img.shields.io/badge/license-all%20rights%20reserved-blue)
![Status](https://img.shields.io/badge/status-active%20research-brightgreen)
![Protocols tracked (Mainnet)](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FRealSpap%2Fmultisig-overlap-showcase%2Fmain%2Fbadge-data-mainnet-protocols.json)
![Protocols tracked (Superchain)](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FRealSpap%2Fmultisig-overlap-showcase%2Fmain%2Fbadge-data-superchain.json)
![Protocols tracked (Part 3)](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FRealSpap%2Fmultisig-overlap-showcase%2Fmain%2Fbadge-data-part3.json)
![Identities found (mainnet)](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FRealSpap%2Fmultisig-overlap-showcase%2Fmain%2Fbadge-data-mainnet.json)
![Follow](https://img.shields.io/badge/follow-%40RealSpap-000000?logo=x)

**The headline risk:** a single compromised key already controls, or is shared across, dozens of nominally independent DeFi protocols spanning Ethereum mainnet and more than 20 other chains.

The same question, checked at three scales. On Ethereum mainnet, 8 named individuals hold multisig signer keys across 2 or more unrelated DeFi protocols at once, two of them (Michael Egorov and c2tp.eth) now tied at 5 protocols each, identified across 132 protocols checked directly on-chain. Extended to Optimism's Superchain, the same pattern recurs 6 more times: one named individual (aavechan.eth), two of the original 8 turning up again on new chains, and two chain-operator entities concentrating upgrade keys across multiple chains at once. A third extension, onto Arbitrum and 10 more L2s and sidechains, finds an already-tracked signer set or Safe address reappearing on 64 of 86 further protocols checked, including c2tp.eth now confirmed on 4 of these 11 chains. Separately, 30+ protocols reuse the identical Gnosis Safe signer set on multiple chains at once, so spreading exposure across a protocol's chain deployments doesn't actually diversify against key compromise.

**Want this method run on your protocol, or a custom research pass? License it: DM [@RealSpap](https://x.com/RealSpap) on X.**

## Contents

- [Methodology at a glance](#methodology-at-a-glance)
- [Who this is for](#who-this-is-for)
- [At a glance](#at-a-glance)
- [Part 1: Mainnet](#part-1-mainnet)
- [Part 2: Superchain](#part-2-superchain)
- [Part 3: Arbitrum and other L2s](#part-3-arbitrum-and-other-l2s)
  - [Arbitrum](#arbitrum)
  - [Polygon](#polygon)
  - [BNB Chain](#bnb-chain)
  - [Avalanche](#avalanche)
  - [zkSync Era](#zksync-era)
  - [Linea](#linea)
  - [Scroll](#scroll)
  - [Berachain](#berachain)
  - [Mantle](#mantle)
  - [Blast](#blast)
  - [Sonic](#sonic)
- [Access to the tool](#access-to-the-tool)
- [Disclaimer](#disclaimer)
- [About](#about)
- [License](#license)

## Methodology at a glance

Every part of this research, across all three scales below, follows the same four-step discipline:

- **Primary-source sourcing.** Every candidate address comes from a protocol's own documentation or GitHub repository first, never a third-party aggregator or press citation.
- **On-chain re-verification.** Every candidate is checked directly on-chain via `getOwners()` (or the equivalent role-specific getter): no API key, no third-party indexer, pure RPC reads against a public node for the relevant chain.
- **Cross-referencing.** Every signer recovered is checked against the full combined roster this research already has on record across all three Parts, not just within the chain or protocol just checked.
- **Falsification and grounding checks.** Every identity or cross-reference claim is logged in a falsifiable-hypothesis registry with an exact source locator, a stated falsification test, and a confidence level, then checked against a mechanical grounding lexical-grounding tool before publication.

Each Part's own Method section below states only what's specific to that Part: how many protocols and chains, and any edge cases this general method doesn't cover.

## Who this is for

Protocol governance teams sizing up their own key concentration against comparable projects. Depositors, insurers, and risk desks pricing counterparty and key-compromise risk across a portfolio of protocols. Auditors and due-diligence teams who need a starting map of shared signers before their own engagement. Teams evaluating whether to license this method for their own protocol or portfolio. Every finding below cites its own primary source so it can be independently re-checked, not taken on faith.

## At a glance

| | Mainnet | Superchain | Part 3 (other L2s) |
|---|---|---|---|
| Protocols checked | 132 | 79 | 86 (12 on Arbitrum, 74 across 10 further chains) |
| Safes checked | 238 signer slots tested, 194 confirmed as real Safe contracts | 200 Safes across 166 deployments | 120 candidate addresses tested, 88 confirmed as real Safe contracts |
| Chains covered | Ethereum mainnet | 13 | 11 (Arbitrum One, Polygon PoS, BNB Chain, Avalanche C-Chain, zkSync Era, Linea, Scroll, Berachain, Mantle, Blast, Sonic) |
| Shared-key findings | 8 named identities holding signer power on 2+ protocols (Michael Egorov and c2tp.eth both now reaching 5 protocols), plus 30 more shared-infrastructure and signer-overlap cases | 6 documented cross-protocol or cross-chain signer-sharing cases, plus 30+ protocols sharing an identical signer set across chains | 64 of 86 protocols extend a signer-set or Safe-address pattern already found in Part 1 or Part 2, including 1 named identity (c2tp.eth, now on 4 of these 11 chains) and several same-address patterns reaching 9 or 10 of these 11 chains at once |
| Research depth | Grew from an original 41-protocol pilot to 132 protocols across 25 research rounds; every finding independently verified on-chain | 31 research passes, still growing | Three passes: an Arbitrum pilot, a same-day pass across 7 more chains, then a follow-up pass across 3 more second-tier chains (Mantle, Blast, Sonic); explicitly not exhaustive on any of the 11 |
| Live verification | Yes, on-chain event replay (covers 69 of the 194 confirmed Safes so far) | Dashboard only; on-chain event replay planned for a future pass | Not built yet |

Every major DeFi protocol discloses its own emergency and governance multisig signers, usually in its own docs. Nobody aggregates that across protocols or chains, so nobody could previously answer: if one person's key, or one shared signer set, were compromised, how many independent protocols or chains would be affected at the same time? This research answers that at three scales: first across 132 major protocols on Ethereum mainnet, then across Optimism's Superchain specifically, where the same protocol is often deployed on a dozen chains at once, then a third time on Arbitrum and 10 more L2s and sidechains deliberately outside the Superchain family.

## Access to the tool

The verification method behind this research is available under a commercial license, not published in this repository. The findings below were produced with it and are independently reproducible by anyone with the same access; this repo documents the results, not the mechanism. Reach out via [RealSpap on X](https://x.com/RealSpap) for licensing.

## Disclaimer

This report presents an independent, factual analysis of publicly available on-chain data (smart contract code, multisig signer sets, governance transactions) as of the date noted in the Status/Method sections below. Statements about which addresses or individuals hold administrative, multisig, or governance keys are based solely on on-chain records and publicly disclosed information cited inline; they are not allegations of wrongdoing, and no claim of illegal conduct, fraud, or misconduct is made or implied. Concentration of control or key-holder identity is reported as an observed structural fact, not as a moral or legal judgment on the individuals named. Findings reflect a snapshot in time; on-chain configurations, signer sets, and governance parameters can and do change after publication, and this report is not updated automatically to reflect such changes. This is independent research, not commissioned or audited by any protocol discussed, and it does not constitute legal, financial, or investment advice. Any individual or entity named in this report who believes information about them is inaccurate or outdated is invited to contact the author via [X](https://x.com/RealSpap) with supporting evidence; corrections will be issued promptly and transparently. Readers should independently verify all cited addresses, transactions, and figures before relying on them.

## Part 1: Mainnet

### Method

132 protocols' multisig contracts (Gnosis Safe) checked directly on-chain (see [Methodology at a glance](#methodology-at-a-glance) above): 238 signer slots tested, 194 confirmed as real Safe contracts. Scope grew from an original 41-protocol pilot to 132 protocols across 25 research rounds, each adding several more protocols and re-running the full cross-reference against every signer already on record.

### Findings

8 addresses hold signer power on 2+ independent protocols, sorted by how many protocols each one touches. All 8 are identified by name or known pseudonym, each backed by a primary-source citation:

| Rank | Identity | Protocols | Reach | Role |
|---|---|---|---|---|
| 1 | **Michael Egorov** | Abracadabra + Yearn + Prisma + Threshold Network + Usual Money | 5 protocols | Founder of Curve Finance |
| 1 | **c2tp.eth** | Convex (his own protocol) + Prisma + Votium + Curve Finance's own Emergency DAO + Resupply | 5 protocols | Pseudonymous creator of Convex Finance |
| 3 | **Ernesto Boado** (BGD Labs) | Lido + Balancer | 2 protocols | Infrastructure/security provider working with multiple protocols |
| 3 | **Pablo Veyrat** | Angle (his own protocol) + Morpho | 2 protocols | Founder of Angle Protocol |
| 3 | **Julien Bouteloup** | Abracadabra + StakeDAO (his own protocol) | 2 protocols | Founder of StakeDAO / Rekt News, early Curve team |
| 3 | **"Tommy"** | Votium (his own protocol) + Convex | 2 protocols | Known representative of Votium |
| 3 | **Sam Kazemian** (high confidence, not independently name-confirmed) | Frax (his own protocol) + Prisma | 2 protocols | Founder of Frax Finance |
| 3 | **Matthew Graham** | Gearbox + TokenLogic (his own service) | 2 protocols | Founder of TokenLogic |

*What this means in practice: Egorov's and c2tp.eth's keys now each touch 5 independent protocols at once, tied for the widest documented mainnet reach of any named individual in this research. A single compromised key for either one puts several unrelated protocols' funds at risk simultaneously, not one.*

Three of the eight (Egorov, c2tp, Kazemian) sit together on Prisma Finance's emergency multisig, a deliberate, publicly disclosed design choice by Prisma to recruit established protocol founders for credibility, not a hidden concentration. The other five are more organic: independent protocols with no obvious institutional link to each other.

Matthew Graham and TokenLogic reappear in Part 2 below: the same footprint that starts here on Gearbox and TokenLogic's own Ethereum Safe extends onto three of Aave's Superchain Safes as well, the widest documented footprint of any named individual across this entire research (3 protocols, 3 chains, 5 Safes).

Four of the eight named identities gained a further protocol seat along the way, not shown as separate rows in the case table below since each extends an identity already in the table above rather than introducing a new one: Michael Egorov's seats on Threshold Network and Usual Money (his 4th and 5th protocols), and c2tp.eth's seats on Curve Finance's own Emergency DAO (his 4th protocol) and on Resupply, a protocol co-built by Convex and Yearn (his 5th protocol, tying Egorov's reach).

Beyond the 8 named identities and their extensions, this research has surfaced 26 more shared-infrastructure or signer-overlap cases on mainnet, each a Safe or signer set already tracked elsewhere in this research turning up again, or a new pseudonymous overlap found entirely within mainnet itself:

| Protocol (Mainnet) | What was found | Already tracked as |
|---|---|---|
| **EigenLayer** | Pauser, Community, Executor, and Operations multisigs are the identical Safes already used by Aave under those same roles, at 4 different addresses (7, 13, 2, and 6 owners). No public source explains why | Aave's own Safes (mainnet) |
| **Silo Finance** | Mainnet SiloFactory owner is the identical Safe already tracked on Optimism, Base, and Ink; the mainnet 3-of-4 set is a subset of the 5 owners on those chains | Part 2 |
| **1inch** | Aggregation Router V6 owner on mainnet is the identical 5-signer set already tracked on Optimism, Base, and Unichain | Part 2 |
| **ether.fi** | Mainnet Controller Safe shares 4 of its 7 signers with the Controller Safe set already tracked on Base, Ink, Mode, Optimism, and Unichain: a partial rather than full match | Part 2 (partial) |
| **Aura Finance / Balancer** | One signer of Aura's sudo multisig also sits on Balancer's DAO multisig. Aura is built directly on Balancer's veBAL system, an institutionally expected link | Balancer's own Safe (mainnet) |
| **Aura Finance / Abracadabra** | A different signer of Aura's sudo multisig also sits on Abracadabra Money's multisig, with no obvious institutional link between the two | New pseudonymous link (mainnet) |
| **API3** | Manager multisig, already the identical Safe on 7 Superchain chains, resolves identically on Ethereum mainnet too: an 8th chain, tying Curve's Emergency DAO for the widest same-address propagation in the dataset | Part 2 |
| **Odos** | Router V3 owner on mainnet is the literal same Safe address already tracked on Optimism, Base, and Unichain | Part 2 |
| **deBridge** | Mainnet admin Safe shares the identical 8-owner set already tracked on Optimism and Base | Part 2 |
| **ParaSwap / Velora** | Mainnet AugustusSwapper admin is a 12-owner Safe identical to the set already tracked on Base and Optimism | Part 2 |
| **Beefy Finance** | Mainnet devMultisig is the identical 6-owner Safe already shared across six Superchain chains; a separate treasuryMultisig is a genuine, unshared 7-signer Safe | Part 2 |
| **Hyperlane** | Mainnet Mailbox and ProxyAdmin owner is the identical 10-owner Safe already tracked on Optimism and Base | Part 2 |
| **Renzo Protocol** | Mainnet admin Safe shares the identical 6-owner set already tracked on Ink, and is a strict superset of the 5 owners shared by Optimism, Base, Mode, Unichain, and World Chain | Part 2 |
| **Chainlink Data Feeds** | Mainnet ETH/USD price feed owner shares the identical 9-owner set already tracked on 4 Superchain chains and on Arbitrum | Part 2 + Part 3 |
| **Kelp DAO / Stader Labs** | One signer of Kelp DAO's mainnet manager Safe also sits on Stader Labs' Optimism Safe. Kelp DAO and Stader Labs share founders, an institutionally expected link | Part 2 |
| **Superfluid** | Mainnet protocol-governance Safe is the identical Safe already tracked on Optimism, Base, and Celo | Part 2 |
| **Term Finance** | Mainnet admin and devops Safes are the identical contract addresses already tracked on Base | Part 2 |
| **Compound / Resolv** | The same pseudonymous signer already linking Compound III's Base Pause Guardian to Resolv's Base and Soneium Safes also sits on both Compound's own mainnet pauseGuardian and Resolv's mainnet Token Owner Safe: the first direct mainnet-to-mainnet overlap found within Part 1 itself | Part 2 |
| **AladdinDAO / f(x) Protocol** | f(x) Protocol's governance Safe shares its full 9-signer set with AladdinDAO's own Concentrator Treasury Safe. AladdinDAO is the team that built f(x) Protocol, an institutionally expected link | AladdinDAO's own Safe (mainnet) |
| **Hop Protocol** | Mainnet Community multisig shares the identical 5-owner set already tracked on Optimism, at a different Safe address per chain | Part 2 |
| **Venus Protocol** | Mainnet Guardian shares the identical 7-owner set already tracked on Base and Unichain, and the same group already tracked on BNB Chain and zkSync Era | Part 2 + Part 3 |
| **Flux Finance / Ondo** | One of Flux Finance's 5 pauseGuardian signers also sits on Ondo Finance's own Management Multisig. Flux Finance is governed by the Ondo DAO, an institutionally expected link | Ondo Finance's own Safe (mainnet) |
| **Stader Labs / Kelp DAO, Treasury-to-Treasury** | 3 of Stader Labs' 5 Treasury signers are the same 3 addresses as 3 of Kelp DAO's 4 ProtocolTreasury signers: a majority overlap, a much stronger version of the single-signer link already on record between the same two protocols above | Strengthens the Kelp DAO / Stader Labs case above (mainnet) |
| **Gravita Protocol / Puffer Finance** | One signer of Gravita's adminContract Safe also sits on two of Puffer Finance's own Safes (Community and Pauser multisigs). No disclosed institutional relationship found | New pseudonymous link (mainnet) |
| **Inverse Finance / Yearn** | One signer of Inverse Finance's Risk Working Group Safe also sits on Yearn's own ychad multisig. No disclosed institutional relationship found | New pseudonymous link (mainnet) |
| **WBTC / Aura Finance** | One signer of WBTC's Controller multisig also sits on Aura Finance's own sudo multisig, already on record since an earlier pass. Independently confirmed by live ENS resolution as `solarcurve.eth`, the first identity in this registry resolved this way rather than from a documentation citation | New pseudonymous link, ENS-confirmed (mainnet) |

None of these 26 cases turns up a new named individual beyond the four identity extensions above; the pseudonymous signers in the Aura, Kelp DAO/Stader Labs, Compound/Resolv, Gravita/Puffer, Inverse/Yearn, and WBTC/Aura rows could not be tied to a real name from a primary source strong enough to publish under this research's own naming bar, so they're reported at address level only, except WBTC/Aura's, independently confirmed via live ENS resolution.

### Live verification

[dune.com/s_pap/multisig-overlap](https://dune.com/s_pap/multisig-overlap): a self-computing query that skips the point-in-time snapshot entirely and replays the actual on-chain event history of all 69 Safe contracts tracked as of the query's own last update, recomputing current ownership fresh every time it runs. This hasn't yet been extended to the protocols added across two dozen subsequent research rounds, so those newer findings above are confirmed by direct on-chain reads at a point in time, not yet by event replay.

**Get notified**, no account needed on this repo: click Watch, then Custom, then Releases only, on this repo's GitHub page for a per-pass update feed. On Dune, star the dashboard to keep it in your own list, or set a scheduled alert on the query for a ping the moment a tracked Safe's owner set actually changes on-chain, not just when this repo gets updated.

The live query relies on parsing on-chain event history rather than static contract reads. Some older Safes were created before their deployment transaction logged the data a pure event-based rebuild needs, so 2 of the 8 identities (Julien Bouteloup's second seat and c2tp.eth's Convex seat) are instead confirmed by a direct `getOwners()` read, independently cross-checked by manually reading the relevant transaction logs on Etherscan.

### Open data (Mainnet)

The live query's own result table is queryable directly through [Dune's Query API](https://docs.dune.com/api-reference/api-overview) by anyone with a free Dune API key, no scraping needed: pull the same 8 identities the same way this page does, recomputed fresh on every call.

### What's checked next (Mainnet)

132 protocols is a growing survey, not a finished one. Open a GitHub Issue on this repo to suggest the next protocol to check; a thumbs-up on an existing suggestion counts as a vote (this sets research priority only; checks are still run under the same licensed method, not opened to contributors). The Superchain-specific follow-up already covers 79 more protocols, and a third extension covers 86 more across Arbitrum and 10 other L2s and sidechains: see Part 2 and Part 3 below.

### Verification

Every claim in this research follows the same verification discipline described in [Methodology at a glance](#methodology-at-a-glance) above. The mainnet registry holds 39 rows: the 8 identities, 1 correction (see Caveats below), and 30 shared-infrastructure or signer-overlap cases; 38 rows at High confidence and 1 (Sam Kazemian's link to Frax, role-inference rather than a direct name-to-address citation) at Medium confidence.

### Status

Last verified: 2026-09-10.

132 protocols checked (238 signer slots tested, 194 confirmed as real Safe contracts), not a finished survey. Scope has grown from an original 41-protocol pilot across 25 research rounds, each one adding new protocols, resolving a previously parked case, or re-running the full cross-reference against every signer already on record.

### Caveats (Mainnet)

- One of the 8 identities (Julien Bouteloup's second seat) and one seat behind another (c2tp.eth's Convex seat) don't reproduce through live event replay, because they sit on Safe versions old enough that their creation transactions don't log the data a pure event-based rebuild needs; both are confirmed by a direct `getOwners()` read instead. See Live verification above.
- 132 protocols is a growing survey, not a finished one (see What's checked next). A protocol not listed here hasn't been checked, not confirmed clean.
- Three of the eight identified signers (Egorov, c2tp, Kazemian) sit together on Prisma Finance's multisig by Prisma's own deliberate, publicly disclosed design choice to recruit established founders for credibility, not a hidden concentration; treating that case the same as the other five would overstate how coordinated the overlap actually is.
- One candidate address needed a correction from a sibling project in this research program. Ethena's `Owner_Multisig_3of11` is a real, confirmed 10-signer Safe, but an independent check in a sibling research project found it does not match the actual `owner()` of either EthenaMinting V2 or the USDe token (both a 24-hour Timelock instead), nor EthenaMinting V1's actual owner (a separate 5-of-10 Safe). The Safe is real; what it currently controls at Ethena, if anything, is unconfirmed.

## Part 2: Superchain

Extension of Part 1 to Optimism's Superchain (OP Mainnet, Base, Mode, Unichain, Ink, Soneium, Lisk, Celo, Zora Network, World Chain, Fraxtal, Derive Chain, and BOB so far). Part 1 asks "does the same person hold emergency keys on multiple, unrelated protocols at once?" This part asks a Superchain-specific variant: "does the same signer set control a protocol's admin multisig on multiple chains at once, and does anyone share keys across genuinely different Superchain protocols?"

### Method

200 Gnosis Safe multisig contracts across 166 protocol/chain deployments, checked directly on-chain (see [Methodology at a glance](#methodology-at-a-glance) above). This also covers who controls the 13 tracked chains themselves at the L1 (Ethereum mainnet) level, not just the dapps deployed on them: a real Gnosis Safe was confirmed as the ProxyAdminOwner on all 13, with World Chain's separate SystemConfigOwner the sole exception, a bare EOA rather than a Safe.

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

1. `0x8f02b4a44Eacd9b8eE7739aa0BA58833DD45d002` is an owner of both Morpho Blue's governance Safe (**Base, World Chain, and Fraxtal**) and Angle Protocol's Guardian Safe (**Optimism, Base, and Celo**), six separate Safe deployments in total. Morpho and Angle have no institutional relationship. The same address also sits on both protocols' Ethereum mainnet Safes (already on record in Part 1 for Angle), so a single compromised key here threatens Morpho and Angle simultaneously, across mainnet and six Superchain deployments. It's identified with **high confidence as Pablo Veyrat, co-founder of Angle Protocol and Merkl**, named explicitly with this exact address by Morpho Association's own governance forum post proposing him as a multisig signer.
   *What this means in practice: a depositor treating Morpho Blue and Angle as independent risk exposures is wrong. One compromised key ends both at once, on six chains simultaneously.*

2. **Matthew Graham / TokenLogic**, already named in Part 1 as an owner of both Gearbox's Technical Multisig and TokenLogic's own Safe on Ethereum, is now also confirmed as an owner of three of Aave's role-specific Safes (Merkl rewards distribution, a "Robot Guardian" automation role, and TokenLogic's own execution Safe), deployed at the identical addresses on both Ink and Celo. A second TokenLogic team member from that same Ethereum Safe is confirmed alongside him on both chains. This is the widest documented footprint of any named individual across this research: three protocols, three chains, five Safes.
   *What this means in practice: this is the single widest blast radius identified across this research. A key held by one small team now touches Gearbox, TokenLogic, and Aave at once.*

3. **aavechan.eth**, an ENS-verified, Basescan-labeled Aave ecosystem operator, is confirmed as an owner of both QiDao/Mai Finance's Base and Fraxtal Guardian Safes and Aave's Celo "Masiv" Safe: three separate Safe deployments across two independently-run protocols with no institutional relationship, caught by the script's own cross-reference logic rather than assumed.
   *What this means in practice: an independent Aave-ecosystem operator, not Aave itself, also holds a guardian key on an unrelated lending protocol.*

4. `0x9A73D57BB1fB280C5672A13f655675De25F13b70` is an owner of both Compound III's Base Pause Guardian Safe and Resolv's Base and Soneium Token Owner Safes. Compound III and Resolv have no institutional relationship. Found by the same cross-reference logic once Resolv's Safes were added to the registry, not assumed in advance.
   *What this means in practice: a pause-guardian key for one blue-chip lending protocol doubles as a token-owner key for an unrelated stablecoin issuer.*

5. **5 of the 13 tracked chains (Optimism, Mode, Ink, Soneium, Zora) delegate their entire L1 chain-governance authority, the ProxyAdminOwner role able to upgrade nearly any part of that chain's L1 bridge/rollup contracts, to the identical Gnosis Safe**: a nested 2-of-2 between the Optimism Foundation and the Security Council. Unichain's own separate Safe shares 2 of its 3 signers with that same pair. This isn't one protocol deployed six times: these are six independently branded chains, several run day-to-day by entirely separate companies, that have each chosen to hand core upgrade rights to the same small, centrally Optimism-Foundation-operated group.
   *What this means in practice: this is the single largest concentration in the dataset. One Safe's signers can upgrade the core L1 contracts of 6 of the 13 chains this project tracks.*

6. **Conduit**, the Rollup-as-a-Service operator behind Mode and Derive Chain, controls both chains' core chain-governance role through the identical Safe. Four of that Safe's 11 signers individually also sit on Zora Network's and/or BOB's own separate chain-governance Safes: the same infrastructure-provider personnel holding upgrade rights across at least four nominally independent chains at once.
   *What this means in practice: several chains presented to users as independently operated share upgrade-key personnel with a common infrastructure vendor, not just with each other.*

Separately, one more pseudonymous signer (`0xb291232F480F41c75802C4a60F1D2AC03404Afef`) shows up on Aave's core Protocol Guardian Safe on Optimism, Base, Soneium, and Celo, and also on a distinct 3-person cluster controlling four of Aave's Ink and Celo Safes: a single Aave ecosystem operator trusted with keys across at least six separate Safe formations.

Beyond those cases, the sample also confirms a **Superchain-specific pattern**: several protocols run the exact same signer set across multiple chains at once.

| Protocol | What was found |
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

**Get notified of new passes**, no account needed on this repo: click Watch, then Custom, then Releases only, on this repo's GitHub page. Every research pass gets tagged as a release, title and body taken straight from that pass's own commit message. On Dune, star the dashboard to have it in your own list, or set a scheduled alert on the query for a ping when a tracked Safe's owner set changes.

### Open data (Superchain)

The dashboard's own table above is queryable directly through [Dune's Query API](https://docs.dune.com/api-reference/api-overview) by anyone with a free Dune API key, no scraping needed.

### What's checked next (Superchain)

Not a finished survey by design (see Status below). Open a GitHub Issue on this repo to suggest the next protocol or chain to check; a thumbs-up on an existing suggestion counts as a vote (this sets research priority only; checks are still run under the same licensed method, not opened to contributors).

### Verification

Every claim in this research follows the same verification discipline described in [Methodology at a glance](#methodology-at-a-glance) above. On the Superchain side, 92 of 92 hypotheses currently in the registry pass clean at High confidence.

### Status

Last verified: 2026-09-09.

200 Safes across 166 deployments and 79 protocols, not a finished survey. The most recent pass turned to who controls the 13 tracked chains themselves rather than the dapps on them: a real Gnosis Safe confirmed as ProxyAdminOwner on all 13, 5 of them sharing the identical Optimism Foundation/Security Council Safe and 2 more (Mode, Derive) sharing an identical Safe operated by Conduit whose signers recur on Zora's and BOB's own chain-governance Safes too. A second thread into centralized stablecoin issuers (USDC, USDT, PYUSD) found a complete negative: none of the three is controlled by a Gnosis Safe on any tracked chain.

### Caveats (Superchain)

- Point-in-time snapshot across all findings; Safe owner sets, thresholds, and operator-set status can change after this was checked.
- 200 Safes across 166 deployments and 79 protocols is not a finished survey (see What's checked next); a protocol or chain not listed here hasn't been checked, not confirmed clean.
- Several same-signer-set findings above are expected, not new institutional links, when the same team knowingly operates multiple deployments (for example Zora Inc. operating both Zora the protocol and Zora Network the chain, or Frax operating Fraxtal), each such case is labeled inline as "expected" rather than presented as a surprising finding.
- A negative result was also checked and is reported here for completeness: none of the three centralized stablecoin issuers checked (USDC, USDT, PYUSD) is controlled by a Gnosis Safe on any tracked chain.

This is independent research, not commissioned, audited, or endorsed by any protocol, chain, or individual named above. Everything stated is held to the confidence level the on-chain data actually supports.

## Part 3: Arbitrum and other L2s

An extension of the same method beyond the Superchain family covered in Part 2, onto major L2s and sidechains that each run their own separate architecture and governance: Arbitrum (Nitro, the Arbitrum DAO and Security Council) first, as a pilot pass, then seven more chains chosen for real TVL and a real governance or emergency multisig (Polygon PoS, BNB Chain, Avalanche C-Chain, zkSync Era, Linea, Scroll, and Berachain), then a follow-up pass across three more explicitly second-tier chains (Mantle, Blast, and Sonic). Parts 1 and 2 both ask whether the same signer or Safe holds trusted power across multiple unrelated protocols or chains at once; this part asks the identical question a third time, on a third terrain, and every signer recovered here is cross-referenced against the full combined roster of Part 1 and Part 2, not just one or the other.

### Method

120 candidate addresses tested across the 11 chains (see [Methodology at a glance](#methodology-at-a-glance) above): 88 resolved to confirmed Gnosis Safe contracts. Several sources publish a factory, provider, or router contract rather than the multisig directly, so the actual Safe address was obtained by calling `owner()` or a role-specific getter on that contract first, then re-verified with its own `getOwners()` call. Each chain's own internal cross-check (does any signer repeat across two different protocols on that one chain) comes back clean on all 11; the signal is entirely cross-part and cross-chain.

### Findings

64 of the 86 protocols checked across Part 3 turn out to extend a pattern this research had already documented elsewhere, sometimes at the literal same Safe address and sometimes at a different address with an identical or overlapping signer list, including 1 named identity (c2tp.eth, via Curve Finance's Emergency DAO Safe, now confirmed on 4 of these 11 chains) and several same-address, same-owner patterns now reaching 9 or 10 of these 11 chains at once (Aave's GOVERNANCE_GUARDIAN on 9, Beefy Finance's dev/treasury multisigs on 10, API3's manager multisig on 10). 22 protocols across the sample show no overlap with the existing roster at all, split between real new Safes (GMX and Camelot on Arbitrum; Merchant Moe, INIT Capital, Shadow Exchange, SwapX, Kodiak Finance, ZeroLend, and Berachain's own Proof-of-Liquidity core on the newer chains) and no usable Safe recovered at all (Dolomite and Pendle Finance on Arbitrum; Pendle Finance, Silo Finance, Lendle, Agni Finance, ZeroLend, Overnight Finance's AgentTimelock, Mangrove, and 1inch on Mantle/Blast, a low-TVL-chain pattern largely absent from the first 8 chains checked).

#### Arbitrum

A first pilot pass, deliberately mixing protocols never touched by this research before (GMX, Camelot, Dolomite) with protocols already tracked elsewhere (Aave, Compound III, Curve Finance, 1inch, Silo Finance, Beefy Finance, Chainlink, Pendle Finance, and Radiant Capital). 20 candidate addresses were tested; 13 resolved to confirmed Gnosis Safe contracts, recovering 87 signer slots (83 unique addresses). No signer or Safe was shared between two different protocols within the Arbitrum sample itself; 8 of the 12 Arbitrum protocols checked extend a pattern already documented on other chains.

| Protocol | What was found | Already tracked as |
|---|---|---|
| **Compound III**, pauseGuardian | Identical 9-owner set as Compound's own Ethereum mainnet pauseGuardian and Compound III's Base Pause Guardian. One of the 9 is the same pseudonymous signer already linking Compound III's Base Pause Guardian to Resolv | Part 1 + Part 2 |
| **Curve Finance**, Emergency DAO | Deployed at the literal same Safe contract address already used on Ethereum mainnet and the 6 Superchain chains this research tracks. One of the 9 owners is c2tp.eth, already named for Convex, Prisma, Votium, and Curve's own mainnet Emergency DAO Safe: an institutionally expected link given Convex is built directly on Curve | Part 1 + Part 2 |
| **Aave V3**, GOVERNANCE_GUARDIAN | Identical 9-owner set as Aave V3's own governance-guardian Safe on BOB, at a different Safe address | Part 2 |
| **1inch**, Aggregation Router V6 owner | Identical 5-owner set already shared, at one single literal address, across mainnet, Optimism, Base, and Unichain. Arbitrum is the first of these deployments to use a distinct Safe address for the same 5 people | Part 1 + Part 2 |
| **Silo Finance**, SiloFactory owner | 4 owners, identical to that same Safe's own mainnet owner set, and a complete subset of its 5-owner (Optimism, Base) and 6-owner (Ink) versions | Part 1 + Part 2 |
| **Beefy Finance**, devMultisig | Identical 6-owner set already shared across 6 Superchain chains; Arbitrum is a 7th | Part 2 |
| **Chainlink Data Feeds**, ETH/USD feed owner | Identical 9-owner set already tracked on 4 Superchain chains; Arbitrum is a 5th | Part 2 |
| **Radiant Capital**, EmergencyAdmin | 5 owners, a complete subset of the 8-owner Dao Treasury Safe already tracked for Radiant Capital on Base: same protocol, different role and chain, partial signer reuse rather than a full match | Part 2 |

Four protocols showed no overlap with the existing combined roster at all: **GMX** (2 confirmed Safes, 7 and 8 signers), **Camelot** (2 confirmed Safes, 3 and 6 signers), **Dolomite**, and **Pendle Finance** (both confirmed real admin contracts, but not classic Gnosis Safes).

#### Polygon

| Protocol | What was found | Already tracked as |
|---|---|---|
| Aave V3, GOVERNANCE_GUARDIAN | Identical 9-owner set, same literal Safe address as Arbitrum, BNB Chain, and Scroll | Part 2 + Part 3 |
| Curve Finance, Emergency DAO | Same literal Safe address as mainnet, 6 Superchain chains, and Arbitrum; identical 9 owners including c2tp.eth | Part 1 + Part 2 + Part 3 |
| Compound III, pauseGuardian | Identical 9-owner set as mainnet's and Arbitrum's pauseGuardian, including the signer already linked to Resolv | Part 1 + Part 3 |
| 1inch, Router V6 owner | Identical 5-owner set already shared across mainnet, Optimism, Base, Unichain, and Arbitrum | Part 1 + Part 2 + Part 3 |
| Chainlink Data Feeds, ETH/USD owner | Identical 9-owner set already tracked on 4 Superchain chains and Arbitrum | Part 2 + Part 3 |
| Beefy Finance, dev + treasury multisig | Identical 6 and 7-owner sets already shared on mainnet, 6 Superchain chains, and Arbitrum | Part 1 + Part 2 + Part 3 |
| API3, manager multisig | Same literal address, identical 8 owners, already the widest same-address spread in the dataset | Part 1 + Part 2 + Part 3 |
| CoW Protocol, admin Safe | Same literal address and identical 9 owners already tracked on Optimism and Ink | Part 2 |

#### BNB Chain

| Protocol | What was found | Already tracked as |
|---|---|---|
| Aave V3, GOVERNANCE_GUARDIAN | Identical 9-owner set, same literal Safe address as Polygon, Scroll, and Arbitrum | Part 2 + Part 3 |
| Curve Finance, Emergency DAO | Same literal Safe address as every other chain this research tracks it on | Part 1 + Part 2 + Part 3 |
| Silo Finance, SiloFactory owner | Same literal Safe address as mainnet, Optimism, Base, Ink, and Arbitrum; identical 4 owners | Part 1 + Part 2 + Part 3 |
| 1inch, Router V6 owner | Identical 5-owner set already shared everywhere else in this research | Part 1 + Part 2 + Part 3 |
| Chainlink Data Feeds, ETH/USD owner | Identical 9-owner set already tracked elsewhere in this research | Part 2 + Part 3 |
| Beefy Finance, dev + treasury multisig | Identical sets already shared elsewhere; BNB Chain is Beefy's own founding chain | Part 1 + Part 2 + Part 3 |
| API3, manager multisig | Same literal address, identical 8 owners | Part 1 + Part 2 + Part 3 |
| CoW Protocol, admin Safe | Same literal address as Optimism, Ink, and Polygon; identical 9 owners | Part 2 |
| Radiant Capital, PoolAdmin | 7 of 11 owners match Radiant's own 8-owner Dao Treasury Safe on Base, plus 4 new signers | Part 2 |
| Radiant Capital, EmergencyAdmin | Identical 5-owner set already tracked as Radiant's EmergencyAdmin on Arbitrum | Part 2 + Part 3 |
| Venus Protocol, Guardian (3 Safes, same set) | Identical 7-owner set already tracked as Venus's Guardian multisig on Base and Unichain | Part 2 |

#### Avalanche

| Protocol | What was found | Already tracked as |
|---|---|---|
| Aave V3, GOVERNANCE_GUARDIAN | Identical 9-owner set, an Avalanche-specific Safe address | Part 2 + Part 3 |
| Curve Finance, Emergency DAO | Same literal Safe address as every other chain this research tracks it on | Part 1 + Part 2 + Part 3 |
| Silo Finance, SiloFactory owner | Same literal Safe address as mainnet, Optimism, Base, Ink, Arbitrum, and BNB Chain | Part 1 + Part 2 + Part 3 |
| 1inch, Router V6 owner | Identical 5-owner set already shared everywhere else in this research | Part 1 + Part 2 + Part 3 |
| Chainlink Data Feeds, ETH/USD owner | Identical 9-owner set already tracked elsewhere in this research | Part 2 + Part 3 |
| Beefy Finance, dev + treasury multisig | Identical sets already shared elsewhere; one of Beefy's earliest-supported chains | Part 1 + Part 2 + Part 3 |
| API3, manager multisig | Same literal address, identical 8 owners | Part 1 + Part 2 + Part 3 |
| CoW Protocol, admin Safe | Same literal address as Optimism, Ink, Polygon, and BNB Chain | Part 2 |

#### zkSync Era

| Protocol | What was found | Already tracked as |
|---|---|---|
| Aave V3, GOVERNANCE_GUARDIAN | Identical 9-owner set, a zkSync-specific Safe address | Part 2 + Part 3 |
| Chainlink Data Feeds, ETH/USD owner | Identical 9-owner set already tracked elsewhere in this research | Part 2 + Part 3 |
| Beefy Finance, dev + treasury multisig | Identical sets already shared elsewhere | Part 1 + Part 2 + Part 3 |
| API3, manager multisig | Same literal address; only 6 of 8 owners match, a partial rather than a full set, the only chain in this batch where that is true | Part 1 + Part 2 + Part 3 (partial) |
| Venus Protocol, Guardian | Identical 7-owner set already tracked as Venus's Guardian multisig on Base and Unichain | Part 2 |

#### Linea

| Protocol | What was found | Already tracked as |
|---|---|---|
| Aave V3, GOVERNANCE_GUARDIAN | Identical 9-owner set, a Linea-specific Safe address | Part 2 + Part 3 |
| Compound III, pauseGuardian | Identical 9-owner set as mainnet's, Arbitrum's, and Polygon's pauseGuardian | Part 1 + Part 3 |
| 1inch, Router V6 owner | Identical 5-owner set already shared everywhere else in this research | Part 1 + Part 2 + Part 3 |
| Chainlink Data Feeds, ETH/USD owner | Identical 9-owner set already tracked elsewhere in this research | Part 2 + Part 3 |
| Beefy Finance, dev + treasury multisig | Identical sets already shared elsewhere | Part 1 + Part 2 + Part 3 |
| API3, manager multisig | Same literal address, identical 8 owners | Part 1 + Part 2 + Part 3 |

#### Scroll

| Protocol | What was found | Already tracked as |
|---|---|---|
| Aave V3, GOVERNANCE_GUARDIAN | Identical 9-owner set, same literal Safe address as Polygon, BNB Chain, and Arbitrum | Part 2 + Part 3 |
| Compound III, pauseGuardian | Identical 9-owner set as mainnet's, Arbitrum's, Polygon's, and Linea's pauseGuardian | Part 1 + Part 3 |
| Chainlink Data Feeds, ETH/USD owner | Identical 9-owner set already tracked elsewhere in this research | Part 2 + Part 3 |
| Beefy Finance, dev + treasury multisig | Identical sets already shared elsewhere | Part 1 + Part 2 + Part 3 |
| API3, manager multisig | Same literal address, identical 8 owners | Part 1 + Part 2 + Part 3 |

#### Berachain

Berachain (mainnet 2025) is young enough that most of the multi-chain registries this research relies on elsewhere don't cover it yet, so sourcing here leans more on direct on-chain confirmation than a published deployment file.

| Protocol | What was found | Already tracked as |
|---|---|---|
| Beefy Finance, dev + treasury multisig | Identical sets already shared across every other chain checked in this batch | Part 1 + Part 2 + Part 3 |
| API3, manager multisig | Same literal address, identical 8 owners, even though API3's own public deployment registry does not (yet) list a Berachain deployment | Part 1 + Part 2 + Part 3 |

Two new real Safes never seen before in this research were also confirmed on Berachain with no overlap onto the existing roster: **Kodiak Finance** (its own UniswapV3Factory owner, a real 5-owner Safe) and **Berachain's own Proof-of-Liquidity core** (the Safe that assigns BGT emission weights to reward vaults). Two more Berachain-native contracts checked the same way are real contracts but access-controlled by role rather than by a single owner, so no candidate Safe could be recovered for either, a negative result worth recording rather than a gap.

#### Mantle

Mantle, Blast, and Sonic were deliberately chosen as second-tier chains, unlike the first 7: real DeFi TVL is thinner and less stable on all three. Mantle (about $95M chain-level TVL at research time) produced a respectable haul of real, disclosed multisigs.

| Protocol | What was found | Already tracked as |
|---|---|---|
| Aave V3, GOVERNANCE_GUARDIAN | Identical 9-owner set, a Mantle-specific Safe address; also confirmed identical on Sonic the same day | Part 2 + Part 3 |
| Compound III, pauseGuardian | Identical 9-owner set as mainnet's, Arbitrum's, Polygon's, Linea's, and Scroll's pauseGuardian | Part 1 + Part 3 |
| Beefy Finance, dev + treasury multisig | Different Safe addresses than every other chain this research tracks Beefy on, but byte-for-byte identical 6 and 7-owner sets to the ones already confirmed on Berachain and Sonic: same underlying people, different Safe | Part 1 + Part 2 + Part 3 |
| API3, manager multisig | Same literal address, identical 8 owners | Part 1 + Part 2 + Part 3 |

Two new real Safes never seen before in this research were also confirmed on Mantle with no overlap onto the existing roster: **Merchant Moe** (its Liquidity Book and legacy factories share one 5-owner Safe owner) and **INIT Capital** (its AccessControlManager owner, 7 signers). Several other candidates produced no usable Safe: a real contract whose admin-recovery call reverts outright (Pendle Finance's governanceProxy, Lendle's PoolAddressesProvider owner), a resolved address with no deployed bytecode at all, meaning a single externally-owned key rather than a multisig controls the role (Silo Finance's SiloFactory owner, despite Silo using a real Safe for this exact role on every other chain this research tracks it on; Agni Finance's factory owner and Lendle's separate emergency-admin address), and a chain-invariant address that third-party listings claim is deployed but which carries no bytecode at all on this specific chain (1inch's Aggregation Router V6, genuinely absent on Mantle though real and Safe-owned on Sonic).

#### Blast

This is this batch's honest weak result, reported as such rather than padded to match Mantle and Sonic. Of the 6 protocols tested on Blast, only 2 resolved to a real, confirmed Safe, a 2-of-6 hit rate against Mantle's 6-of-11 and Sonic's 7-of-9. This tracks the underlying ecosystem, not a gap in the search: Blast's entire chain-level TVL sat around $31.5M at research time, with no single protocol above $10M. Two of Blast's better-TVL protocols compounded the problem directly: their own documentation sites had gone unreachable by the time of this pass, so Blast's single largest DEX by TVL could not be sourced to this research's primary-source standard at all and was dropped rather than sourced secondhand.

| Protocol | What was found | Already tracked as |
|---|---|---|
| API3, manager multisig | Same literal address, identical 8 owners, even though API3's own public deployment registry does not (yet) list a Blast deployment | Part 1 + Part 2 + Part 3 |
| Overnight Finance, OvnAgent | Identical 5-owner set already tracked as Overnight Finance's OvnAgent on Optimism and Base; Overnight Finance was already inside this research's roster and only recognized as such at the cross-reference step here | Part 2 |

The other 4 protocols tested on Blast produced no usable Safe: two real contracts (ZeroLend's and Overnight Finance's own separate Blast Timelock-style contracts, distinct from the OvnAgent Safe above) whose admin-recovery calls revert outright, one candidate address with no deployed bytecode at all (a genuine negative rather than a gap), and Mangrove's own core contract, whose docs mark the Blast deployment "deprecated."

#### Sonic

Sonic (formerly Fantom, migrated to a new token and rebranded) produced a more fragmented but still-active haul, about $16 to 30M in TVL spread across a longer tail of protocols.

| Protocol | What was found | Already tracked as |
|---|---|---|
| Aave V3, GOVERNANCE_GUARDIAN | Identical 9-owner set, a Sonic-specific Safe address; also confirmed identical on Mantle the same day | Part 2 + Part 3 |
| API3, manager multisig | Same literal address, identical 8 owners | Part 1 + Part 2 + Part 3 |
| Beefy Finance, dev + treasury multisig | Same literal Safe addresses as Berachain, identical 6 and 7 owners | Part 1 + Part 2 + Part 3 |
| 1inch, Router V6 owner | Identical 5-owner set already shared across mainnet, 4 Superchain chains, Arbitrum, Polygon, BNB Chain, Avalanche, and Linea | Part 1 + Part 2 + Part 3 |
| Chainlink Data Feeds, ETH/USD owner | Identical 9-owner set already tracked on Polygon, 4 Superchain chains, and Arbitrum | Part 2 + Part 3 |

Two new real Safes never seen before in this research were also confirmed on Sonic with no overlap onto the existing roster: **Shadow Exchange** (the only protocol in this batch to publish its multisig address directly rather than needing an `owner()` derivation, 4 signers) and **SwapX** (its AlgebraFactory owner, 6 signers). Pendle Finance's governanceProxy and Silo Finance's SiloFactory owner produced the same two negative results already recorded for them on Mantle above.

### Caveats

- This is a first, wide pass sized to cover ground quickly rather than to be exhaustive on any single chain: 4 to 12 protocols per chain, against Part 2's 79. The high hit rate (64 of 86) is concentrated in protocols this research already had reason to check closely, since they were chosen partly because a prior overlap made a repeat plausible; a broader, protocol-agnostic pass on any one of these chains might find a different ratio.
- No live event-replay verification exists yet for any part of Part 3, the same gap Part 2 already carries.
- Radiant Capital's BNB Chain PoolAdmin finding is a partial signer match (7 of 11), not a full identical set: read it as "shares most of its signers with," not "is the same Safe as."
- API3's manager multisig address is chain-invariant and was tested directly via `getOwners()` on zkSync Era, Berachain, and Blast specifically, since API3's own deployment registry does not list a folder for any of the three; the address still resolves to a real, matching Safe (fully on Berachain and Blast, partially on zkSync Era), a slightly different sourcing standard than the other chains, where an explicit per-chain deployment file exists.
- Mantle, Blast, and Sonic were deliberately chosen as second-tier chains, unlike the first 8: real DeFi TVL is thinner and less stable on all three, and Blast in particular is reported as a genuinely weak, low-signal result (2 of 6 protocols tested resolved to a real multisig) rather than forced to look comparable to Mantle or Sonic.
- Silo Finance's SiloFactory owner resolving to a bare externally-owned address, not a Safe, on both Mantle and Sonic is a genuine finding about that specific role on those two chains, not a claim about Silo Finance's security posture generally: Silo uses a real multisig for this same role on every other chain this research tracks it on (mainnet, Optimism, Base, Ink, Arbitrum, BNB Chain, Avalanche).
- Several of the Safe addresses used across Part 3 were derived by a second on-chain call (`owner()`, or a role-specific getter) rather than read directly from a published multisig list; each derivation is individually logged and cross-checked before use.

### Verification

Every claim in this research follows the same verification discipline described in [Methodology at a glance](#methodology-at-a-glance) above. 66 hypotheses across the 11 chain-scoped registries (8 for Arbitrum, 58 across the other 10 chains), all at High confidence.

### Status

Last verified: 2026-09-10.

86 protocols across 11 chains, three passes deep: a pilot on Arbitrum (12 protocols), a same-day pass across seven more chains (48 protocols), then a follow-up pass across three more second-tier chains (26 protocols). Not a finished survey on any of the 11, and no live event-replay verification exists yet for this part, the same gap noted throughout the Caveats above.

This is independent research, not commissioned, audited, or endorsed by any protocol, chain, or individual named above. Everything stated is held to the confidence level the on-chain data actually supports.

## About

This is part of a small, ongoing program of independent on-chain research, same discipline throughout: primary-source anchors, on-chain reconstruction, corrections issued openly when something's found wrong. The sibling project [onchain-postmortems](https://github.com/RealSpap/onchain-postmortems) applies the same discipline to DeFi security incidents; see that repo's own at-a-glance table for the current incident count, recomputed loss total, and corrections made, rather than duplicating fast-moving figures here that would only go stale again. Ongoing work and dashboards: [Dune](https://dune.com/s_pap), [X](https://x.com/RealSpap).

## License

All rights reserved. This repository documents the results; the tool itself is available under a commercial license, see above.
