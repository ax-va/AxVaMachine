from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class LotRecord:
    units: float
    price: float
    fee: float
    dt: datetime
