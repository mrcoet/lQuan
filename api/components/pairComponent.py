"""
quoteTokenName,
quoteTokenSymbol,
quoteTokenLogo,
quoteTokenAge,
mCap,
pairAddress,
quoteTokenAddress,
"""

from pydantic import BaseModel
from typing import Optional

from calls.webThree.panCakeSwap import Cake

from calls.coingecko.fetch_one_logo import one_logo

from calls.moralis.erc20_metadata import token_block_number

import random

import asyncio


class Pair(BaseModel):
    id: int = None
    quoteTokenAddres: str = None  # checked
    quoteTokenName: str = None  # checked
    quoteTokenSymbol: str = None  # checked
    quoteTokenLogo: Optional[bytes] = None
    quoteTokenAge: int = None  # checked
    mCap: float = None  # checked
    pairAddress: str = None  # checked
    blockNumber: Optional[int] = None  # checked


cake = Cake()


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


async def pairInfo(pair_address: str, block_number=None, token0_address=None, token1_address=None):

    pair_address = cake.w3.toChecksumAddress(pair_address)
    pair_contract = await cake.get_pair_contract(pair_address)

    if token0_address and token1_address:
        tokens_addresses = [cake.w3.toChecksumAddress(token0_address), cake.w3.toChecksumAddress(token1_address)]
    else:
        task_token0_address = asyncio.create_task(cake.get_token0_address(pair_contract))
        task_token1_address = asyncio.create_task(cake.get_token1_address(pair_contract))
        tasks = [task_token0_address, task_token1_address]
        tokens_addresses = await asyncio.gather(*tasks)

    if cake.WBNB not in tokens_addresses:
        return None

    try:
        reserves = await cake.get_reserves(pair_contract)
        mcap = reserves[0] if tokens_addresses[0] == cake.WBNB else reserves[1]
        mcap = mcap / (10 ** 18)
        mcap = round(mcap, 3)
    except Exception as e:
        print("=" * 50)
        print(f"Error: pairComponent -> pairInfo -> cake.get_reserves")
        print(f"Error Type: {e.__class__} Occurred")
        print("-" * 50)
        print(e)
        print("=" * 50)
        mcap = 0.0

    if mcap < 0.3:
        return None

    quote_address = tokens_addresses[0] if tokens_addresses[1] == cake.WBNB else tokens_addresses[1]

    quote_contract = await cake.get_token_contract(quote_address)

    task_quote_name = asyncio.create_task(cake.get_token_name(quote_contract))
    task_quote_symbol = asyncio.create_task(cake.get_token_symbol(quote_contract))
    task_token_logo = asyncio.create_task(one_logo(quote_address))
    task_token_age = asyncio.create_task(token_age(quote_address))

    tasks = [task_quote_name, task_quote_symbol, task_token_logo, task_token_age]
    quote_info = await asyncio.gather(*tasks)

    pair = Pair(id=(random.randint(0, 10000)), quoteTokenAddres=quote_address, quoteTokenName=quote_info[0], quoteTokenSymbol=quote_info[1], quoteTokenLogo=quote_info[2], quoteTokenAge=quote_info[3], mCap=mcap, pairAddress=pair_address, blockNumber=block_number)
    return pair
