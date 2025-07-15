# app/models/tick.py
from pydantic import BaseModel

class TickInfo(BaseModel):
    time: int
    bid: float
    ask: float
    last: float
    volume: int
    time_msc: int
    flags: int
    volume_real: float