import datetime as dt

from dataclasses import dataclass


@dataclass(frozen=True)
class BaseLotRecord:
    units: float
    price: float
    datetime: dt.datetime
