import aiohttp
import json
import base64


async def fetch_data(addr: str):
    __BASE_URL = "https://api.coingecko.com/api/v3/"
    __API_ID = "binance-smart-chain"
    url = f"{__BASE_URL}/coins/{__API_ID}/contract/{addr}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def fetch_logo_binary(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            logo_binary = await response.read()
            return base64.b64encode(logo_binary)


async def one_logo(addr: str):
    try:
        token_info = await fetch_data(addr)
        token_data = json.loads(token_info)
    except Exception as e:
        print("=" * 50)
        print(f"error in addr: {addr}")
        print(token_info)
        print("=" * 50)
        return None
    try:
        logo_url = token_data["image"]["thumb"]
        return await fetch_logo_binary(logo_url)
    except:
        print(f"Logo Not Found: {addr}")
        return None
