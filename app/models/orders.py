# app/models/orders.py
from pydantic import BaseModel
from typing import Optional

class OrderRequest(BaseModel):
    action: int
    symbol: str
    volume: float
    price: float
    sl: float
    tp: float
    deviation: int
    magic: int
    comment: str
    type_time: int
    type_filling: int
    expiration: int
    dry_run: Optional[bool] = False

class OrderResponse(BaseModel):
    retcode: int
    deal: Optional[int]
    order: Optional[int]
    volume: float
    price: float
    bid: float
    ask: float
    sl: float
    tp: float
    deviation: int
    magic: int
    comment: str
    price_level: float
    type: int
    type_time: int
    type_filling: int
    expiration: int
    state: int
    request_id: int
    retcode_external: int
    comment_external: str
    request_attempt: int
    request_cnt: int
    error_desc: str
