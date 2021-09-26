"https://honeypot.api.rugdoc.io/api/honeypotStatus.js?address=0x13668c334701798261583A7969A467e42937286A&chain=bsc"

import json
import aiohttp


async def check_honeypot(token_address: str) -> dict:
    url = "https://honeypot.api.rugdoc.io/api/honeypotStatus.js"
    paramaters = {"address": token_address, "chain": "bsc"}
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, params=paramaters) as response:
                data = json.loads(await response.text())
                return data  # {'status': 'OK'}
    except Exception as e:
        print("=" * 50)
        print("Error in --> pairModal --> honeypot --> check_honeypot")
        print("-" * 50)
        print(e)
        print("=" * 50)
        return None
