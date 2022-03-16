from typing import Optional
from ..config import models, schema
from fastapi import APIRouter, Path, Query

router = APIRouter(
    prefix='/user',
    tags=["User"]
)

@router.get('/{user_id}', response_model=schema.UserUniversalOuput)
async def read_items(
    *,          # all the following parameters should be called as keyword arguments
        # title metadata, numerical constraint
    user_id : int = Path(..., title="The ID of the user to get", ge=0, le=1000),
    q : Optional[str] = Query(None, alias="item-query"),
    info: models.Universal
):
    results = {**info.dict(), "user_id": user_id}
    if q:
        results.update({"q": q})
    return results