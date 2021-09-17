import aiohttp
import asyncio
import base64

logo_url = "https://bscscan.com/token/images/safemoon2_32.png"


async def logo_binary(logo_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(logo_url) as response:
            logo_binary = await response.read()
            print(logo_binary)
            logo_64_encode = base64.b64encode(logo_binary)  # encode -> translate byteString to the encoded type.
            print("=" * 50)
            print(logo_64_encode)
            print(logo_64_encode.decode())  # decode -> just remove b''


asyncio.run(logo_binary(logo_url))
