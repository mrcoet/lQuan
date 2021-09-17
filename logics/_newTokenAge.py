from web3 import Web3
from web3.middleware import geth_poa_middleware
import json
from datetime import timezone


w3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org/"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

print(w3.isConnected())

fromBlock = w3.eth.block_number - 4000
fromBlock = hex(int(fromBlock))
transferHash = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
tokenAddress = w3.toChecksumAddress("0x9bb8dae2b5b5153ff19857c252f591f3e4bdbc9a")

params = {"address": tokenAddress, "fromBlock": fromBlock, "topics": [transferHash]}

blockNumber = w3.eth.get_logs(params)[0]["blockNumber"]
timeEpoch = w3.eth.get_block(blockNumber)["timestamp"]

print(timeEpoch)


def EpochToISO8601(theEpoch):

    from datetime import datetime

    return datetime.fromtimestamp(theEpoch, timezone.utc).isoformat()


print(EpochToISO8601(timeEpoch))


def tokenAge(tokenAddress: str):
    w3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org/"))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    fromBlock = w3.eth.block_number - 4000
    fromBlock = hex(int(fromBlock))
    transferHash = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
    tokenAddress = w3.toChecksumAddress(tokenAddress)
    params = {"address": tokenAddress, "fromBlock": fromBlock, "topics": [transferHash]}
    firstTransfer = w3.eth.get_logs(params)[0]
    blockNumber = firstTransfer["blockNumber"]
    theBlock = w3.eth.get_block(blockNumber)
    timeEpoch = theBlock["timestamp"]
    return timeEpoch


print(tokenAge("0x9bb8dae2b5b5153ff19857c252f591f3e4bdbc9a"))
