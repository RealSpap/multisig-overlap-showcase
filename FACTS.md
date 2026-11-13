# Public facts

Generated from facts/public-facts.json with python3 scripts/prove.py --write-facts-md. Each fact has six fields: the claim, the network with its chain id, a named block, the replay command, an expiry date and whether it was read.

A fact is a statement about addresses on one network at one block. It stays true only until one of its owners or its threshold changes. After its expiry date it is not vouched for until it is read again. The full owner lists are in facts/public-facts.json.

## curve-emergency-dao-ethereum

- Claim: Curve Finance Emergency DAO Safe (the address listed in Part 1) on Ethereum mainnet: threshold 5 of 9 owners.
- Address: `0x467947ee34af926cf1dcac093870f613c96b1e0c` on Ethereum mainnet (chain id 1)
- Block: number 26407129 on Ethereum mainnet (chain id 1), hash `0x1b2102bc30cd68103d334c09717776110fd1cea19305b4dcd55a85b0628e9d97`, 2026-11-13T16:06:35Z
- Read: yes, read at 16:08Z on 13 November 2026, 2 public RPC endpoints, identical answers, read 2026-11-13T16:08:58Z
- Expires: 2026-11-27
- Replay: `python3 scripts/prove.py --fact curve-emergency-dao-ethereum`
- Same read with cast on Ethereum mainnet (chain id 1): `cast call 0x467947ee34af926cf1dcac093870f613c96b1e0c "getThreshold()(uint256)" --rpc-url https://ethereum-rpc.publicnode.com --block 26407129 ; cast call 0x467947ee34af926cf1dcac093870f613c96b1e0c "getOwners()(address[])" --rpc-url https://ethereum-rpc.publicnode.com --block 26407129`

## curve-emergency-dao-same-address-ethereum

- Claim: Curve Finance Emergency DAO Safe at the address it has on the other chains on Ethereum mainnet: threshold 5 of 9 owners.
- Address: `0x6d447e544d01a59cb0774763bf15526574cfffed` on Ethereum mainnet (chain id 1)
- Block: number 26407129 on Ethereum mainnet (chain id 1), hash `0x1b2102bc30cd68103d334c09717776110fd1cea19305b4dcd55a85b0628e9d97`, 2026-11-13T16:06:35Z
- Read: yes, read at 16:08Z on 13 November 2026, 2 public RPC endpoints, identical answers, read 2026-11-13T16:08:58Z
- Expires: 2026-11-27
- Replay: `python3 scripts/prove.py --fact curve-emergency-dao-same-address-ethereum`
- Same read with cast on Ethereum mainnet (chain id 1): `cast call 0x6d447e544d01a59cb0774763bf15526574cfffed "getThreshold()(uint256)" --rpc-url https://ethereum-rpc.publicnode.com --block 26407129 ; cast call 0x6d447e544d01a59cb0774763bf15526574cfffed "getOwners()(address[])" --rpc-url https://ethereum-rpc.publicnode.com --block 26407129`

## convex-multisig-ethereum

- Claim: Convex Finance multisig on Ethereum mainnet: threshold 3 of 5 owners.
- Address: `0xa3c5a1e09150b75ff251c1a7815a07182c3de2fb` on Ethereum mainnet (chain id 1)
- Block: number 26407129 on Ethereum mainnet (chain id 1), hash `0x1b2102bc30cd68103d334c09717776110fd1cea19305b4dcd55a85b0628e9d97`, 2026-11-13T16:06:35Z
- Read: yes, read at 16:08Z on 13 November 2026, 2 public RPC endpoints, identical answers, read 2026-11-13T16:08:58Z
- Expires: 2026-11-27
- Replay: `python3 scripts/prove.py --fact convex-multisig-ethereum`
- Same read with cast on Ethereum mainnet (chain id 1): `cast call 0xa3c5a1e09150b75ff251c1a7815a07182c3de2fb "getThreshold()(uint256)" --rpc-url https://ethereum-rpc.publicnode.com --block 26407129 ; cast call 0xa3c5a1e09150b75ff251c1a7815a07182c3de2fb "getOwners()(address[])" --rpc-url https://ethereum-rpc.publicnode.com --block 26407129`

## resupply-main-multisig-ethereum

- Claim: Resupply main multisig on Ethereum mainnet: threshold 3 of 5 owners.
- Address: `0xfe11a5009f2121622271e7dd0fd470264e076af6` on Ethereum mainnet (chain id 1)
- Block: number 26407129 on Ethereum mainnet (chain id 1), hash `0x1b2102bc30cd68103d334c09717776110fd1cea19305b4dcd55a85b0628e9d97`, 2026-11-13T16:06:35Z
- Read: yes, read at 16:08Z on 13 November 2026, 2 public RPC endpoints, identical answers, read 2026-11-13T16:08:58Z
- Expires: 2026-11-27
- Replay: `python3 scripts/prove.py --fact resupply-main-multisig-ethereum`
- Same read with cast on Ethereum mainnet (chain id 1): `cast call 0xfe11a5009f2121622271e7dd0fd470264e076af6 "getThreshold()(uint256)" --rpc-url https://ethereum-rpc.publicnode.com --block 26407129 ; cast call 0xfe11a5009f2121622271e7dd0fd470264e076af6 "getOwners()(address[])" --rpc-url https://ethereum-rpc.publicnode.com --block 26407129`

## stakedao-treasury-ethereum

- Claim: StakeDAO treasury Safe on Ethereum on Ethereum mainnet: threshold 3 of 5 owners.
- Address: `0xf930ebbd05ef8b25b1797b9b2109ddc9b0d43063` on Ethereum mainnet (chain id 1)
- Block: number 26407129 on Ethereum mainnet (chain id 1), hash `0x1b2102bc30cd68103d334c09717776110fd1cea19305b4dcd55a85b0628e9d97`, 2026-11-13T16:06:35Z
- Read: yes, read at 16:08Z on 13 November 2026, 2 public RPC endpoints, identical answers, read 2026-11-13T16:08:58Z
- Expires: 2026-11-27
- Replay: `python3 scripts/prove.py --fact stakedao-treasury-ethereum`
- Same read with cast on Ethereum mainnet (chain id 1): `cast call 0xf930ebbd05ef8b25b1797b9b2109ddc9b0d43063 "getThreshold()(uint256)" --rpc-url https://ethereum-rpc.publicnode.com --block 26407129 ; cast call 0xf930ebbd05ef8b25b1797b9b2109ddc9b0d43063 "getOwners()(address[])" --rpc-url https://ethereum-rpc.publicnode.com --block 26407129`

## curve-emergency-dao-optimism

- Claim: Curve Finance Emergency DAO Safe on Optimism: threshold 5 of 9 owners.
- Address: `0x6d447e544d01a59cb0774763bf15526574cfffed` on Optimism (chain id 10)
- Block: number 159493668 on Optimism (chain id 10), hash `0xc345f224bd2ff4f1b796f21381c1c523a8af14631553a16c0a35f487c07a4ef0`, 2026-11-13T16:08:33Z
- Read: yes, read at 16:08Z on 13 November 2026, 2 public RPC endpoints, identical answers, read 2026-11-13T16:08:58Z
- Expires: 2026-11-27
- Replay: `python3 scripts/prove.py --fact curve-emergency-dao-optimism`
- Same read with cast on Optimism (chain id 10): `cast call 0x6d447e544d01a59cb0774763bf15526574cfffed "getThreshold()(uint256)" --rpc-url https://mainnet.optimism.io --block 159493668 ; cast call 0x6d447e544d01a59cb0774763bf15526574cfffed "getOwners()(address[])" --rpc-url https://mainnet.optimism.io --block 159493668`

## sablier-comptroller-admin-optimism

- Claim: Sablier Comptroller admin Safe (a single signer can act) on Optimism: threshold 1 of 4 owners.
- Address: `0x58290bbdb51a4c6b022a81e9cded24be19ca57fd` on Optimism (chain id 10)
- Block: number 159493668 on Optimism (chain id 10), hash `0xc345f224bd2ff4f1b796f21381c1c523a8af14631553a16c0a35f487c07a4ef0`, 2026-11-13T16:08:33Z
- Read: yes, read at 16:08Z on 13 November 2026, 2 public RPC endpoints, identical answers, read 2026-11-13T16:08:58Z
- Expires: 2026-11-27
- Replay: `python3 scripts/prove.py --fact sablier-comptroller-admin-optimism`
- Same read with cast on Optimism (chain id 10): `cast call 0x58290bbdb51a4c6b022a81e9cded24be19ca57fd "getThreshold()(uint256)" --rpc-url https://mainnet.optimism.io --block 159493668 ; cast call 0x58290bbdb51a4c6b022a81e9cded24be19ca57fd "getOwners()(address[])" --rpc-url https://mainnet.optimism.io --block 159493668`

## curve-emergency-dao-base

- Claim: Curve Finance Emergency DAO Safe on Base: threshold 5 of 9 owners.
- Address: `0x6d447e544d01a59cb0774763bf15526574cfffed` on Base (chain id 8453)
- Block: number 56978784 on Base (chain id 8453), hash `0xc0c60ff34e28fffeaa47077eb838e27677e8119f80f1fe6ef2291b735f8571c3`, 2026-11-13T16:08:52Z
- Read: yes, read at 16:08Z on 13 November 2026, 2 public RPC endpoints, identical answers, read 2026-11-13T16:08:58Z
- Expires: 2026-11-27
- Replay: `python3 scripts/prove.py --fact curve-emergency-dao-base`
- Same read with cast on Base (chain id 8453): `cast call 0x6d447e544d01a59cb0774763bf15526574cfffed "getThreshold()(uint256)" --rpc-url https://mainnet.base.org --block 56978784 ; cast call 0x6d447e544d01a59cb0774763bf15526574cfffed "getOwners()(address[])" --rpc-url https://mainnet.base.org --block 56978784`

## sablier-comptroller-admin-base

- Claim: Sablier Comptroller admin Safe on Base: threshold 2 of 4 owners.
- Address: `0x58290bbdb51a4c6b022a81e9cded24be19ca57fd` on Base (chain id 8453)
- Block: number 56978784 on Base (chain id 8453), hash `0xc0c60ff34e28fffeaa47077eb838e27677e8119f80f1fe6ef2291b735f8571c3`, 2026-11-13T16:08:52Z
- Read: yes, read at 16:08Z on 13 November 2026, 2 public RPC endpoints, identical answers, read 2026-11-13T16:08:58Z
- Expires: 2026-11-27
- Replay: `python3 scripts/prove.py --fact sablier-comptroller-admin-base`
- Same read with cast on Base (chain id 8453): `cast call 0x58290bbdb51a4c6b022a81e9cded24be19ca57fd "getThreshold()(uint256)" --rpc-url https://mainnet.base.org --block 56978784 ; cast call 0x58290bbdb51a4c6b022a81e9cded24be19ca57fd "getOwners()(address[])" --rpc-url https://mainnet.base.org --block 56978784`

## curve-emergency-dao-arbitrum

- Claim: Curve Finance Emergency DAO Safe on Arbitrum One: threshold 5 of 9 owners.
- Address: `0x6d447e544d01a59cb0774763bf15526574cfffed` on Arbitrum One (chain id 42161)
- Block: number 523911969 on Arbitrum One (chain id 42161), hash `0x131faf937f3d89eec2fe3811ab8c6eb6fbe87d482f4ab234c4cae296de9c5ab4`, 2026-11-13T16:08:52Z
- Read: yes, read at 16:08Z on 13 November 2026, 2 public RPC endpoints, identical answers, read 2026-11-13T16:08:58Z
- Expires: 2026-11-27
- Replay: `python3 scripts/prove.py --fact curve-emergency-dao-arbitrum`
- Same read with cast on Arbitrum One (chain id 42161): `cast call 0x6d447e544d01a59cb0774763bf15526574cfffed "getThreshold()(uint256)" --rpc-url https://arb1.arbitrum.io/rpc --block 523911969 ; cast call 0x6d447e544d01a59cb0774763bf15526574cfffed "getOwners()(address[])" --rpc-url https://arb1.arbitrum.io/rpc --block 523911969`

## odos-router-owner-arbitrum

- Claim: Odos Router V3 owner Safe (a single signer acts alone) on Arbitrum One: threshold 1 of 6 owners.
- Address: `0x498292dc123f19bdbc109081f6cf1d0e849a9daf` on Arbitrum One (chain id 42161)
- Block: number 523911969 on Arbitrum One (chain id 42161), hash `0x131faf937f3d89eec2fe3811ab8c6eb6fbe87d482f4ab234c4cae296de9c5ab4`, 2026-11-13T16:08:52Z
- Read: yes, read at 16:08Z on 13 November 2026, 2 public RPC endpoints, identical answers, read 2026-11-13T16:08:58Z
- Expires: 2026-11-27
- Replay: `python3 scripts/prove.py --fact odos-router-owner-arbitrum`
- Same read with cast on Arbitrum One (chain id 42161): `cast call 0x498292dc123f19bdbc109081f6cf1d0e849a9daf "getThreshold()(uint256)" --rpc-url https://arb1.arbitrum.io/rpc --block 523911969 ; cast call 0x498292dc123f19bdbc109081f6cf1d0e849a9daf "getOwners()(address[])" --rpc-url https://arb1.arbitrum.io/rpc --block 523911969`

## Signers shared by several Safes

- signer-0xbd0a74e5-curve-convex-resupply: One externally owned address is an owner of the Curve Emergency DAO Safe, the Convex multisig and the Resupply main multisig on Ethereum mainnet. Signer `0xbd0a74e51729a4d0b92742e67183c4cbc97bca92` on Ethereum mainnet (chain id 1), Safes curve-emergency-dao-ethereum, convex-multisig-ethereum, resupply-main-multisig-ethereum, read at 16:08Z on 13 November 2026. An address does not say who holds it, so whether one person holds the key cannot be read from the chain.
- signer-0x4046b37f-curve-stakedao: One externally owned address is an owner of the Curve Emergency DAO Safe and of the StakeDAO treasury Safe on Ethereum mainnet. Signer `0x4046b37ffc36b0c723d7fc64e0c763b698d81934` on Ethereum mainnet (chain id 1), Safes curve-emergency-dao-ethereum, stakedao-treasury-ethereum, read at 16:08Z on 13 November 2026. An address does not say who holds it, so whether one person holds the key cannot be read from the chain.

