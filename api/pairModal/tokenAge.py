from calls.moralis.erc20_metadata import token_block_number


async def token_age(tokenAddress: str):
    from web3 import Web3
    from web3.middleware import geth_poa_middleware

    w3 = Web3(Web3.HTTPProvider("https://bsc-dataseed.binance.org/"))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    block_number = await token_block_number(tokenAddress)
    if block_number:
        theBlock = w3.eth.get_block(int(block_number))
        timeEpoch = theBlock["timestamp"]
        return timeEpoch
    else:
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
