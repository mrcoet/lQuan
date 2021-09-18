import json
import aiohttp


from keys import moralis_api_key


async def token_metadata(token_address):
    async with aiohttp.ClientSession() as session:
        url = "https://deep-index.moralis.io/api/v2/erc20/metadata"
        parameters = {
            "chain": "bsc",
            "addresses": token_address,
        }
        headers = {"Accepts": "application/json", "X-API-Key": moralis_api_key}
        async with session.get(url, headers=headers, params=parameters) as response:
            data = json.loads(await response.text())
            return data


async def token_block_number(token_address):
    try:
        data = await token_metadata(token_address)
        token_block_number = data[0]["block_number"]
        return token_block_number
    except Exception as e:
        print("=" * 50)
        print(f"Error: moralis -> token_block_number")
        print(f"Error Type: {e.__class__} Occurred")
        print("-" * 50)
        print(e)
        print("=" * 50)
        return None
