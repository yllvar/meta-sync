# app/models/history.py
from pydantic import BaseModel
from typing import Optional

class HistoricalBar(BaseModel):
    time: int
    open: float
    high: float
    low: float
    close: float
    tick_volume: int
    spread: int
    real_volume: float

class HistoricalTick(BaseModel):
    time: int
    bid: float
    ask: float
    last: float
    volume: int
    time_msc: int
    flags: int
    volume_real: float