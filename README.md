# multisig-overlap

![License](https://img.shields.io/badge/license-all%20rights%20reserved-blue)
![Status](https://img.shields.io/badge/status-active%20research-brightgreen)
![Identities found (mainnet)](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FRealSpap%2Fmultisig-overlap-showcase%2Fmain%2Fbadge-data-mainnet.json)
![Protocols tracked (Superchain)](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FRealSpap%2Fmultisig-overlap-showcase%2Fmain%2Fbadge-data-superchain.json)
![Protocols tracked (Part 3)](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FRealSpap%2Fmultisig-overlap-showcase%2Fmain%2Fbadge-data-part3.json)
![Follow](https://img.shields.io/badge/follow-%40RealSpap-000000?logo=x)

**The headline finding:** the same question, checked at three scales. On Ethereum mainnet, 8 named individuals hold multisig signer keys across 2 or more unrelated DeFi protocols at once, one now reaching 5 protocols and another reaching 4, identified across 75 protocols checked directly on-chain. Extended to Optimism's Superchain, the same pattern recurs 6 more times: one brand-new named individual (aavechan.eth), two of the original 8 turning up again on new chains, and two chain-operator entities concentrating upgrade keys across multiple chains at once. A third extension, onto Arbitrum and seven more L2s and sidechains, finds an already-tracked signer set or Safe address reappearing on 52 of 60 further protocols checked, including one named individual (c2tp.eth) now confirmed on 4 of those 8 chains. Separately, 30+ protocols reuse the identical Gnosis Safe signer set on multiple chains at once, so spreading exposure across a protocol's chain deployments doesn't actually diversify against key compromise. [Mainnet findings](#part-1-mainnet) · [Superchain findings](#part-2-superchain) · [Part 3 findings](#part-3-arbitrum-and-other-l2s) · [Contact for licensing / custom research](https://x.com/RealSpap)

**Want this method run on your protocol, or a custom research pass? License it: DM [@RealSpap](https://x.com/RealSpap) on X.**

## At a glance

| | Mainnet | Superchain | Part 3 (other L2s) |
|---|---|---|---|
| Protocols checked | 75 | 79 | 60 (12 on Arbitrum, 48 across 7 further chains) |
| Safes checked | 142 signer slots tested, 125 confirmed as real Safe contracts | 200 Safes across 166 deployments | 90 candidate addresses tested, 71 confirmed as real Safe contracts |
| Chains covered | Ethereum mainnet | 13 | 8 (Arbitrum One, Polygon PoS, BNB Chain, Avalanche C-Chain, zkSync Era, Linea, Scroll, Berachain) |
| Shared-key findings | 8 named identities holding signer power on 2+ protocols (Michael Egorov now reaching 5, c2tp.eth reaching 4), plus 22 more shared-infrastructure and signer-overlap cases | 6 documented cross-protocol or cross-chain signer-sharing cases, plus 30+ protocols sharing an identical signer set across chains | 52 of 60 protocols extend a signer-set or Safe-address pattern already found in Part 1 or Part 2, including 1 named identity (c2tp.eth, now on 4 of these 8 chains) and several same-address patterns reaching 6 or more chains at once |
| Research depth | 75-protocol scope, extended seven times in one day (2026-09-10); every finding independently verified on-chain | 31 research passes, still growing | Two passes on 2026-09-10 (an Arbitrum pilot, then seven more chains the same day); explicitly not exhaustive on any of the 8 chains |
| Live verification | Yes, on-chain event replay (covers 69 of the 125 confirmed Safes so far) | Dashboard only; on-chain event replay planned for a future pass | Not built yet |

Every major DeFi protocol discloses its own emergency and governance multisig signers, usually in its own docs. Nobody aggregates that across protocols or chains, so nobody could previously answer: if one person's key, or one shared signer set, were compromised, how many independent protocols or chains would be affected at the same time? This research answers that at three scales: first across 75 major protocols on Ethereum mainnet, then across Optimism's Superchain specifically, where the same protocol is often deployed on a dozen chains at once, then a third time on Arbitrum and seven more L2s and sidechains deliberately outside the Superchain family.

## Access to the tool

The verification method behind this research is available under a commercial license, not published in this repository. The findings below were produced with it and are independently reproducible by anyone with the same access; this repo documents the results, not the mechanism. Reach out via [RealSpap on X](https://x.com/RealSpap) for licensing.

## Disclaimer

This report presents an independent, factual analysis of publicly available on-chain data (smart contract code, multisig signer sets, governance transactions) as of the date noted in the Status/Method sections below. Statements about which addresses or individuals hold administrative, multisig, or governance keys are based solely on on-chain records and publicly disclosed information cited inline; they are not allegations of wrongdoing, and no claim of illegal conduct, fraud, or misconduct is made or implied. Concentration of control or key-holder identity is reported as an observed structural fact, not as a moral or legal judgment on the individuals named. Findings reflect a snapshot in time; on-chain configurations, signer sets, and governance parameters can and do change after publication, and this report is not updated automatically to reflect such changes. This is independent research, not commissioned or audited by any protocol discussed, and it does not constitute legal, financial, or investment advice. Any individual or entity named in this report who believes information about them is inaccurate or outdated is invited to contact the author via [X](https://x.com/RealSpap) with supporting evidence; corrections will be issued promptly and transparently. Readers should independently verify all cited addresses, transactions, and figures before relying on them.

## Part 1: Mainnet

### Method

Last verified: 2026-09-10

75 protocols' multisig contracts (Gnosis Safe) checked directly on-chain via `getOwners()`: no API key, no third-party indexer, pure RPC reads against a public Ethereum node. 142 signer slots tested, 125 confirmed as real Safe contracts. Scope grew from the original 41 protocols across seven research passes on 2026-09-10 alone, each adding several more protocols and re-running the full cross-reference against every signer already on record.

### Findings

8 addresses hold signer power on 2+ independent protocols, sorted by how many protocols each one touches. All 8 are identified by name or known pseudonym, each backed by a primary-source citation:

| Rank | Identity | Protocols | Reach | Role |
|---|---|---|---|---|
| 1 | **Michael Egorov** | Abracadabra + Yearn + Prisma + Threshold Network + Usual Money | 5 protocols | Founder of Curve Finance |
| 2 | **c2tp.eth** | Convex (his own protocol) + Prisma + Votium + Curve Finance's own Emergency DAO | 4 protocols | Pseudonymous creator of Convex Finance |
| 3 | **Ernesto Boado** (BGD Labs) | Lido + Balancer | 2 protocols | Infrastructure/security provider working with multiple protocols |
| 3 | **Pablo Veyrat** | Angle (his own protocol) + Morpho | 2 protocols | Founder of Angle Protocol |
| 3 | **Julien Bouteloup** | Abracadabra + StakeDAO (his own protocol) | 2 protocols | Founder of StakeDAO / Rekt News, early Curve team |
| 3 | **"Tommy"** | Votium (his own protocol) + Convex | 2 protocols | Known representative of Votium |
| 3 | **Sam Kazemian** (high confidence, not independently name-confirmed) | Frax (his own protocol) + Prisma | 2 protocols | Founder of Frax Finance |
| 3 | **Matthew Graham** | Gearbox + TokenLogic (his own service) | 2 protocols | Founder of TokenLogic |

*What this means in practice: Egorov's key now touches 5 independent protocols at once, the widest documented mainnet reach of any named individual in this research; c2tp.eth's touches 4. A single compromised key for either one puts several unrelated protocols' funds at risk simultaneously, not one.*

Three of the eight (Egorov, c2tp, Kazemian) sit together on Prisma Finance's emergency multisig, a deliberate, publicly disclosed design choice by Prisma to recruit established protocol founders for credibility, not a hidden concentration. The other five are more organic: independent protocols with no obvious institutional link to each other.

Matthew Graham and TokenLogic reappear in Part 2 below: the same footprint that starts here on Gearbox and TokenLogic's own Ethereum Safe extends onto three of Aave's Superchain Safes as well.

Extending mainnet coverage from 41 to 75 protocols across seven research passes on 2026-09-10 surfaced 22 more cases beyond the 8 named identities above. Three extend an identity already named in the table (Egorov's seats on Threshold Network and Usual Money, c2tp.eth's seat on Curve Finance's own Emergency DAO); the other 19 are Safes and signer sets already tracked elsewhere in this research turning up again on Ethereum mainnet, plus a couple of new pseudonymous overlaps entirely within mainnet itself:

| Case | What's shared |
|---|---|
| EigenLayer / Aave | EigenLayer's own Pauser, Community, Executor, and Operations multisigs are the identical Safes already used by Aave under those same roles, at 4 different addresses (7, 13, 2, and 6 owners). No public source explains why |
| Silo Finance, L1 | Silo Finance's mainnet SiloFactory owner is the identical Safe already tracked on Optimism, Base, and Ink; the mainnet 3-of-4 set is a subset of the 5 owners on those chains |
| 1inch, L1 | 1inch's Aggregation Router V6 owner on mainnet shares the identical 5-signer set already tracked on Optimism, Base, and Unichain |
| ether.fi, L1 | ether.fi's mainnet Controller Safe shares 4 of its 7 signers with the Controller Safe set already tracked on Base, Ink, Mode, Optimism, and Unichain: a partial rather than full match |
| Aura Finance / Balancer | One signer of Aura's sudo multisig also sits on Balancer's DAO multisig. Aura is built directly on Balancer's veBAL system, an institutionally expected link |
| Aura Finance / Abracadabra | A different signer of Aura's sudo multisig also sits on Abracadabra Money's multisig, with no obvious institutional link between the two |
| API3, L1 | API3's manager multisig, already the identical Safe on 7 Superchain chains, resolves identically on Ethereum mainnet too: an 8th chain, tying Curve's Emergency DAO for the widest same-address propagation in the dataset |
| Odos, L1 | Odos' Router V3 owner on mainnet is the literal same Safe address already tracked on Optimism, Base, and Unichain |
| deBridge, L1 | deBridge's mainnet admin Safe shares the identical 8-owner set already tracked on Optimism and Base |
| ParaSwap / Velora, L1 | ParaSwap/Velora's mainnet AugustusSwapper admin is a 12-owner Safe identical to the set already tracked on Base and Optimism |
| Beefy Finance, L1 | Beefy's mainnet devMultisig is the identical 6-owner Safe already shared across six Superchain chains; a separate treasuryMultisig is a genuine, unshared 7-signer Safe |
| Hyperlane, L1 | Hyperlane's mainnet Mailbox and ProxyAdmin owner is the identical 10-owner Safe already tracked on Optimism and Base |
| Renzo Protocol, L1 | Renzo's mainnet admin Safe shares the identical 6-owner set already tracked on Ink, and is a strict superset of the 5 owners shared by Optimism, Base, Mode, Unichain, and World Chain: Ethereum L1 becomes the 7th deployment of this signer group |
| Chainlink Data Feeds, L1 | Chainlink's mainnet ETH/USD price feed owner shares the identical 9-owner set already tracked on 4 Superchain chains, making mainnet the 6th chain carrying this signer group |
| Kelp DAO / Stader Labs | One signer of Kelp DAO's mainnet manager Safe also sits on Stader Labs' Optimism Safe. Kelp DAO and Stader Labs share founders (Amitej G and Dheeraj B), an institutionally expected link |
| Superfluid, L1 | Superfluid's mainnet protocol-governance Safe is the identical Safe already tracked on Optimism, Base, and Celo |
| Term Finance, L1 | Term Finance's mainnet admin and devops Safes are the identical contract addresses already tracked on Base |
| Compound / Resolv | The same pseudonymous signer already linking Compound III's Base Pause Guardian to Resolv's Base and Soneium Safes also sits on both Compound's own mainnet pauseGuardian and Resolv's mainnet Token Owner Safe: the first direct mainnet-to-mainnet overlap found within Part 1 itself |
| AladdinDAO / f(x) Protocol | f(x) Protocol's governance Safe shares its full 9-signer set with AladdinDAO's own Concentrator Treasury Safe. AladdinDAO is the team that built f(x) Protocol, an institutionally expected link |

None of these 22 cases turns up a new named individual beyond the two extensions to Egorov and c2tp.eth above; the pseudonymous signers in the Aura, Kelp DAO, and Compound/Resolv rows could not be tied to a real name from a primary source strong enough to publish under this research's own naming bar, so they're reported at address level only.

### Live verification

[dune.com/s_pap/multisig-overlap](https://dune.com/s_pap/multisig-overlap): a self-computing query that skips the point-in-time snapshot entirely and replays the actual on-chain event history of all 69 Safe contracts tracked as of the query's own last update, recomputing current ownership fresh every time it runs. This hasn't yet been extended to the 34 protocols added on 2026-09-10, so the newer findings above are confirmed by direct on-chain reads at a point in time, not yet by event replay.

**Get notified**, no account needed on this repo: click Watch, then Custom, then Releases only, on this repo's GitHub page for a per-pass update feed. On Dune, star the dashboard to keep it in your own list, or set a scheduled alert on the query for a ping the moment a tracked Safe's owner set actually changes on-chain, not just when this repo gets updated.

The live query relies on parsing on-chain event history rather than static contract reads. Some older Safes were created before their deployment transaction logged the data a pure event-based rebuild needs, so 2 of the 8 identities (Julien Bouteloup's second seat and c2tp.eth's Convex seat) are instead confirmed by a direct `getOwners()` read, independently cross-checked by manually reading the relevant transaction logs on Etherscan.

### Open data (Mainnet)

The live query's own result table is queryable directly through [Dune's Query API](https://docs.dune.com/api-reference/api-overview) by anyone with a free Dune API key, no scraping needed: pull the same 8 identities the same way this page does, recomputed fresh on every call.

### What's checked next (Mainnet)

75 protocols is a pilot, not a finished survey. Open a GitHub Issue on this repo to suggest the next protocol to check; a thumbs-up on an existing suggestion counts as a vote (this sets research priority only; checks are still run under the same licensed method, not opened to contributors). The Superchain-specific follow-up already covers 79 more protocols, and a third extension covers 60 more across Arbitrum and seven other L2s and sidechains: see Part 2 and Part 3 below.

### Caveats (Mainnet)

- One of the 8 identities (Julien Bouteloup's second seat) and one seat behind another (c2tp.eth's Convex seat) don't reproduce through live event replay, because they sit on Safe versions old enough that their creation transactions don't log the data a pure event-based rebuild needs; both are confirmed by a direct `getOwners()` read instead. See Live verification above.
- 75 protocols is a pilot, not a finished survey (see What's checked next). A protocol not listed here hasn't been checked, not confirmed clean.
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

**Get notified of new passes**, no account needed on this repo: click Watch, then Custom, then Releases only, on this repo's GitHub page. Every research pass gets tagged as a release, title and body taken straight from that pass's own commit message. On Dune, star the dashboard to have it in your own list, or set a scheduled alert on the query for a ping when a tracked Safe's owner set changes.

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

## Part 3: Arbitrum and other L2s

An extension of the same method beyond the Superchain family covered in Part 2, onto major L2s and sidechains that each run their own separate architecture and governance: Arbitrum (Nitro, the Arbitrum DAO and Security Council) first, as a pilot pass, then seven more chains chosen for real TVL and a real governance or emergency multisig, all checked the same day: Polygon PoS, BNB Chain, Avalanche C-Chain, zkSync Era, Linea, Scroll, and Berachain. Parts 1 and 2 both ask whether the same signer or Safe holds trusted power across multiple unrelated protocols or chains at once; this part asks the identical question a third time, on a third terrain, and every signer recovered here is cross-referenced against the full combined roster of Part 1 and Part 2, not just one or the other.

### Arbitrum

A first pilot pass onto Arbitrum One, a major L2 deliberately outside the Superchain family covered in Part 2: Arbitrum runs on Nitro, not the OP Stack, with its own separate rollup architecture, bridge, and governance (the Arbitrum DAO and its Security Council). This is explicitly a first pass, not an exhaustive survey: 12 protocols were chosen for real TVL and a real governance or emergency multisig, deliberately mixing protocols never touched by this research before (GMX, Camelot, Dolomite) with protocols already tracked on other chains (Aave, Compound III, Curve Finance, 1inch, Silo Finance, Beefy Finance, Chainlink, Pendle Finance, and Radiant Capital), since the latter group is exactly where a real cross-reference hit is most likely to show up, and it did.

#### Method

12 Arbitrum-native or Arbitrum-deployed DeFi protocols checked directly on-chain via `getOwners()`: no API key, no third-party indexer, pure RPC reads against a public Arbitrum node. Every candidate address came from a primary source (official docs or GitHub deployment registry); several sources publish a factory, provider, or router contract rather than the multisig directly, so the actual Safe address was obtained by calling `owner()` or a role-specific getter on that contract first, then re-verified with its own `getOwners()` call. 20 candidate addresses were tested; 13 resolved to confirmed Gnosis Safe contracts, recovering 87 signer slots (83 unique addresses), every one of them cross-referenced against the combined roster of unique signer addresses already on record from Parts 1 and 2.

#### Findings

No signer or Safe was shared between two different protocols within the Arbitrum sample itself. The real signal is cross-part: 8 of the 12 Arbitrum protocols checked turn out to extend a pattern this research had already documented on other chains, sometimes at the literal same Safe address and sometimes at a different address with an identical or overlapping signer list.

| Protocol (Arbitrum) | What was found | Already tracked as |
|---|---|---|
| **Compound III**, pauseGuardian | Identical 9-owner set as Compound's own Ethereum mainnet pauseGuardian and Compound III's Base Pause Guardian. One of the 9 is the same pseudonymous signer already linking Compound III's Base Pause Guardian to Resolv's Base and Soneium Token Owner Safes; that signer's reach now spans two protocols across five chain-level deployments | Part 1 + Part 2 |
| **Curve Finance**, Emergency DAO | Deployed at the literal same Safe contract address (`0x6d447e544D01a59cb0774763bf15526574CffFeD`) already used on Ethereum mainnet and the 6 Superchain chains this research tracks. One of the 9 owners is c2tp.eth, already named above for Convex, Prisma, Votium, and Curve's own mainnet Emergency DAO Safe: an institutionally expected link given Convex is built directly on Curve | Part 1 + Part 2 |
| **Aave V3**, GOVERNANCE_GUARDIAN | Identical 9-owner set as Aave V3's own governance-guardian Safe on BOB, already tracked in Part 2, at a different Safe address | Part 2 |
| **1inch**, Aggregation Router V6 owner | Identical 5-owner set already shared, at one single literal address, across mainnet, Optimism, Base, and Unichain. Arbitrum is the first of these deployments to use a distinct Safe address for the same 5 people | Part 1 + Part 2 |
| **Silo Finance**, SiloFactory owner | 4 owners, identical to that same Safe's own mainnet owner set, and a complete subset of its 5-owner (Optimism, Base) and 6-owner (Ink) versions | Part 1 + Part 2 |
| **Beefy Finance**, devMultisig | Identical 6-owner set already shared across 6 Superchain chains; Arbitrum is a 7th | Part 2 |
| **Chainlink Data Feeds**, ETH/USD feed owner | Identical 9-owner set already tracked on 4 Superchain chains; Arbitrum is a 5th | Part 2 |
| **Radiant Capital**, EmergencyAdmin | 5 owners, a complete subset of the 8-owner Dao Treasury Safe already tracked for Radiant Capital on Base: same protocol, different role and chain, partial signer reuse rather than a full match | Part 2 |

Four protocols showed no overlap with the existing combined roster at all: **GMX** (2 confirmed Safes, 7 and 8 signers), **Camelot** (2 confirmed Safes, 3 and 6 signers), **Dolomite**, and **Pendle Finance** (both confirmed real admin contracts, but not classic Gnosis Safes).

#### Caveats

This is a first pass sized for a pilot, not a survey: 12 protocols against Part 2's 79. The 8 cross-part findings above are concentrated in protocols this research already had reason to check closely (they were chosen partly because a prior overlap made a repeat plausible), so the 4-of-12 clean rate shouldn't be read as a general hit rate for Arbitrum; a broader, protocol-agnostic pass might find a different ratio in either direction. No live event-replay verification exists yet for this part, the same gap Part 2 already carries. Radiant Capital's docs page lists several PoolAddressesProvider addresses for different isolated markets; only the main-market one was checked, so a signer overlap specific to one of its isolated markets would not have been caught here.

#### Verification

Every claim in this part is backed by a primary-source citation, tracked against a falsification test and a confidence level, following the same standard as Parts 1 and 2. All 8 hypotheses currently in the registry are at Haute confidence.

### Further chains

The same day the Arbitrum pilot above wrapped up, the same method went to seven more chains at once: Polygon PoS, BNB Chain, Avalanche C-Chain, zkSync Era, Linea, Scroll, and Berachain, deliberately mixing large, long-established L2s and sidechains (Polygon, BNB Chain, Avalanche) with newer zero-knowledge and optimistic rollups (zkSync Era, Linea, Scroll) and one chain young enough (Berachain, mainnet 2025) that most of the multi-chain registries this research already relies on elsewhere do not cover it yet. 48 protocols were checked across the seven chains, weighted toward protocols already tracked somewhere else in this research (Aave, Curve Finance, Compound III, 1inch, Chainlink Data Feeds, Beefy Finance, API3, CoW Protocol, Silo Finance, Radiant Capital, Venus Protocol), the same logic the Arbitrum pilot already used, plus a small number native to one of these chains and never seen before (ZeroLend, Kodiak Finance, Berachain's own Proof-of-Liquidity core).

#### Method

70 candidate addresses tested across the seven chains, each checked directly on-chain via `getOwners()`: no API key, no third-party indexer, pure RPC reads against each chain's own public node. Several sources publish a factory, router, or provider contract rather than the multisig directly, so the actual Safe address was obtained first via a role-specific getter on that contract, then re-verified with its own `getOwners()` call, the same method already used for Silo Finance and Radiant Capital on Arbitrum above. 58 of the 70 candidates resolved to confirmed Gnosis Safe contracts, recovering 428 signer slots; the other 12 are real contracts but fail `getOwners()`, including Aave's own guardian and executor roles on all 6 chains where Aave was checked, the same negative result already recorded for these two roles on Arbitrum. Each chain's own internal cross-check (does any signer repeat across two different protocols on that one chain) comes back clean on all seven, the same result the Arbitrum pilot found first. Every signer recovered was then cross-referenced against the combined roster already built by Part 1, Part 2, and Arbitrum.

#### Findings

The internal, within-chain cross-check comes back clean on every one of the seven chains, the same as Arbitrum. The signal here is entirely cross-part and cross-chain: 44 of the 48 protocols checked turn out to extend a pattern this research had already documented elsewhere, several at the literal same Safe address.

| Chain | Protocol | What was found | Already tracked as |
|---|---|---|---|
| Polygon | Aave V3, GOVERNANCE_GUARDIAN | Identical 9-owner set, same literal Safe address as Arbitrum, BNB Chain, and Scroll | Part 2 + Part 3 |
| Polygon | Curve Finance, Emergency DAO | Same literal Safe address as mainnet, 6 Superchain chains, and Arbitrum; identical 9 owners including c2tp.eth | Part 1 + Part 2 + Part 3 |
| Polygon | Compound III, pauseGuardian | Identical 9-owner set as mainnet's and Arbitrum's pauseGuardian, including the signer already linked to Resolv | Part 1 + Part 3 |
| Polygon | 1inch, Router V6 owner | Identical 5-owner set already shared across mainnet, Optimism, Base, Unichain, and Arbitrum | Part 1 + Part 2 + Part 3 |
| Polygon | Chainlink Data Feeds, ETH/USD owner | Identical 9-owner set already tracked on 4 Superchain chains and Arbitrum | Part 2 + Part 3 |
| Polygon | Beefy Finance, dev + treasury multisig | Identical 6 and 7-owner sets already shared on mainnet, 6 Superchain chains, and Arbitrum | Part 1 + Part 2 + Part 3 |
| Polygon | API3, manager multisig | Same literal address, identical 8 owners, already the widest same-address spread in the dataset | Part 1 + Part 2 + Part 3 |
| Polygon | CoW Protocol, admin Safe | Same literal address and identical 9 owners already tracked on Optimism and Ink | Part 2 |
| BNB Chain | Aave V3, GOVERNANCE_GUARDIAN | Identical 9-owner set, same literal Safe address as Polygon, Scroll, and Arbitrum | Part 2 + Part 3 |
| BNB Chain | Curve Finance, Emergency DAO | Same literal Safe address as every other chain this research tracks it on | Part 1 + Part 2 + Part 3 |
| BNB Chain | Silo Finance, SiloFactory owner | Same literal Safe address as mainnet, Optimism, Base, Ink, and Arbitrum; identical 4 owners | Part 1 + Part 2 + Part 3 |
| BNB Chain | 1inch, Router V6 owner | Identical 5-owner set already shared everywhere else in this research | Part 1 + Part 2 + Part 3 |
| BNB Chain | Chainlink Data Feeds, ETH/USD owner | Identical 9-owner set already tracked elsewhere in this research | Part 2 + Part 3 |
| BNB Chain | Beefy Finance, dev + treasury multisig | Identical sets already shared elsewhere; BNB Chain is Beefy's own founding chain | Part 1 + Part 2 + Part 3 |
| BNB Chain | API3, manager multisig | Same literal address, identical 8 owners | Part 1 + Part 2 + Part 3 |
| BNB Chain | CoW Protocol, admin Safe | Same literal address as Optimism, Ink, and Polygon; identical 9 owners | Part 2 |
| BNB Chain | Radiant Capital, PoolAdmin | 7 of 11 owners match Radiant's own 8-owner Dao Treasury Safe on Base, plus 4 new signers | Part 2 |
| BNB Chain | Radiant Capital, EmergencyAdmin | Identical 5-owner set already tracked as Radiant's EmergencyAdmin on Arbitrum | Part 2 + Part 3 |
| BNB Chain | Venus Protocol, Guardian (3 Safes, same set) | Identical 7-owner set already tracked as Venus's Guardian multisig on Base and Unichain | Part 2 |
| Avalanche | Aave V3, GOVERNANCE_GUARDIAN | Identical 9-owner set, an Avalanche-specific Safe address | Part 2 + Part 3 |
| Avalanche | Curve Finance, Emergency DAO | Same literal Safe address as every other chain this research tracks it on | Part 1 + Part 2 + Part 3 |
| Avalanche | Silo Finance, SiloFactory owner | Same literal Safe address as mainnet, Optimism, Base, Ink, Arbitrum, and BNB Chain | Part 1 + Part 2 + Part 3 |
| Avalanche | 1inch, Router V6 owner | Identical 5-owner set already shared everywhere else in this research | Part 1 + Part 2 + Part 3 |
| Avalanche | Chainlink Data Feeds, ETH/USD owner | Identical 9-owner set already tracked elsewhere in this research | Part 2 + Part 3 |
| Avalanche | Beefy Finance, dev + treasury multisig | Identical sets already shared elsewhere; one of Beefy's earliest-supported chains | Part 1 + Part 2 + Part 3 |
| Avalanche | API3, manager multisig | Same literal address, identical 8 owners | Part 1 + Part 2 + Part 3 |
| Avalanche | CoW Protocol, admin Safe | Same literal address as Optimism, Ink, Polygon, and BNB Chain | Part 2 |
| zkSync Era | Aave V3, GOVERNANCE_GUARDIAN | Identical 9-owner set, a zkSync-specific Safe address | Part 2 + Part 3 |
| zkSync Era | Chainlink Data Feeds, ETH/USD owner | Identical 9-owner set already tracked elsewhere in this research | Part 2 + Part 3 |
| zkSync Era | Beefy Finance, dev + treasury multisig | Identical sets already shared elsewhere | Part 1 + Part 2 + Part 3 |
| zkSync Era | API3, manager multisig | Same literal address; only 6 of 8 owners match, a partial rather than a full set, the only chain in this batch where that is true | Part 1 + Part 2 + Part 3 (partial) |
| zkSync Era | Venus Protocol, Guardian | Identical 7-owner set already tracked as Venus's Guardian multisig on Base and Unichain | Part 2 |
| Linea | Aave V3, GOVERNANCE_GUARDIAN | Identical 9-owner set, a Linea-specific Safe address | Part 2 + Part 3 |
| Linea | Compound III, pauseGuardian | Identical 9-owner set as mainnet's, Arbitrum's, and Polygon's pauseGuardian | Part 1 + Part 3 |
| Linea | 1inch, Router V6 owner | Identical 5-owner set already shared everywhere else in this research | Part 1 + Part 2 + Part 3 |
| Linea | Chainlink Data Feeds, ETH/USD owner | Identical 9-owner set already tracked elsewhere in this research | Part 2 + Part 3 |
| Linea | Beefy Finance, dev + treasury multisig | Identical sets already shared elsewhere | Part 1 + Part 2 + Part 3 |
| Linea | API3, manager multisig | Same literal address, identical 8 owners | Part 1 + Part 2 + Part 3 |
| Scroll | Aave V3, GOVERNANCE_GUARDIAN | Identical 9-owner set, same literal Safe address as Polygon, BNB Chain, and Arbitrum | Part 2 + Part 3 |
| Scroll | Compound III, pauseGuardian | Identical 9-owner set as mainnet's, Arbitrum's, Polygon's, and Linea's pauseGuardian | Part 1 + Part 3 |
| Scroll | Chainlink Data Feeds, ETH/USD owner | Identical 9-owner set already tracked elsewhere in this research | Part 2 + Part 3 |
| Scroll | Beefy Finance, dev + treasury multisig | Identical sets already shared elsewhere | Part 1 + Part 2 + Part 3 |
| Scroll | API3, manager multisig | Same literal address, identical 8 owners | Part 1 + Part 2 + Part 3 |
| Berachain | Beefy Finance, dev + treasury multisig | Identical sets already shared across every other chain checked in this batch | Part 1 + Part 2 + Part 3 |
| Berachain | API3, manager multisig | Same literal address, identical 8 owners, even though the chain isn't yet listed in API3's own public deployment registry | Part 1 + Part 2 + Part 3 |

Four protocols showed no overlap with the existing combined roster at all, counted once per chain: **ZeroLend** (zkSync Era and Linea, never tracked before in this research; the two Safes share an identical 5-owner set with each other but with nothing else in this dataset), **Kodiak Finance** (Berachain, a real 5-owner Safe never seen before), and **Berachain's own Proof-of-Liquidity core** (the Safe that assigns BGT emission weights to reward vaults, also never seen before). Two more Berachain-native contracts checked the same way are real contracts but access-controlled by role rather than by a single owner, so no candidate Safe could be recovered for either, a negative result worth recording rather than a gap. On top of Aave's guardian/executor negative result already noted in Method above, this batch's one partial-rather-than-full match is API3's manager multisig on zkSync Era specifically (see table).

#### Caveats

- This is a first, wide pass across seven chains at once, sized to cover ground quickly rather than to be exhaustive on any single one: 4 to 10 protocols per chain, against Part 2's 79. The high hit rate (44 of 48) is concentrated in protocols this research already had reason to check closely, the same caveat the Arbitrum pilot above already carries; a broader, protocol-agnostic pass on any one of these seven chains might find a different ratio.
- No live event-replay verification exists yet for any of these seven chains, the same gap Part 2 and Arbitrum already carry.
- API3's manager multisig address is chain-invariant and was tested directly on zkSync Era and Berachain even though neither has an explicit entry in API3's own public deployment registry yet; the address still resolves to a real, matching Safe (fully on Berachain, partially on zkSync Era), a slightly different sourcing standard than the other five chains.
- Radiant Capital's BNB Chain PoolAdmin finding is a partial signer match (7 of 11), not a full identical set: read it as "shares most of its signers with," not "is the same Safe as."

#### Verification

Every claim in this subsection is backed by a primary-source citation, tracked against a falsification test and a confidence level, following the same standard as the rest of this research. 47 hypotheses across the seven chain-scoped registries, all at Haute confidence.

### What's checked next (Part 3)

Not a finished survey by design (see Caveats above). Open a GitHub Issue on this repo to suggest the next chain or protocol to check; a thumbs-up on an existing suggestion counts as a vote (this sets research priority only; checks are still run under the same licensed method, not opened to contributors).

### Status

Last verified: 2026-09-10

60 protocols across 8 chains, two passes deep: a pilot on Arbitrum (12 protocols), then a same-day pass across seven more chains (48 protocols). Not a finished survey on any of the 8, and no live event-replay verification exists yet for this part, the same gap noted throughout the Caveats above.

This is independent research, not commissioned, audited, or endorsed by any protocol, chain, or individual named above. Everything stated is held to the confidence level the on-chain data actually supports.

## About

This is part of a small, ongoing program of independent on-chain research, same discipline throughout: primary-source anchors, on-chain reconstruction, corrections issued openly when something's found wrong. The sibling project [onchain-postmortems](https://github.com/RealSpap/onchain-postmortems) applies it to 8 DeFi exploits, correcting 4 already-published press or DefiLlama figures along the way, about $29.5M recomputed from primary sources across those 8 incidents. Ongoing work and dashboards: [Dune](https://dune.com/s_pap), [X](https://x.com/RealSpap).

## License

All rights reserved. This repository documents the results; the tool itself is available under a commercial license, see above.
