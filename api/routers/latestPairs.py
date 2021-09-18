from fastapi import APIRouter

from calls.bitQuery.pairCreated import get_latest_pairs
from components.pairComponent import pairInfo


router_latest_pairs = APIRouter()


@router_latest_pairs.get("/latestpairs/{page}")
async def latest_pairs(page: int = 0):
    bitquery_latest_pairs: list(dict) = await get_latest_pairs(50, page)
    latest_pairs_final = []
    for pair_dict in bitquery_latest_pairs:
        try:
            pair_component = await pairInfo(pair_address=pair_dict["pair"], block_number=pair_dict["blockNumber"], token0_address=pair_dict["token0"], token1_address=pair_dict["token1"])
            if pair_component:
                latest_pairs_final.append(pair_component)
        except Exception as e:
            print("=" * 50)
            print(e)
            print("=" * 50)
    return latest_pairs_final
