# One Safe address, the same four owners, two thresholds

*Read at 19:00Z on 2026-11-25, on Optimism (chainId 10) at block 160017196 and on Base (chainId 8453) at block 62214254. I re-read it on any day I quote it.*

## The question

A Safe is a multisig wallet. Its threshold is the number of owners who must sign before it acts. Can one Safe address, with the same owners, ask for a different number of signatures on two chains?

## What I read

The address is `0x58290bbdb51a4c6b022a81e9cded24be19ca57fd` on Optimism (chainId 10) and on Base (chainId 8453). I read it on two public nodes per chain, and both nodes gave the same answer.

- On Optimism (chainId 10) it lists four owners and its threshold is 1. One owner can act alone.
- On Base (chainId 8453) it lists the same four owners and its threshold is 2.
- On both chains no module is enabled and no guard is set (steps 6 to 9), so nothing there changes how many owners must sign.

## Limits

- One example is not a rate. It says nothing about how many other Safes look like this.
- A threshold of 1 can be a choice. I do not call the setup a fault, and I do not call it safe.
- It says nothing about other chains where the same address might exist.
- A read that fails would be unread, never zero. Here every read answered on both nodes.

## Redo it

Each line runs on the chain named in its comment. I read each chain on two public nodes: mainnet.optimism.io and optimism-rpc.publicnode.com for Optimism, mainnet.base.org and base-rpc.publicnode.com for Base. Swap the node after `-r` for any other public node of that chain.

1. The threshold on Optimism (chainId 10). It prints `1`:

```
cast call 0x58290bbdb51a4c6b022a81e9cded24be19ca57fd "getThreshold()(uint256)" --block 160017196 -r https://mainnet.optimism.io # Optimism, chainId 10
```

2. The threshold on Base (chainId 8453). It prints `2`:

```
cast call 0x58290bbdb51a4c6b022a81e9cded24be19ca57fd "getThreshold()(uint256)" --block 62214254 -r https://mainnet.base.org # Base, chainId 8453
```

3. The owners on Optimism (chainId 10), as one hash:

```
cast call 0x58290bbdb51a4c6b022a81e9cded24be19ca57fd "getOwners()(address[])" --block 160017196 -r https://mainnet.optimism.io | shasum # Optimism, chainId 10
```

4. The owners on Base (chainId 8453), as one hash. It prints the same hash as step 3, so the owners are the same:

```
cast call 0x58290bbdb51a4c6b022a81e9cded24be19ca57fd "getOwners()(address[])" --block 62214254 -r https://mainnet.base.org | shasum # Base, chainId 8453
```

5. The number of owners on Optimism (chainId 10). It prints `4`:

```
cast call 0x58290bbdb51a4c6b022a81e9cded24be19ca57fd "getOwners()(address[])" --block 160017196 -r https://mainnet.optimism.io | tr ',' '\n' | wc -l # Optimism, chainId 10
```

6. The modules on Optimism (chainId 10). The first line is `[]`, an empty list:

```
cast call 0x58290bbdb51a4c6b022a81e9cded24be19ca57fd "getModulesPaginated(address,uint256)(address[],address)" 0x0000000000000000000000000000000000000001 10 --block 160017196 -r https://mainnet.optimism.io # Optimism, chainId 10
```

7. The modules on Base (chainId 8453). The first line is `[]`:

```
cast call 0x58290bbdb51a4c6b022a81e9cded24be19ca57fd "getModulesPaginated(address,uint256)(address[],address)" 0x0000000000000000000000000000000000000001 10 --block 62214254 -r https://mainnet.base.org # Base, chainId 8453
```

8. The guard on Optimism (chainId 10). It prints 32 bytes of zeros, so no guard is set:

```
cast storage 0x58290bbdb51a4c6b022a81e9cded24be19ca57fd 0x4a204f620c8c5ccdca3fd54d003badd85ba500436a431f0cbda4f558c93c34c8 --block 160017196 -r https://mainnet.optimism.io # Optimism, chainId 10
```

9. The guard on Base (chainId 8453). It prints 32 bytes of zeros:

```
cast storage 0x58290bbdb51a4c6b022a81e9cded24be19ca57fd 0x4a204f620c8c5ccdca3fd54d003badd85ba500436a431f0cbda4f558c93c34c8 --block 62214254 -r https://mainnet.base.org # Base, chainId 8453
```
