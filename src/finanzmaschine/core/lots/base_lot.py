import math
from datetime import datetime
from typing import List, Type, TypeVar, Generic

from finanzmaschine.core.lots.lot_record import LotRecord


class BaseLot:
    """
    Base lot managing immutable lot records.
    """

    def __init__(self):
        self.lot_record_in: LotRecord | None = None
        self.lot_records_out: List[LotRecord] = []

    @property
    def units_out_total(self) -> float:
        return math.fsum(lr.units for lr in self.lot_records_out)

    def record_in(
        self,
        *,
        units: float,
        price: float,
        fee: float,
        dt: datetime,
    ) -> None:
        assert units > 0
        assert price > 0
        assert fee >= 0

        self.lot_record_in = LotRecord(
            units=units,
            price=price,
            fee=fee,
            dt=dt,
        )

    def record_out(
        self,
        *,
        units: float,
        price: float,
        fee: float,
        dt: datetime,
    ) -> None:
        assert self.lot_record_in.units > 0
        assert units > 0
        assert price > 0

        lot_record_out = LotRecord(
            units=units,
            price=price,
            fee=fee,
            dt=dt,
        )
        self.lot_records_out.append(lot_record_out)
