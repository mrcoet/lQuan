from calls.webThree import get_w3


from sqlalchemy.util import greenlet_spawn


from calls.webThree import abis as ABI

from typing import List


class Cake:
    def __init__(self):
        self.w3 = get_w3()
        self.WBNB = self.w3.toChecksumAddress("0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c")
        self.ROUTER = self.w3.toChecksumAddress("0x10ED43C718714eb63d5aA57B78B54704E256024E")
        self.FACTORY = self.w3.toChecksumAddress("0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73")
        self.routerContract = None  # self.w3.eth.contract(address=self.ROUTER, abi=ABI.CAKEROUTER)
        self.factoryContract = None

    def private_get_height(self):
        if not self.factoryContract:
            self.factoryContract = self.w3.eth.contract(address=self.FACTORY, abi=ABI.CAKEFACTORY)
        return self.factoryContract.functions.allPairsLength().call()

    async def get_height(self) -> int:
        return await greenlet_spawn(self.private_get_height)

    def private_get_pair_addr(self, pair_height: int):
        if not self.factoryContract:
            self.factoryContract = self.w3.eth.contract(address=self.FACTORY, abi=ABI.CAKEFACTORY)
        return self.factoryContract.functions.allPairs(pair_height).call()

    async def get_pair_address_from_height(self, pair_height: int) -> str:
        pair_ = await greenlet_spawn(self.private_get_pair_addr, pair_height)
        pair_ = self.w3.toChecksumAddress(pair_)
        return pair_

    def private_get_pair_contract(self, pair_addrs: str):
        return self.w3.eth.contract(address=pair_addrs, abi=ABI.LP)

    async def get_pair_contract(self, pair_addr):
        pair_contract = await greenlet_spawn(self.private_get_pair_contract, pair_addr)
        return pair_contract

    def private_get_reserves(self, pair_contract):
        return pair_contract.functions.getReserves().call()

    async def get_reserves(self, pair_contract) -> List[float]:
        return await greenlet_spawn(self.private_get_reserves, pair_contract)

    def private_get_token0_addrs(self, pair_contract):
        return pair_contract.functions.token0().call()

    async def get_token0_address(self, pair_contract):
        token0_addrs = await greenlet_spawn(self.private_get_token0_addrs, pair_contract)
        token0_addrs = self.w3.toChecksumAddress(token0_addrs)
        return token0_addrs

    def private_get_token1_addrs(self, pair_contract):
        return pair_contract.functions.token1().call()

    async def get_token1_address(self, pair_contract):
        token1_addrs = await greenlet_spawn(self.private_get_token1_addrs, pair_contract)
        token1_addrs = self.w3.toChecksumAddress(token1_addrs)
        return token1_addrs

    def private_get_token_contract(self, token0_addrs: str):
        return self.w3.eth.contract(token0_addrs, abi=ABI.ERC20)

    async def get_token_contract(self, token0_addrs):
        return await greenlet_spawn(self.private_get_token_contract, token0_addrs)

    def private_get_token_decimals(self, token0_contract):
        return token0_contract.functions.decimals().call()

    async def get_token_decimals(self, token0_contract):
        return await greenlet_spawn(self.private_get_token_decimals, token0_contract)

    def private_get_token_symbol(self, token0_contract):
        return token0_contract.functions.symbol().call()

    async def get_token_symbol(self, token0_contract):
        return await greenlet_spawn(self.private_get_token_symbol, token0_contract)

    def private_get_token_name(self, token0_contract):
        return token0_contract.functions.name().call()

    async def get_token_name(self, token0_contract):
        return await greenlet_spawn(self.private_get_token_name, token0_contract)

    def private_pair_total_supply(self, pair_contract):
        return pair_contract.functions.totalSupply().call()

    async def get_pair_total_supply(self, pair_contract):
        return await greenlet_spawn(self.private_pair_total_supply, pair_contract)

    def private_pair_locked_lp(self, pair_contract, locker_address: str):
        return pair_contract.functions.balanceOf(locker_address).call()

    async def check_locked_liquidity(self, pair_contract, locker_address: str):
        return await greenlet_spawn(self.private_pair_locked_lp, pair_contract, locker_address)
