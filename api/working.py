# from calls.bitQuery.pairCreated import get_pairs_reserve
# import asyncio


# asyncio.run(get_pairs_reserve(10, 0))
# =========================================================================
# from components.pairComponent import PairComponent
# import asyncio

# pair_component = PairComponent("0x0A8Ca6C1eE7051875D1b2A97839EE2C70755b494")


# res = asyncio.run(pair_component.data())
# print(res)
# =========================================================================
# from calls.moralis.erc20_metadata import tokenMetadata, tokenAge
# import asyncio

# res = asyncio.run(tokenMetadata("0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3"))
# print(res)
# res = asyncio.run(tokenAge("0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3"))
# print(res)
# =========================================================================
from components.pairComponent import pairInfo
import asyncio

res = asyncio.run(pairInfo("0x0A8Ca6C1eE7051875D1b2A97839EE2C70755b494"))
print(res)
