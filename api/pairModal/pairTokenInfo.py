from typing import Optional
from calls.webThree.panCakeSwap import Cake
import asyncio

cake = Cake()


async def tokens_addresses(pair_address):
    pair_address = cake.w3.toChecksumAddress(pair_address)
    pair_contract = await cake.get_pair_contract(pair_address)
    try:
        task_token0_address = asyncio.create_task(cake.get_token0_address(pair_contract))
        task_token1_address = asyncio.create_task(cake.get_token1_address(pair_contract))
        tasks = [task_token0_address, task_token1_address]

        tokens_addresses = await asyncio.gather(*tasks)  # [token0Address, token1Address]
        return tokens_addresses
    except Exception as e:
        print("=" * 50)
        print(f"Error: pairTokenInfo -> tokens_address")
        print(f"Error Type: {e.__class__} Occurred")
        print("-" * 50)
        print(e)
        print("=" * 50)
        return False


async def quote_token_info(tokens_addresses) -> Optional[dict]:
    quote_token_address = tokens_addresses[1] if tokens_addresses[0] == cake.WBNB else tokens_addresses[0]
    quote_token_contract = await cake.get_token_contract(quote_token_address)
    task_quote_name = asyncio.create_task(cake.get_token_name(quote_token_contract))
    task_quote_symbol = asyncio.create_task(cake.get_token_symbol(quote_token_contract))
    task_quote_decimals = asyncio.create_task(cake.get_token_decimals(quote_token_contract))

    tasks = [task_quote_name, task_quote_symbol, task_quote_decimals]
    res = await asyncio.gather(*tasks)

    try:
        token_quote_owner = await cake.get_token_owner(quote_token_contract)
    except Exception as e:
        print("=" * 50)
        print(f"Error: pairTokenInfo -> tokens_address")
        print(f"Error Type: {e.__class__} Occurred")
        print("-" * 50)
        print(e)
        print("=" * 50)
        token_quote_owner = None

    out_ = {"address": quote_token_address, "name": res[0], "symbol": res[1], "decimals": res[2], "owner": token_quote_owner}
    return out_


async def reserves(pair_address) -> Optional[list]:
    pair_address = cake.w3.toChecksumAddress(pair_address)
    pair_contract = await cake.get_pair_contract(pair_address)
    try:
        reserves = await cake.get_reserves(pair_contract)
        return reserves
    except Exception as e:
        print("=" * 50)
        print(f"Error: pairComponent -> pairInfo -> cake.get_reserves")
        print(f"Error Type: {e.__class__} Occurred")
        print("-" * 50)
        print(e)
        print("=" * 50)
        return None


async def token_mcap(reserves, tokens_addresses: list) -> Optional[float]:
    if not reserves:
        return None
    mcap = reserves[0] if tokens_addresses[0] == cake.WBNB else reserves[1]
    mcap = mcap / (10 ** 18)
    mcap = round(mcap, 3)
    return mcap


async def token_price(reserves, tokens_addresses, quote_tokenDecimals):  # quote price # rewrite it with getAmountsOut
    if not reserves:
        return None
    reserve_base = reserves[0] if tokens_addresses[0] == cake.WBNB else reserves[1]
    reserve_quote = reserves[1] if tokens_addresses[0] == cake.WBNB else reserves[0]
    base_decimals = 18
    quote_decimals = quote_tokenDecimals
    price_ = (reserve_base * 10 ** quote_decimals) / (reserve_quote * 10 ** base_decimals)
    bnb_price = await BNBPrice()
    price_in_usd = price_ * bnb_price
    # https://stackoverflow.com/questions/29849445/convert-scientific-notation-to-decimals
    return ("%.11f" % price_in_usd).rstrip("0").rstrip(".")


async def BNBPrice():  # quote price # rewrite it with getAmountsOut
    aContract = await cake.get_pair_contract("0x58F876857a02D6762E0101bb5C46A8c1ED44Dc16")
    aReserves = await cake.get_reserves(aContract)
    BNBReserve = aReserves[0]
    BUSDReserve = aReserves[1]
    BNBPrice = BUSDReserve / BNBReserve
    print(f"BNB Price: {BNBPrice}")
    return BNBPrice


async def pair_total_supply(pair_address):
    pair_address = cake.w3.toChecksumAddress(pair_address)
    pair_contract = await cake.get_pair_contract(pair_address)
    pairTotalSupply = await cake.get_pair_total_supply(pair_contract)
    return pairTotalSupply


async def lockedLiquidity(locker_address, pair_address, pairTotalSupply):
    if float(pairTotalSupply) <= 0.0:
        return None
    pair_address = cake.w3.toChecksumAddress(pair_address)
    pair_contract = await cake.get_pair_contract(pair_address)
    locker_address = cake.w3.toChecksumAddress(locker_address)

    locked_amount = await cake.check_locked_liquidity(pair_contract, locker_address)
    percent_ = (locked_amount / pairTotalSupply) * 100
    return round(percent_, 2)
