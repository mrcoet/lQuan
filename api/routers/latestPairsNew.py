from fastapi import APIRouter

from components.pairComponent_2 import pairs_info


router_latest_pairs_new = APIRouter()


@router_latest_pairs_new.get("/latestpairsnew/{page}")
async def latest_pairs_new(page: int = 0):
    return await pairs_info(page=page)
