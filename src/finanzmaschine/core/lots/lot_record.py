from dataclasses import dataclass
from datetime import datetime

from finanzmaschine.core.lots.currency_enum import Currency


@dataclass(frozen=True)
class LotRecord:
    units: float
    price: float
    price_currency: Currency
    fee: float
    fee_currency: Currency
    dt: datetime
