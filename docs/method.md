# Method and vocabulary

## Methodology at a glance

Every part of this research, across all three scales below, follows the same four-step discipline:

- **Primary-source sourcing.** Every candidate address comes from a protocol's own documentation or GitHub repository first, never a third-party aggregator or press citation.
- **On-chain re-verification.** Every candidate is checked directly on-chain via `getOwners()` (or the equivalent role-specific getter): no API key, no third-party indexer, pure RPC reads against a public node for the relevant chain.
- **Cross-referencing.** Every signer recovered is checked against the full combined roster this research already has on record across all three Parts, not just within the chain or protocol just checked.
- **Falsification checks.** Every identity or cross-reference claim is logged in a falsifiable-hypothesis registry with an exact source locator, a stated falsification test, and a confidence level, then checked against its cited source before publication.

Each Part's own Method section below states only what's specific to that Part: how many protocols and chains, and any edge cases this general method doesn't cover.

## Who this is for

Protocol governance teams sizing up their own key concentration against comparable projects. Depositors, insurers, and risk desks pricing counterparty and key-compromise risk across a portfolio of protocols. Auditors and due-diligence teams who need a starting map of shared signers before their own engagement. Teams who want the same check run on their own protocol or portfolio. Every seat was checked against the protocols' own public signer disclosures; the named mapping is not published here. Every address-level finding can be re-checked on-chain, not taken on faith.

**Protocols referenced include:** Aave, Curve Finance, Compound III, Lido, Balancer, Yearn, Convex, Morpho Blue, Frax Finance, Chainlink Data Feeds, 1inch, and Beefy Finance.

**Confidence & match vocabulary:**
- **Key A, Key B...**: a signer key held by a person, shown under a neutral, stable label. No individual is named in this report; only organizations and companies are.
- **Confirmed**: a primary-source citation (a protocol's own docs, GitHub, or governance forum post) ties that specific address to its holder.
- **High confidence**: strong circumstantial evidence (role, context, or a single indirect signal) rather than a direct address citation, flagged inline wherever it applies.
- **Pseudonymous**: the address recurs across protocols but no primary source ties it to a holder, so it's reported at address level only.
- **Identical signer set**: two Safe contracts at different addresses share the exact same list of owner addresses.
- **Same literal Safe address**: the identical contract address is deployed and live on more than one chain.
- **Partial overlap**: only some signers are shared between two Safes, not the full set.
