# Tracked Safes with a module

*Read at 19:00Z on 2026-11-25, pinned to block 26494063 on Ethereum mainnet (chainId 1). I re-read it on any day I quote it.*

## The question

A Safe is a multisig wallet. Its owners can enable a module: a contract that may move the Safe's funds without any owner signing. How many of the Safes I follow have one?

## The set

The set is the 223 Safe addresses in [`facts/tracked-safes.tsv`](../facts/tracked-safes.tsv), all on Ethereum mainnet, chainId 1. They come from the Safes I look at in this research, and I left some of those out of the list for reasons I do not give here. It is not a census of Ethereum and not a sample drawn from it, so the numbers below are counts on this list only. They are not a rate, and they say nothing about Safes outside it, including the ones I left out.

## What I read

At block 26494063 on Ethereum mainnet, chainId 1, with public nodes taking turns (four of them at the head, the three that serve old state when you name a block):

- 222 of the 223 Safes read, 1 unread: the contract refuses the module call, so I know nothing about its modules.
- 23 of the 222 Safes read have at least one module enabled, 21 distinct modules in all.
- The script also prints a count of Roles-type modules. I do not quote it for this list, because the Safes I left out change it. I call a module Roles-type when its code, or the code behind it if it is a plain EIP-1167 clone, contains the selector of `execTransactionWithRole` or `execTransactionWithRoleReturnData`. That says what the code can do. It does not say which project wrote it, how its roles are set, or whether it is safe.
- I read the kind of every module that those 23 Safes list.

The script in "Redo it" prints these same figures and nothing else.

## Limits

- A read that fails is unread, never zero. If a node refuses or answers in a shape I do not expect, the Safe is counted as unread.
- Roles-type is a floor. I follow EIP-1167 clones only, so a Roles module behind another proxy kind would be counted as not Roles-type.
- A module can be fine. Teams enable modules on purpose, and a count of Safes with a module is not a count of risky Safes.
- A different list gives a different count. Nothing here says how many Safes with a module exist outside this list.

## Redo it

The script is `scripts/count_modules.py`. It needs Python 3 and nothing else, and it reads only. It checks itself without a network:

```
python3 scripts/count_modules.py --selftest
```

Then it reads every Safe in the list at the block of this page. With `--block`, the default nodes are the ones that serve old state, and a node that fails is replaced by the next one. It takes a few minutes and prints the figures above.

```
python3 scripts/count_modules.py --safes facts/tracked-safes.tsv --block 26494063 --out count.json # Ethereum mainnet, chainId 1
```

Without `--block` it pins to the head it reads first, so you can check it on a block of your own. The figures change when Safes change, and the date on top says when I read them.

## Check one Safe

To read the modules of one Safe yourself, replace `SAFE` with its address. The call only reads. It runs on Ethereum mainnet (chainId 1) at the block of this page, and any public node that serves old state will do:

```
cast call SAFE "getModulesPaginated(address,uint256)(address[],address)" 0x0000000000000000000000000000000000000001 10 --block 26494063 -r https://eth.drpc.org # Ethereum mainnet, chainId 1
```

It prints the modules enabled on that Safe, ten at most, and the next address in the list. An empty list means no module. An error means the module call is refused, which is what happens for the one Safe on my list that I count as unread. A refusal is not an empty list. An error also comes back for a Safe on another chain, or one created after this block. Remove the `--block` option to read a Safe as it is today.

## One transaction I mention

On Ethereum mainnet, chainId 1, block 26427327, transaction 0x6c7c…c9c5 ran a call from a Safe through a Roles-type module. The full hash is in the first command. Each line below prints what I rely on, and each one runs on Ethereum mainnet, chainId 1.

1. The transaction succeeded: it prints `true`.

```
cast receipt 0x6c7cce68b6373dd0e645e6667d46788f49da5a4afc286bc363a2bf34f0a8c9c5 status -r https://eth.drpc.org # Ethereum mainnet, chainId 1
```

2. It calls the module with the selector `0x6928e74b`, `execTransactionWithRole`:

```
cast tx 0x6c7cce68b6373dd0e645e6667d46788f49da5a4afc286bc363a2bf34f0a8c9c5 input -r https://eth.drpc.org | cut -c1-10 # Ethereum mainnet, chainId 1
```

3. The sender has no contract code, so it is a plain key address. It prints `0x`:

```
cast code $(cast tx 0x6c7cce68b6373dd0e645e6667d46788f49da5a4afc286bc363a2bf34f0a8c9c5 from -r https://eth.drpc.org) -r https://eth.drpc.org # Ethereum mainnet, chainId 1
```

4. The Safe ran the call through a module: the receipt holds one `ExecutionFromModuleSuccess` log, and it prints `1`:

```
cast receipt 0x6c7cce68b6373dd0e645e6667d46788f49da5a4afc286bc363a2bf34f0a8c9c5 logs -r https://eth.drpc.org | grep -c $(cast keccak "ExecutionFromModuleSuccess(address)") # Ethereum mainnet, chainId 1
```

5. One block before, the Safe had a threshold of 2. The Safe is the avatar of the module that the transaction called. It prints `2`:

```
cast call $(cast call $(cast tx 0x6c7cce68b6373dd0e645e6667d46788f49da5a4afc286bc363a2bf34f0a8c9c5 to -r https://eth.drpc.org) "avatar()(address)" --block 26427326 -r https://eth.drpc.org) "getThreshold()(uint256)" --block 26427326 -r https://eth.drpc.org # Ethereum mainnet, chainId 1
```

6. The Safe had four owners. It prints four addresses:

```
cast call $(cast call $(cast tx 0x6c7cce68b6373dd0e645e6667d46788f49da5a4afc286bc363a2bf34f0a8c9c5 to -r https://eth.drpc.org) "avatar()(address)" --block 26427326 -r https://eth.drpc.org) "getOwners()(address[])" --block 26427326 -r https://eth.drpc.org # Ethereum mainnet, chainId 1
```

7. The sender was not one of its owners. It prints `false`:

```
cast call $(cast call $(cast tx 0x6c7cce68b6373dd0e645e6667d46788f49da5a4afc286bc363a2bf34f0a8c9c5 to -r https://eth.drpc.org) "avatar()(address)" --block 26427326 -r https://eth.drpc.org) "isOwner(address)(bool)" $(cast tx 0x6c7cce68b6373dd0e645e6667d46788f49da5a4afc286bc363a2bf34f0a8c9c5 from -r https://eth.drpc.org) --block 26427326 -r https://eth.drpc.org # Ethereum mainnet, chainId 1
```

8. The module is a plain EIP-1167 clone. Its code starts with `0x363d3d373d3d3d363d73`, followed by the address of the implementation:

```
cast code $(cast tx 0x6c7cce68b6373dd0e645e6667d46788f49da5a4afc286bc363a2bf34f0a8c9c5 to -r https://eth.drpc.org) -r https://eth.drpc.org | cut -c1-22 # Ethereum mainnet, chainId 1
```

9. The code of that implementation contains the selector from step 2, which is what Roles-type means above. It prints `1`:

```
cast code 0x$(cast code $(cast tx 0x6c7cce68b6373dd0e645e6667d46788f49da5a4afc286bc363a2bf34f0a8c9c5 to -r https://eth.drpc.org) -r https://eth.drpc.org | cut -c23-62) -r https://eth.drpc.org | grep -c 6928e74b # Ethereum mainnet, chainId 1
```
