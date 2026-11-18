## Part 1: Mainnet

### Method

214 protocols' multisig contracts (Gnosis Safe) checked directly on-chain: 395 candidate addresses tested, 328 confirmed as real Safe contracts. Scope grew from an original 41-protocol pilot to 214 protocols across 33 research updates, each adding several more protocols and re-running the full cross-reference against every signer already on record.

### Findings

8 addresses hold signer power on 2+ independent protocols, sorted by how many protocols each one touches. Every seat was checked against the protocols' own public signer disclosures; the named mapping is not published here. 7 of the 8 match such a disclosure; for the eighth, no public source was found:

| Rank | Key | Protocols | Reach |
|---|---|---|---|
| 1 | **Key A** | Abracadabra + Yearn + Prisma + Threshold Network + Usual Money | 5 protocols *(re-read on 2026-11-02: one of Usual Money's 15 signers was replaced between 15 and 31 October 2026; the signer who left is not one of the keys counted here)* |
| 1 | **Key B** | Convex + Prisma + Votium + Curve Finance's own Emergency DAO + Resupply | 5 protocols *(re-read on 2026-11-02: two of the nine owners of Curve's Emergency DAO were replaced between 15 and 31 October 2026; Key B is not one of the two who left, and the two who joined are already tracked signers of other protocols, not yet assessed against the keys in this table)* |
| 3 | **Key C** | Frax + Prisma + Fraxtal's L1 chain-governance Safe | 3 protocols |
| 3 | **Key D** (the Gearbox / TokenLogic signer) | Gearbox + TokenLogic's own Safe, incl. 1 of GHO Stablecoin's role Safes | 3 protocols |
| 5 | **Key E** | Lido + Balancer | 2 protocols |
| 5 | **Key F** | Angle + Morpho | 2 protocols |
| 5 | **Key G** | Abracadabra + StakeDAO | 2 protocols |
| 5 | **Key H** | Votium + Convex | 2 protocols |

Keys A and B each touch 5 independent protocols at once, the widest mainnet reach in this research. In structural terms, one signer key here counts toward the signing threshold of five protocols' multisigs at the same time.

The 2026-09-11 update (scope grew 132→171 protocols) surfaced two reach increases among the original 8, both newly-tracked protocols rather than a change in who holds which key: Key C is also a signer on Fraxtal's own L1 chain-governance Safe (ProxyAdminOwner), and the Gearbox / TokenLogic signer's address now also sits directly on one of GHO Stablecoin's role-specific Safes, its own TokenLogic entity Safe (`0x9DE1d45e2786b03498289959203F25b29B4D1193`), confirmed via a fresh `getOwners()` call on 2026-09-14; that same TokenLogic entity Safe is, in turn, one of three entity-Safes (alongside AaveLabs' and LlamaRisk's) that jointly own GHO's RiskCouncil Safe, so its reach touches RiskCouncil only indirectly through that nested Safe, not as a direct on-chain owner of it.

Three of the eight (Keys A, B and C) sit together on Prisma Finance's emergency multisig, a deliberate, publicly disclosed design choice by Prisma to seat signers from other established protocols for credibility, not a hidden concentration. The other five are more organic; one of them (Key H, Votium and Convex) is an expected link, since Votium is built around Convex, and the rest have no obvious institutional link to each other.

Key D, the Gearbox / TokenLogic signer, reappears in Part 2: the same address also sits on three of Aave's Superchain Safes across Ink and Celo. See Part 2 below for the full cross-chain picture.

A 2026-09-11 same-day follow-up added three new mainnet protocols, none adding a new identified signer, two of them with a new pseudonymous signer-overlap case:

| Protocol | What was found |
|---|---|
| **Spiko** (RWA tokenized money-market funds) | New protocol added to scope, no overlap case yet attached |
| **DeFiSaver** (DeFi position automation) | Its admin signer is also one of Aave's own official Governance Guardian signers |
| **Veda** (fka Se7en Seas, the BoringVault infrastructure operator behind ether.fi's Liquid vaults and others) | Two vault-governance signers are also EtherFi and LombardFinance signers respectively, 2 of 5 signers shared on the Lombard case |

A 2026-09-13 addition covers Gnosis Chain's canonical bridges: the 8-of-15 Bridge Governor Safe that is both the upgrade owner and the admin owner of the xDai Bridge and the OmniBridge on Ethereum (~$271M TVL). No new mainnet-internal overlap, but one of its 15 owners is aavechan.eth, already tracked below on QiDao/Mai Finance and Aave Safes, now confirmed on a third independent protocol; [Gnosis Chain's own docs](https://docs.gnosischain.com/bridges/management) list the Aave-Chan Initiative as one of the 15 governor organizations, so the seat is disclosed, the cross-protocol aggregation is what's new.

Two later additions round out the rollup coverage: Taiko Alethia's `admin.taiko.eth` Safe (4-of-6, added 2026-09-16) and Hop Protocol's L1 bridge-governance Safe (2-of-3). Neither shares a signer with any other tracked protocol.

The 2026-09-19 update added 18 protocols, mostly the teams that curate lending vaults on Morpho and Euler. Their addresses come from the two protocols' own official curator registries, and every Safe and vault role was confirmed on-chain.

| Protocol | What was found |
|---|---|
| **Gauntlet, RockawayX, Armitage by Wintermute, Clearstar, Hakutora, Hyperithm, KPK, MEV Capital, SwissBorg, Re7 Labs** (vault curators) | Real multisigs (2-of-3 up to 5-of-8), no signer shared with any other tracked protocol *(re-read on 2026-11-02: the same new signer was added to each of Gauntlet's three Safes between 15 and 31 October 2026, replacing a former signer on two of them; the new signer is not in the registry of tracked signers, so the statement above still holds for the protocols tracked here)* |
| **Steakhouse Financial + Waterline** | As of 2026-10-14 (Ethereum block 26,192,397), the two brands' owner Safes have identical signer sets (10 addresses, threshold 5), and so do their curator Safes (9 addresses, threshold 3): 19 addresses in total, none specific to one brand. On 2026-09-19 the two brands already shared all of their 10 signers. Both brands then rotated their signers (2026-09-28 and 2026-10-07), and each rotation was signed by keys already among those 10. On-chain, the two brands are controlled by the same keys, so they are not two independent curators. That points to one operator, but identical keys can also come from a shared signing or custody provider, so the chain alone does not show a single organization. |
| **Avantgarde** | One vault-owner signer also sits on Enzyme's Dispatcher owner Safe. Avantgarde is the company that builds Enzyme, so the link is disclosed staff, not a hidden concentration |
| **Sentora** | Not a shared-signer finding, so no figure is kept here. The owner and curator of its two main Morpho vaults are each a 1-of-1 Safe held by a single wallet: a single-key case, described with its vault size and date in the [defi-admin-key-risk showcase](https://github.com/RealSpap/defi-admin-key-risk-showcase#sentora-a-1-of-1-safe-at-the-750m-scale) |
| **Boba Network, ZeroLend, Swaap, Keyring** | New to mainnet scope (Boba's L1 upgrade key, the others' Euler-listed Safes), no overlap found |

The L1 governance Safes of World Chain, Celo, BOB, Soneium, Mode and Zora were checked in the same pass but are already covered in Part 2, so they are not counted twice here.

The 2026-10-01 update added 10 protocols outside lending: token issuers, bridges and shared infrastructure. Each Safe was read on two independent public RPCs, and each role was confirmed by calling the protocol contract's own `owner()` or `admin()` getter.

| Protocol | What was found |
|---|---|
| **Safe** (issuer of the SAFE governance token) | The SAFE token owner is a 3-of-5 Safe. One of its signers is also a signer of Balancer's DAO Multisig (6-of-11). No public disclosure linking the two seats was found yet, so the overlap is recorded, not qualified |
| **Succinct** (SP1 proof verifier gateways, PLONK and Groth16) | Both gateways are owned by a 2-of-3 Safe. One of its 3 signers also sits on Aave's Community Multisig and EigenLayer's Community Multisig, so this key now reaches 3 protocols. Context not yet established |
| **Sablier** (token streaming) | The admin of the V2 LockupLinear contract is a Safe at threshold 1 of 4: any one of its four signers can act as admin alone. No signer shared with another tracked protocol |
| **Function FBTC, pumpBTC, Stables Labs USDX, Ronin Bridge (Ethereum side), LooksRare, ApeCoin staking, Sonic Gateway** | Real multisigs from 2-of-3 up to 5-of-8, no signer shared with any other tracked protocol. The Ronin Bridge gateway is upgraded through a two-level proxy chain that ends at a 3-of-5 Safe |

The same update re-read 5 protocols already in scope (Balancer, Puffer, Ethena, SushiSwap, Stargate). All published overlaps reproduced unchanged. One note was added for Ethena: its USDe distributor Safe (4-of-10) shares 6 of its 10 signers with the two Ethena Safes that already carry an identical 10-signer set. This is a link inside one team, not a cross-protocol one.

Aave's own Governance Guardian Safe, already tracked cross-chain in Part 2 and Part 3, was added to this mainnet scope for the first time in that update, so the DeFiSaver overlap is covered by the on-chain event replay, not only by the hand-documented registry.

Beyond the 8 cross-protocol signers, this research has surfaced 48 more shared-infrastructure or signer-overlap cases on mainnet, each individually documented in the registry, most of which turn out to be Safes already tracked in Part 2 or Part 3 resolving identically on Ethereum too.

**The 2026-10-06 update added 10 chain-governance Safes.** These are the Ethereum-side owners (ProxyAdminOwner) of ten more OP Stack chains, taken from the Optimism Superchain registry and read directly on-chain on three public RPCs: HashKey (3-of-5), Mint (2-of-3), Xterio (3-of-4), Silent Data (2-of-5), Redstone (2-of-3), Cyber (3-of-4), Automata (3-of-4), Swan (3-of-4), Funki (3-of-4) and RACE (3-of-5). Chains already covered in Part 2 were not added again. One new overlap came out of the cross-reference between these ten entries themselves: the Safes of Xterio, Cyber, Automata and Funki (3-of-4 each) have three signers in common. Who operates those keys is not established; a rollup provider serving the four chains is plausible but not confirmed. These are chain governances rather than independent protocols, which is why the three signers are not counted in the figure of 8 above.

**Two more overlaps came from the Curve Emergency DAO rotation (first read on 2026-11-02, read at 16:15Z on 13 November 2026).** Between 15 and 31 October 2026 two of the nine owners of Curve's Emergency DAO Safe were replaced. Both signers who joined already sign for other tracked protocols, and both are externally owned addresses (no contract code on Ethereum mainnet, chain id 1): `0xBd0a74e5...` is also an owner of the Convex multisig and of the Resupply main multisig, and `0x4046B37F...` is also an owner of the StakeDAO treasury Safe on Ethereum. An address does not say who holds it, so whether one person holds either key cannot be read from the chain, and no key label is assigned. Neither signer is counted in the figure of 8 above, which counts the signers found before this rotation. Both overlaps are replayable: see [FACTS.md](../FACTS.md) and `python3 scripts/prove.py`.

### Live verification

An on-chain event replay rebuilds the current owner set of every Safe tracked in the 194-protocol scope from its event history, independently of the direct `getOwners()` reads. It has not yet been re-run for the 20 Safes added on 2026-10-01 and 2026-10-06, which rest on direct reads from two RPCs for now. Two seats (Key G's second seat and Key B's Convex seat) don't reproduce through live event replay, because they sit on Safe versions old enough their creation transactions don't log the data a pure event-based rebuild needs; both are confirmed instead by a direct `getOwners()` read, independently cross-checked against the relevant transaction logs on Etherscan.

**Get notified**: see [Get notified](about.md#get-notified).

### What's checked next (Mainnet)

214 protocols is a growing survey, not a finished one. Open a GitHub Issue on this repo to suggest the next protocol to check; a thumbs-up on an existing suggestion counts as a vote (this sets research priority only; checks are still run with the same private tooling, not opened to contributors). The Superchain-specific follow-up covers 105 more protocols, and a third extension covers 109 more across Arbitrum and 10 other L2s and sidechains: see Part 2 and Part 3 below.

### Verification

Every claim in this research follows the same verification discipline described in [Methodology at a glance](method.md#methodology-at-a-glance) above. The mainnet registry holds 57 finding rows: the 8 cross-protocol signers, 1 correction (see Caveats below), and 48 shared-infrastructure or signer-overlap cases. Of the 9 hand-researched rows (the 8 signers plus the correction), all 9 are at High confidence (one of them was upgraded from Medium on 2026-09-13, once a primary source corroborated it); the 48 shared-infrastructure cases are all independently sourced and at High confidence too, and are re-confirmed by the on-chain event replay. Since 2026-09-19 the registry also carries one verification row per newly added protocol (18 rows on 2026-09-19, 10 on 2026-10-01), plus one note from the 2026-10-01 re-read (86 rows in total). Each points to its on-chain evidence; two of the 2026-10-01 rows are at Medium confidence because the contract address comes from a block-explorer label rather than the protocol's own documentation.

### Status

Last verified: 2026-10-01, except the Steakhouse Financial + Waterline overlap and signer `0x9A73D57B...` (read on 2026-10-14), the count of 214 entries (2026-10-06) and every line marked "re-read on 2026-11-02" (read on that date).

214 protocols checked, not a finished survey. Scope has grown from an original 41-protocol pilot across 33 research updates, each one adding new protocols, resolving a previously parked case, or re-running the full cross-reference against every signer already on record.

### Caveats (Mainnet)

- Two seats (Key G's second seat and Key B's Convex seat) don't reproduce through live event replay, because they sit on Safe versions old enough that their creation transactions don't log the data a pure event-based rebuild needs; both are confirmed by a direct `getOwners()` read instead. See Live verification above.
- 214 protocols is a growing survey, not a finished one (see What's checked next). A protocol not listed here hasn't been checked, not confirmed clean.
- Three of the eight cross-protocol signers (Keys A, B and C) sit together on Prisma Finance's multisig by Prisma's own deliberate, publicly disclosed design choice to seat signers from other established protocols for credibility, not a hidden concentration; treating that case the same as the other five (one of which, Key H on Votium and Convex, is also an expected link) would overstate how coordinated the overlap actually is.
- One candidate address needed a correction after a separate on-chain check. Ethena's `Owner_Multisig_3of11` is a real, confirmed 10-signer Safe, but that check found it does not match the actual `owner()` of either EthenaMinting V2 or the USDe token (both a 24-hour Timelock instead), nor EthenaMinting V1's actual owner (a separate 5-of-10 Safe). The Safe is real; what it currently controls at Ethena, if anything, is unconfirmed.
