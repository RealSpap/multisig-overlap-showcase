## Part 3: Arbitrum and other L2s

An extension of the same method beyond the Superchain family covered in Part 2, onto major L2s and sidechains that each run their own separate architecture and governance, added in successive passes:

- **Arbitrum** (Nitro, the Arbitrum DAO and Security Council): first, as a pilot pass.
- **Seven more chains**, chosen for real TVL and a real governance or emergency multisig: Polygon PoS, BNB Chain, Avalanche C-Chain, zkSync Era, Linea, Scroll, and Berachain.
- **Three more, explicitly second-tier, chains**: Mantle, Blast, and Sonic, added in a follow-up pass. Deliberately chosen unlike the first 8, which were picked for real TVL: on these three, real DeFi TVL is thinner and less stable.
- **A fourth pass (2026-09-18)** added 47 more candidate entries across the same 11 chains: 6 new protocols (LI.FI, Kelp DAO rsETH, Stader Labs, Euler V2, Balancer, Threshold Network/tBTC), plus one new cross-protocol overlap (Kelp DAO / Stader Labs, sharing founders, same expected-link reasoning as the equivalent case in Part 2), and a correction: two previously-tracked Pendle entries (`governanceProxy`, `devProxyAdmin`) turned out not to be Safe contracts (`getOwners()` reverts) and were replaced with Pendle's real Governance and Dev Multisig Safes.
- **A sixth pass (2026-10-05)** added 11 protocols on Arbitrum (dHEDGE, CoW Protocol, API3, Hyperlane, Puffer, Synapse, Spark Liquidity Layer, USDT0, Odos, Premia and deBridge; 17 Safes, plus the Safe behind Dolomite's owner contract, 18 in all), with no new cross-protocol signer overlap: every new signer reappears only inside the same protocol on its other chains. Two notes on already-published Arbitrum entries came with it: Radiant's EmergencyAdmin Safe reads a threshold of 1 (5 owners), and Dolomite's owner is an AccessControl contract whose admin role is held by a 2-of-3 Safe.
- **A fifth pass (2026-09-30)** added 4 protocols on Arbitrum (the Arbitrum Security Council, Frax Finance, Yearn, and Ethena; 8 Safes), with no new cross-protocol signer overlap on Arbitrum. One reconciliation note came with it: Camelot's Ecosystem Safe reads 3-of-6 on-chain, where Camelot's docs state 4-of-6; when that changed is not established.

Parts 1 and 2 both ask whether the same signer or Safe holds trusted power across multiple independent protocols or chains at once; this part asks the identical question a third time, on a third terrain, and every signer recovered here is cross-referenced against the full combined roster of Part 1 and Part 2, not just one or the other.

### Method

185 candidate addresses resolved to confirmed Gnosis Safe contracts across the 11 chains (see [Methodology at a glance](method.md#methodology-at-a-glance) above), up from 167 before the sixth pass on 2026-10-05, which added 11 protocols on Arbitrum (167 was itself up from 159 after the fifth pass on 2026-09-30, which added the Arbitrum Security Council, Frax Finance, Yearn and Ethena on Arbitrum). Several sources publish a factory, provider, or router contract rather than the multisig directly, so the actual Safe address was obtained by calling `owner()` or a role-specific getter on that contract first, then re-verified with its own `getOwners()` call. Each chain's own internal cross-check (does any signer repeat across two different protocols on that one chain) comes back clean on all 11; the signal is entirely cross-part and cross-chain, with the sole exception of the new Kelp DAO / Stader Labs case noted above.

### Findings

66 of the first 94 protocols checked across Part 3 extend a pattern this research had already documented elsewhere (the 4 added on 2026-09-30 have not yet been assessed for pattern extension, and the 11 added on 2026-10-05 add no new cross-protocol link), sometimes at the literal same Safe address and sometimes at a different address with an identical or overlapping signer list:

- **2 Part 1 keys** recur: Key B, via Curve Finance's Emergency DAO Safe, now confirmed on 4 of these 11 chains; and Key F, via Morpho Blue's DAO Safe on Arbitrum.
- **Same-owner patterns (often at the same address)** now reach 9 or 10 of these 11 chains at once: Aave's GOVERNANCE_GUARDIAN on 9, Beefy Finance's dev/treasury multisigs on 10, API3's manager multisig on 10.

The other 28 of those first 94 show no overlap with the existing roster. The per-chain sections below give the detail; the main examples fall two ways (a protocol can appear in both lists when its result differs by chain, as ZeroLend and Pendle Finance do):

- **Real new Safes**: GMX and Camelot on Arbitrum; Merchant Moe, INIT Capital, Shadow Exchange, SwapX, Kodiak Finance, ZeroLend, and Berachain's own Proof-of-Liquidity core on the newer chains.
- **No usable Safe recovered**: Dolomite and Pendle Finance on Arbitrum; Pendle Finance, Silo Finance, Lendle, Agni Finance, ZeroLend, Overnight Finance's AgentTimelock, Mangrove, and 1inch on Mantle, Blast and Sonic, a low-TVL-chain pattern largely absent from the first 8 chains checked.

#### Arbitrum

A first pilot pass, deliberately mixing protocols never touched by this research before (GMX, Camelot, Dolomite) with protocols already tracked elsewhere (Aave, Compound III, Curve Finance, 1inch, Silo Finance, Beefy Finance, Chainlink, Pendle Finance, and Radiant Capital). 22 candidate addresses were tested; 15 resolved to confirmed Gnosis Safe contracts, recovering 101 signer slots (97 unique addresses). No signer or Safe was shared between two different protocols within the Arbitrum sample itself; 10 of the 14 Arbitrum protocols checked extend a pattern already documented on other chains.

<details>
<summary>Show all 10 cases</summary>

| Protocol | What was found | Already tracked as |
|---|---|---|
| **Compound III**, pauseGuardian | Identical 9-owner set as Compound's own Ethereum mainnet pauseGuardian and Compound III's Base Pause Guardian. One of the 9 is the same pseudonymous signer already linking Compound III's Base Pause Guardian to Resolv | Part 1 + Part 2 |
| **Curve Finance**, Emergency DAO | Deployed at the literal same Safe contract address already used on Ethereum mainnet and the 6 Superchain chains this research tracks. One of the 9 owners is Key B, already listed for Convex, Prisma, Votium, and Curve's own mainnet Emergency DAO Safe: an institutionally expected link given Convex is built directly on Curve | Part 1 + Part 2 *(re-read on 2026-11-02: unchanged address and unchanged 5-of-9 threshold; two of the nine owners were replaced between 15 and 31 October 2026, the same two on every chain; Key B is not one of the two who left)* |
| **Aave V3**, GOVERNANCE_GUARDIAN | Identical 9-owner set as Aave V3's own governance-guardian Safe on BOB, at a different Safe address | Part 2 |
| **1inch**, Aggregation Router V6 owner | Identical 5-owner set already shared, at one single literal address, across mainnet, Optimism, Base, and Unichain. Arbitrum is the first of these deployments to use a distinct Safe address for the same 5 people | Part 1 + Part 2 |
| **Silo Finance**, SiloFactory owner | 4 owners, identical to that same Safe's own mainnet owner set, and a complete subset of its 5-owner (Optimism, Base) and 6-owner (Ink) versions | Part 1 + Part 2 |
| **Beefy Finance**, devMultisig | Identical 6-owner set already shared across 6 Superchain chains; Arbitrum is a 7th | Part 2 |
| **Chainlink Data Feeds**, ETH/USD feed owner | Identical 9-owner set already tracked on 4 Superchain chains; Arbitrum is a 5th | Part 2 |
| **Radiant Capital**, EmergencyAdmin | 5 owners, a complete subset of the 8-owner Dao Treasury Safe already tracked for Radiant Capital on Base: same protocol, different role and chain, partial signer reuse rather than a full match | Part 2 |
| **Morpho Blue**, Morpho DAO Safe (owner of the Morpho singleton) | Identical 9-owner set, in identical order and with the identical 5-of-9 threshold, as the Morpho DAO Safe already tracked on Ethereum mainnet and Base; the raw `getOwners()` payloads match byte for byte, at a Safe address specific to Arbitrum. One of the 9 is Key F, already listed for Morpho and Angle | Part 1 + Part 2 |
| **Lido**, Emergency Brakes / CircuitBreaker Committee | The identical 5-signer, 3-of-5 set already tracked on Lido's Ethereum Emergency Brakes and on Optimism and Base, and byte-for-byte the same raw `getOwners()` payload as Optimism's. It can freeze deposits and withdrawals on Arbitrum's wstETH bridge (49,150 wstETH), confirmed with `hasRole()` on-chain, but cannot reopen them or upgrade anything: that stays with Lido's governance executor. Lido documents the shared signer set itself; what is new here is the reach: 3 of the same 5 keys can halt the official bridge route in and out of Arbitrum, Optimism and Base at once, covering about 95,500 bridged wstETH (the tokens stay transferable on each L2; only bridging stops) | Part 1 + Part 2 *(re-read on 2026-11-02: two of the five signers were replaced between 15 and 31 October 2026; the same five are read on Arbitrum, Ethereum, Optimism and Base; neither signer who left is one of the keys counted in this report)* |

</details>

Four protocols showed no overlap with the existing combined roster at all: **GMX** (2 confirmed Safes, 7 and 8 signers), **Camelot** (2 confirmed Safes, 3 and 6 signers), **Dolomite**, and **Pendle Finance** (both confirmed real admin contracts, but not classic Gnosis Safes).

The sixth pass (2026-10-05) added 11 protocols on Arbitrum, each confirmed on two public RPCs with the power of the Safe read on-chain:

<details>
<summary>Show the 11 protocols added on 2026-10-05</summary>

| Protocol | What was found | Already tracked as |
|---|---|---|
| **dHEDGE** | A 3-of-5 Safe that owns the PoolFactory and the Governance contract | Part 2, added in the 2026-10-04 update (same protocol) |
| **CoW Protocol** | A 4-of-12 Safe that owns, and is the EIP-1967 admin of, the solver allow-list | Part 1 + Part 2 |
| **API3** | A 4-of-8 Safe, the manager multisig | Part 1 + Part 2 |
| **Hyperlane** | A 6-of-10 Safe that owns the Mailbox (its ProxyAdmin sits behind a 7-day timelock) | Part 1 + Part 2 |
| **Puffer** | A 3-of-6 Safe that owns pufETH | Part 1 + Part 2 |
| **Synapse** | A 2-of-3 Safe holding DEFAULT_ADMIN_ROLE on the SynapseBridge | Part 1 + Part 2 |
| **Spark Liquidity Layer** | Five Safes (2-of-5, 2-of-4, 1-of-2, 3-of-5 and 2-of-3) with the freezer role on the ALM controller; one of the five needs a single signature | Part 1 + Part 2 |
| **USDT0** | A 3-of-5 Safe that owns the token and its ProxyAdmin | Part 1, and Part 2 since the 2026-10-04 update |
| **Odos** | A 1-of-6 Safe that owns the Router V3: a single signer acts alone | Part 1 + Part 2 |
| **Premia** | Three Safes (4-of-5, 4-of-5 and 2-of-3). Its documentation describes an 11-of-15 "Parliament", while the address reads 2-of-3 on-chain; the gap is unexplained | Part 1 + Part 2 |
| **deBridge** | A 5-of-8 Safe holding DEFAULT_ADMIN_ROLE on the DeBridgeGate | Part 1 + Part 2 |

</details>

#### Polygon

<details>
<summary>Show all 8 cases</summary>

| Protocol | What was found | Already tracked as |
|---|---|---|
| Aave V3, GOVERNANCE_GUARDIAN | Identical 9-owner set, same literal Safe address as Arbitrum, BNB Chain, and Scroll | Part 2 + Part 3 |
| Curve Finance, Emergency DAO | Same literal Safe address as mainnet, 6 Superchain chains, and Arbitrum; identical 9 owners including Key B | Part 1 + Part 2 + Part 3 |
| Compound III, pauseGuardian | Identical 9-owner set as mainnet's and Arbitrum's pauseGuardian, including the signer already linked to Resolv | Part 1 + Part 3 |
| 1inch, Router V6 owner | Identical 5-owner set already shared across mainnet, Optimism, Base, Unichain, and Arbitrum | Part 1 + Part 2 + Part 3 |
| Chainlink Data Feeds, ETH/USD owner | Identical 9-owner set already tracked on 4 Superchain chains and Arbitrum | Part 2 + Part 3 |
| Beefy Finance, dev + treasury multisig | Identical 6 and 7-owner sets already shared on mainnet, 6 Superchain chains, and Arbitrum | Part 1 + Part 2 + Part 3 |
| API3, manager multisig | Same literal address, identical 8 owners, already the widest same-address spread in the dataset | Part 1 + Part 2 + Part 3 |
| CoW Protocol, admin Safe | Same literal address and identical 9 owners already tracked on Optimism and Ink | Part 2 |

</details>

#### BNB Chain

<details>
<summary>Show all 11 cases</summary>

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

</details>

#### Avalanche

<details>
<summary>Show all 8 cases</summary>

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

</details>

#### zkSync Era

<details>
<summary>Show all 5 cases</summary>

| Protocol | What was found | Already tracked as |
|---|---|---|
| Aave V3, GOVERNANCE_GUARDIAN | Identical 9-owner set, a zkSync-specific Safe address | Part 2 + Part 3 |
| Chainlink Data Feeds, ETH/USD owner | Identical 9-owner set already tracked elsewhere in this research | Part 2 + Part 3 |
| Beefy Finance, dev + treasury multisig | Identical sets already shared elsewhere | Part 1 + Part 2 + Part 3 |
| API3, manager multisig | Same literal address; only 6 of 8 owners match, a partial rather than a full set, the only chain in this batch where that is true | Part 1 + Part 2 + Part 3 (partial) |
| Venus Protocol, Guardian | Identical 7-owner set already tracked as Venus's Guardian multisig on Base and Unichain | Part 2 |

</details>

#### Linea

<details>
<summary>Show all 6 cases</summary>

| Protocol | What was found | Already tracked as |
|---|---|---|
| Aave V3, GOVERNANCE_GUARDIAN | Identical 9-owner set, a Linea-specific Safe address | Part 2 + Part 3 |
| Compound III, pauseGuardian | Identical 9-owner set as mainnet's, Arbitrum's, and Polygon's pauseGuardian | Part 1 + Part 3 |
| 1inch, Router V6 owner | Identical 5-owner set already shared everywhere else in this research | Part 1 + Part 2 + Part 3 |
| Chainlink Data Feeds, ETH/USD owner | Identical 9-owner set already tracked elsewhere in this research | Part 2 + Part 3 |
| Beefy Finance, dev + treasury multisig | Identical sets already shared elsewhere | Part 1 + Part 2 + Part 3 |
| API3, manager multisig | Same literal address, identical 8 owners | Part 1 + Part 2 + Part 3 |

</details>

#### Scroll

<details>
<summary>Show all 5 cases</summary>

| Protocol | What was found | Already tracked as |
|---|---|---|
| Aave V3, GOVERNANCE_GUARDIAN | Identical 9-owner set, same literal Safe address as Polygon, BNB Chain, and Arbitrum | Part 2 + Part 3 |
| Compound III, pauseGuardian | Identical 9-owner set as mainnet's, Arbitrum's, Polygon's, and Linea's pauseGuardian | Part 1 + Part 3 |
| Chainlink Data Feeds, ETH/USD owner | Identical 9-owner set already tracked elsewhere in this research | Part 2 + Part 3 |
| Beefy Finance, dev + treasury multisig | Identical sets already shared elsewhere | Part 1 + Part 2 + Part 3 |
| API3, manager multisig | Same literal address, identical 8 owners | Part 1 + Part 2 + Part 3 |

</details>

#### Berachain

Berachain (mainnet 2025) is young enough that most of the multi-chain registries this research relies on elsewhere don't cover it yet, so sourcing here leans more on direct on-chain confirmation than a published deployment file.

<details>
<summary>Show all 2 cases</summary>

| Protocol | What was found | Already tracked as |
|---|---|---|
| Beefy Finance, dev + treasury multisig | Identical sets already shared across every other chain checked in this batch | Part 1 + Part 2 + Part 3 |
| API3, manager multisig | Same literal address, identical 8 owners, even though API3's own public deployment registry does not (yet) list a Berachain deployment | Part 1 + Part 2 + Part 3 |

</details>

Two new real Safes never seen before in this research were also confirmed on Berachain with no overlap onto the existing roster: **Kodiak Finance** (its own UniswapV3Factory owner, a real 5-owner Safe) and **Berachain's own Proof-of-Liquidity core** (the Safe that assigns BGT emission weights to reward vaults). Two more Berachain-native contracts checked the same way are real contracts but access-controlled by role rather than by a single owner, so no candidate Safe could be recovered for either, a negative result worth recording rather than a gap.

#### Mantle

Mantle (about $95M chain-level TVL at research time; see above for why Mantle, Blast, and Sonic are second-tier chains) produced a respectable haul of real, disclosed multisigs.

<details>
<summary>Show all 4 cases</summary>

| Protocol | What was found | Already tracked as |
|---|---|---|
| Aave V3, GOVERNANCE_GUARDIAN | Identical 9-owner set, a Mantle-specific Safe address; also confirmed identical on Sonic the same day | Part 2 + Part 3 |
| Compound III, pauseGuardian | Identical 9-owner set as mainnet's, Arbitrum's, Polygon's, Linea's, and Scroll's pauseGuardian | Part 1 + Part 3 |
| Beefy Finance, dev + treasury multisig | Different Safe addresses than every other chain this research tracks Beefy on, but byte-for-byte identical 6 and 7-owner sets to the ones already confirmed on Berachain and Sonic: same underlying people, different Safe | Part 1 + Part 2 + Part 3 |
| API3, manager multisig | Same literal address, identical 8 owners | Part 1 + Part 2 + Part 3 |

</details>

Two new real Safes never seen before in this research were also confirmed on Mantle with no overlap onto the existing roster, and several other candidates produced no usable Safe:

- **New Safes**: **Merchant Moe** (its Liquidity Book and legacy factories share one 5-owner Safe owner) and **INIT Capital** (its AccessControlManager owner, 7 signers).
- **Admin-recovery call reverts outright**: Pendle Finance's governanceProxy, Lendle's PoolAddressesProvider owner.
- **No deployed bytecode at all**, meaning a single externally-owned key rather than a multisig controls the role: Silo Finance's SiloFactory owner (a bare EOA here and on Sonic below, though Silo uses a real Safe for this same role on mainnet, Optimism, Base, Ink, Arbitrum, BNB Chain, and Avalanche), Agni Finance's factory owner, and Lendle's separate emergency-admin address.
- **Claimed by third-party listings but no bytecode on this specific chain**: 1inch's Aggregation Router V6, genuinely absent on Mantle though real and Safe-owned on Sonic.

#### Blast

This is this batch's honest weak result, reported as such rather than padded to match Mantle and Sonic. Of the 6 protocols tested on Blast, only 2 resolved to a real, confirmed Safe, a 2-of-6 hit rate against Mantle's 6-of-11 and Sonic's 7-of-9. This tracks the underlying ecosystem, not a gap in the search: Blast's entire chain-level TVL sat around $31.5M at research time, with no single protocol above $10M. Two of Blast's better-TVL protocols compounded the problem directly: their own documentation sites had gone unreachable by the time of this pass, so Blast's single largest DEX by TVL could not be sourced to this research's primary-source standard at all and was dropped rather than sourced secondhand.

<details>
<summary>Show all 2 cases</summary>

| Protocol | What was found | Already tracked as |
|---|---|---|
| API3, manager multisig | Same literal address, identical 8 owners, even though API3's own public deployment registry does not (yet) list a Blast deployment | Part 1 + Part 2 + Part 3 |
| Overnight Finance, OvnAgent | Identical 5-owner set already tracked as Overnight Finance's OvnAgent on Optimism and Base; Overnight Finance was already inside this research's roster and only recognized as such at the cross-reference step here | Part 2 |

</details>

The other 4 protocols tested on Blast produced no usable Safe: two real contracts (ZeroLend's and Overnight Finance's own separate Blast Timelock-style contracts, distinct from the OvnAgent Safe above) whose admin-recovery calls revert outright, one candidate address with no deployed bytecode at all (a genuine negative rather than a gap), and Mangrove's own core contract, whose docs mark the Blast deployment "deprecated."

#### Sonic

Sonic (formerly Fantom, migrated to a new token and rebranded) produced a more fragmented but still-active haul, about $16 to 30M in TVL spread across a longer tail of protocols.

<details>
<summary>Show all 5 cases</summary>

| Protocol | What was found | Already tracked as |
|---|---|---|
| Aave V3, GOVERNANCE_GUARDIAN | Identical 9-owner set, a Sonic-specific Safe address; also confirmed identical on Mantle the same day | Part 2 + Part 3 |
| API3, manager multisig | Same literal address, identical 8 owners | Part 1 + Part 2 + Part 3 |
| Beefy Finance, dev + treasury multisig | Same literal Safe addresses as Berachain, identical 6 and 7 owners | Part 1 + Part 2 + Part 3 |
| 1inch, Router V6 owner | Identical 5-owner set already shared across mainnet, 3 Superchain chains, Arbitrum, Polygon, BNB Chain, Avalanche, and Linea | Part 1 + Part 2 + Part 3 |
| Chainlink Data Feeds, ETH/USD owner | Identical 9-owner set already tracked on Polygon, 4 Superchain chains, and Arbitrum | Part 2 + Part 3 |

</details>

Two new real Safes never seen before in this research were also confirmed on Sonic with no overlap onto the existing roster: **Shadow Exchange** (the only protocol in this batch to publish its multisig address directly rather than needing an `owner()` derivation, 4 signers) and **SwapX** (its AlgebraFactory owner, 6 signers). Pendle Finance's governanceProxy and Silo Finance's SiloFactory owner produced the same two negative results already recorded for them on Mantle above.

### Caveats

- This is a first, wide pass sized to cover ground quickly rather than to be exhaustive on any single chain: 4 to 20 protocols per chain, against Part 2's 105. The high hit rate (66 of the first 94) is concentrated in protocols this research already had reason to check closely, since they were chosen partly because a prior overlap made a repeat plausible; a broader, protocol-agnostic pass on any one of these chains might find a different ratio.
- An on-chain event replay covers all 11 of Part 3's tracked chains (full raw-logs coverage, unlike Part 2's partial coverage). Within Part 3 alone it finds one cross-protocol signer overlap, Kelp DAO / Stader Labs (see Method above); every other Part 3 signal is cross-Part or cross-chain. It has not yet been re-run for the 8 Safes added on 2026-09-30, which are confirmed by direct on-chain reads.
- Radiant Capital's BNB Chain PoolAdmin finding is a partial signer match (7 of 11), not a full identical set: read it as "shares most of its signers with," not "is the same Safe as."
- API3's manager multisig address is chain-invariant and was tested directly via `getOwners()` on zkSync Era, Berachain, and Blast specifically, since API3's own deployment registry does not list a folder for any of the three; the address still resolves to a real, matching Safe (fully on Berachain and Blast, partially on zkSync Era), a slightly different sourcing standard than the other chains, where an explicit per-chain deployment file exists.
- Mantle, Blast, and Sonic are second-tier chains (see above for why); Blast in particular is a genuinely weak, low-signal result (see Blast section) rather than forced to look comparable to Mantle or Sonic.
- Silo Finance's SiloFactory owner resolving to a bare externally-owned address on Mantle and Sonic is a genuine per-chain finding, not a claim about Silo's security posture generally (see Mantle section above).
- Several of the Safe addresses used across Part 3 were derived by a second on-chain call (`owner()`, or a role-specific getter) rather than read directly from a published multisig list; each derivation is individually logged and cross-checked before use.

### Verification

119 hypotheses across the 11 chain-scoped registries as of 2026-09-18, all at High confidence, same discipline as Part 1; the 2026-09-30 pass added 4 more plus the Camelot reconciliation note above.

### Status

Last verified: 2026-09-30, except the 11 protocols added on 2026-10-05 (read on that date) and every line marked "re-read on 2026-11-02" (read on that date).

109 protocols across 11 chains: a pilot on Arbitrum (12 protocols), a same-day pass across seven more chains (48 protocols), a follow-up pass across three more second-tier chains (26 protocols), two follow-up rounds each adding one more protocol on Arbitrum (Morpho Blue, then Lido's Emergency Brakes), a 2026-09-18 pass adding 6 new protocols across all 11 chains (LI.FI, Kelp DAO rsETH, Stader Labs, Euler V2, Balancer, Threshold Network/tBTC) plus a Pendle correction, a 2026-09-30 pass adding 4 protocols on Arbitrum (Arbitrum Security Council, Frax Finance, Yearn, Ethena), and a 2026-10-05 pass adding 11 protocols on Arbitrum (dHEDGE, CoW Protocol, API3, Hyperlane, Puffer, Synapse, Spark Liquidity Layer, USDT0, Odos, Premia, deBridge). Not a finished survey on any of the 11; live event-replay verification now exists for this part (see Caveats above).

Everything stated is held to the confidence level the on-chain data actually supports.
