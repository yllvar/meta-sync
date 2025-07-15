# app/models/profit.py
from pydantic import BaseModel
from typing import Optional

class ProfitResponse(BaseModel):
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
    profit: float
    swap: float
    commission: float
    error_desc: str