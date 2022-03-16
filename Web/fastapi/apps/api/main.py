from typing import Optional, List, Union, Dict
from fastapi import FastAPI, Query, Path, HTTPException, status, Body, Cookie, Header
from datetime import datetime, time, timedelta
from uuid import UUID

from .config import models, schema
from .config.function import rt_list
from .routers import users, offer


app = FastAPI()

app.include_router(users.router)
app.include_router(offer.router)




items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@app.get(
    "/items/{item_id}/name",
    response_model=models.Item,
    response_model_include={"name", "description"},
)
async def read_item_name(item_id: str):
    return items[item_id]


@app.get(
    "/items/{item_id}/public",
    response_model=models.Item,
    response_model_exclude={"tax"}
)
async def read_item_public_data(item_id: str):
    return items[item_id]


@app.post("/items/", response_model=models.Item)
async def create_item(item: models.Item):
    return item


@app.post("/user/",response_model=schema.UserOut)
async def create_user(user: models.UserIn):
    return user


# @app.get("/items/;")
# async def read_items(
#     x_token: Optional[List[str]] = Header(None)
# ):
#     return {"X-Token values": x_token}

# @app.get("/items/")
# async def read_items(ads_id: Optional[str] = Cookie(None)):
#     return {"ads_id": ads_id}


# @app.get('/items/{item_id}')
# async def read_items(
#     item_id: UUID,
#     start_datetime: Optional[datetime] = Body(None),
#     end_datetime: Optional[datetime] = Body(None),
#     repeat_at: Optional[time] = Body(None),
#     process_after: Optional[timedelta] = Body(None)
    
# ):
#     try:          
#         start_process = start_datetime + process_after
#         duration = end_datetime - start_datetime
#         return {
#             "item_id" : item_id,
#             "start_datetime": start_datetime,
#             "end_datetime": end_datetime,
#             "repeat_at": repeat_at,
#             "process_after": process_after,
#             "start_process": start_process,
#             "duration": duration
#         }

#     except:
#         raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
#                              detail=f"Try again :("
#         )



@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: models.Item = Body(
        ...,
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** item works correctly.",
                "value": {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
            },
            "converted": {
                "summary": "An example with converted data",
                "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                "value": {
                    "name": "Bar",
                    "price": "35.4",
                },
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error",
                "value": {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            },
        },
    ),
):
    results = {"item_id": item_id, "item": item}
    return results


@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights