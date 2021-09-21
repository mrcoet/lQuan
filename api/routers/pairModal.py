from fastapi import APIRouter

from components.modalComponent import modalInfo


router_pair_modal = APIRouter()


@router_pair_modal.get("/modal/{pairAddress}")
async def get_modal_info(pairAddress: str):
    return await modalInfo(pairAddress)
