from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from finanzmaschine.core.lots.currency_enum import Currency


@dataclass(frozen=True)
class LotRecord:
    units: float
    price: Decimal
    price_currency: Currency
    fee: Decimal
    fee_currency: Currency
    dt: datetime
