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
# from components.pairComponent import pairInfo
# import asyncio

# res = asyncio.run(pairInfo("0x0A8Ca6C1eE7051875D1b2A97839EE2C70755b494"))
# print(res)
# =========================================================================
# import json
# import aiohttp
# import asyncio

# from keys import bscscan_api_key


# async def get_contract(addr: str):
#     async with aiohttp.ClientSession() as session:
#         url = "https://api.bscscan.com/api"
#         parameters = {"module": "contract", "action": "getsourcecode", "address": addr, "apikey": bscscan_api_key}

#         async with session.get(url, params=parameters) as response:
#             data = json.loads(await response.text())
#             print(data["result"][0]["SourceCode"])
#             print("=" * 100)
#             print(data["result"][0]["CompilerVersion"])
#             print("=" * 100)
#             print(data["result"][0]["Proxy"])
#             print("=" * 100)
#             print(data["result"][0]["ABI"])
#             print("=" * 100)
#             if version := data["result"][0]["CompilerVersion"]:
#                 proxy = data["result"][0]["Proxy"]
#                 version = version[0 : version.index("+")]
#                 return version, proxy  # ('v0.6.12', '0')
#             else:
#                 return None


# asyncio.run(get_contract("0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3"))
# =========================================================================
from pairModal.honeypot import check_honeypot
import asyncio

asyncio.run(check_honeypot("0x13668c334701798261583A7969A467e42937286A"))
