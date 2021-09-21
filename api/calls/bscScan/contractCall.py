import json
import aiohttp


from keys import bscscan_api_key


# async def get_contract(addr: str):
#     async with aiohttp.ClientSession() as session:
#         url = "https://api.bscscan.com/api"
#         parameters = {"module": "contract", "action": "getsourcecode", "address": addr, "apikey": bscscan_api_key}

#         async with session.get(url, params=parameters) as response:
#             data = json.loads(await response.text())
#             if version := data["result"][0]["CompilerVersion"]:
#                 proxy = data["result"][0]["Proxy"]
#                 version = version[0 : version.index("+")]
#                 return version, proxy  # ('v0.6.12', '0')
#             else:
#                 return None


async def get_contract(addr: str):
    async with aiohttp.ClientSession() as session:
        url = "https://api.bscscan.com/api"
        parameters = {"module": "contract", "action": "getsourcecode", "address": addr, "apikey": bscscan_api_key}

        async with session.get(url, params=parameters) as response:
            data = json.loads(await response.text())
            return data


"""
data["result"][0]["SourceCode"]
data["result"][0]["CompilerVersion"]
data["result"][0]["Proxy"]
data["result"][0]["ABI"]
"""
