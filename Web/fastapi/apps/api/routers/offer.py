from fastapi import APIRouter
from ..config import models

router = APIRouter(
    prefix="/offer",
    tags=["Offer"]
)

@router.post("/")
async def create_offer(offer: models.Offer):
    return offer
