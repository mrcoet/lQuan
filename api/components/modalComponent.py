"""
tokenName,
tokenSymbol,
tokenPrice,
contractVersion,
honeypot,
funnyName,
tokenOwner,
tokenAge,
tokenHolders,
mCap,
lockers[],
socialMedia
badMethods[],
"""

from pydantic import BaseModel

import pairModal.pairTokenInfo as info
from pairModal.tokenAge import token_age
from pairModal.funnyName import okay_name
from calls.bscScan.contractCall import get_contract
from pairModal.contractVersion import check_contract_version
import pairModal.miniAudit as miniaudit
from pairModal.honeypot import check_honeypot

import random

from typing import Optional


class Modal(BaseModel):
    id: int = None
    tokenName: Optional[str] = None
    tokenSymbol: Optional[str] = None
    tokenPrice: Optional[str] = None
    contractVersion: Optional[str] = None
    honeypot: Optional[str] = None
    funnyName: Optional[bool] = False
    tokenOwner: Optional[str] = None
    tokenAge: Optional[int] = None
    tokenHolders: Optional[str] = None
    mCap: Optional[float] = None
    lockers: Optional[dict] = None
    socialMedia: Optional[dict] = None
    badMethods: Optional[dict] = None
    routerV2: Optional[bool] = False
    pairAddress: Optional[str] = None
    tokenAddress: Optional[str] = None


# rewrite it --> lack of concurancy
async def modalInfo(pair_address):
    tokensAddresses = await info.tokens_addresses(pair_address)  # [token0Address, token1Address]
    quoteTokenInfo = await info.quote_token_info(tokensAddresses)  # {"address":, "name": , "symbol": , "decimals": , "owner": }
    pairReserves = await info.reserves(pair_address)
    tokenmCap = await info.token_mcap(pairReserves, tokensAddresses)
    tokenPrice = await info.token_price(pairReserves, tokensAddresses, quoteTokenInfo["decimals"])
    pairTotalSupply = await info.pair_total_supply(pair_address)
    burnLocked = await info.lockedLiquidity("0x000000000000000000000000000000000000dEaD", pair_address, pairTotalSupply)  # None , Float
    zeroLocked = await info.lockedLiquidity("0x0000000000000000000000000000000000000000", pair_address, pairTotalSupply)  # None , Float
    deepLocker = await info.lockedLiquidity("0x3f4D6bf08CB7A003488Ef082102C2e6418a4551e", pair_address, pairTotalSupply)  # None , Float
    unicryptLocked = await info.lockedLiquidity("0xC765bddB93b0D1c1A88282BA0fa6B2d00E3e0c83", pair_address, pairTotalSupply)  # None , Float
    cakeMainStaking = await info.lockedLiquidity("0x73feaa1ee314f8c655e354234017be2193c9e24e", pair_address, pairTotalSupply)  # None , Float
    quoteTokenAge = await token_age(quoteTokenInfo["address"])
    okayName = await okay_name(quoteTokenInfo["name"])  # True, False
    okaySymbol = await okay_name(quoteTokenInfo["symbol"])  # True, False
    callContract = await get_contract(quoteTokenInfo["address"])
    contractVersion = await check_contract_version(callContract)  # None or Str
    contractSourceCode = await miniaudit.get_source_code(callContract)
    bad_methods_calling_router_v2 = await miniaudit.using_router_v2(contractSourceCode)  # True, False
    bad_methods_have_telegram = await miniaudit.telegram_in_code(contractSourceCode)  # True, False
    bad_methods_have_twitter = await miniaudit.twitter_in_code(contractSourceCode)  # True, False
    bad_methods_have_website = await miniaudit.website_in_code(contractSourceCode)  # True, False
    bad_methods_code = await miniaudit.bad_in_code("./badInCode.txt", contractSourceCode)  # {"warning": True, "warnings": warnings}, {"warning": False, "warnings": []}
    tokenHoneypotCheck = await check_honeypot(quoteTokenInfo["address"])
    modal = Modal()
    modal.id = random.randint(0, 10000)
    modal.tokenName = quoteTokenInfo["name"]
    modal.tokenSymbol = quoteTokenInfo["symbol"]
    modal.tokenPrice = tokenPrice
    modal.contractVersion = contractVersion
    modal.honeypot = tokenHoneypotCheck["status"]
    if okayName and okaySymbol:
        modal.funnyName = False
    else:
        modal.funnyName = True
    modal.tokenOwner = quoteTokenInfo["owner"]
    modal.tokenAge = quoteTokenAge
    modal.tokenHolders = "N/A"
    modal.mCap = tokenmCap
    modal.lockers = {"burn": (burnLocked + zeroLocked), "deepLocker": deepLocker, "unicrypt": unicryptLocked, "cakeMainStaking": cakeMainStaking}
    modal.socialMedia = {"twitter": bad_methods_have_twitter, "telegram": bad_methods_have_telegram, "website": bad_methods_have_website}
    modal.badMethods = bad_methods_code
    modal.routerV2 = bad_methods_calling_router_v2
    modal.tokenAddress = quoteTokenInfo["address"]
    modal.pairAddress = pair_address
    return modal
