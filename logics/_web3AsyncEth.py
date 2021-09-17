import asyncio
from web3 import Web3, AsyncHTTPProvider
from web3.eth import AsyncEth
from web3.net import AsyncNet
from web3.middleware import geth_poa_middleware


async def main():
    moralis_url = ""
    w3 = Web3(AsyncHTTPProvider(moralis_url), modules={"eth": (AsyncEth,), "net": (AsyncNet,)}, middlewares=[])
    print(type(w3.provider))
    coinbase = await w3.eth.coinbase
    print(coinbase)
    wallet = await w3.eth.block_number
    print(wallet)


# not supported yet
# Resource: https://web3py.readthedocs.io/en/stable/providers.html#supported-middleware


async def tokenAge(tokenAddress: str):
    moralis_url = ""
    w3 = Web3(AsyncHTTPProvider(moralis_url), modules={"eth": (AsyncEth,), "net": (AsyncNet,)}, middlewares=[])
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    blockNumber = await w3.eth.block_number
    fromBlock = blockNumber - 4000
    fromBlock = hex(int(fromBlock))
    transferHash = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
    tokenAddress = w3.toChecksumAddress(tokenAddress)
    params = {"address": tokenAddress, "fromBlock": fromBlock, "topics": [transferHash]}
    firstTransfer = await w3.eth.get_logs(params)[0]
    blockNumber = firstTransfer["blockNumber"]
    theBlock = await w3.eth.get_block(blockNumber)
    timeEpoch = theBlock["timestamp"]
    return timeEpoch


if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(tokenAge("0x9bb8dae2b5b5153ff19857c252f591f3e4bdbc9a"))
