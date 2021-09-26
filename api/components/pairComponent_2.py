"""
quoteTokenName,
quoteTokenSymbol,
quoteTokenLogo,
quoteTokenAge,
mCap,
pairAddress,
quoteTokenAddress,
blockNumber
"""

from pydantic import BaseModel
from typing import Optional

import random

from toolz.itertoolz import get

from calls.streamingFast.latestPairs import latest_pairs

from pairModal.honeypot import check_honeypot

import time

from pairModal.tokenAge import token_age

from pairModal.contractVersion import check_contract_version

from calls.bscScan.contractCall import get_contract

import random

WBNB = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"


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
    version: Optional[str] = None


async def pairs_info(limit=20, page=0):
    streamingFastCall = await latest_pairs(limit, page)
    """
    list(dict):
    "block", "id", "reserve0", "reserve1", "token0"{"derivedUSD","id","name","symbol"}, "token1"{"derivedUSD","id","name","symbol"}
    """
    out_ = []
    for pair in streamingFastCall:
        pair_ = Pair()
        tokens = [str(pair["token0"]["id"]).lower(), str(pair["token1"]["id"]).lower()]
        if WBNB.lower() not in tokens:
            continue
        mcap = float(pair["reserve0"]) if tokens[0] == WBNB.lower() else float(pair["reserve1"])
        print("=" * 50)
        print(f"mcap: {mcap}")
        if float(mcap) < 0.0:
            continue

        tokenAddress = tokens[1] if tokens[0] == WBNB.lower() else tokens[0]

        time.sleep(1.5)
        honeypot = await check_honeypot(tokenAddress)
        print(f"honeypot: {honeypot}")

        if honeypot.get("error"):
            print(f"Cant check honeypot for: {tokenAddress}")
            continue

        else:
            if honeypot["status"] != "OK":
                continue

        time.sleep(1.5)
        contractcall = await get_contract(tokenAddress)

        contractVersion = await check_contract_version(contractcall)
        print(f"contract Version: {contractVersion}")
        if not contractVersion:
            contractVersion = "N/A"

        tokenName = pair["token1"]["name"] if tokens[0] == WBNB.lower() else pair["token0"]["name"]
        tokenSymbol = pair["token1"]["symbol"] if tokens[0] == WBNB.lower() else pair["token0"]["symbol"]
        tokenAge = await token_age(tokenAddress)

        pair_.id = random.randint(0, 10000)
        pair_.quoteTokenAddres = tokenAddress
        pair_.quoteTokenName = tokenName
        pair_.quoteTokenSymbol = tokenSymbol
        pair_.quoteTokenLogo = None
        pair_.quoteTokenAge = tokenAge
        pair_.mCap = mcap
        pair_.pairAddress = pair["id"]
        pair_.blockNumber = pair["block"]
        pair_.version = contractVersion
        out_.append(pair_)
    return out_
