from datetime import datetime
from typing import override

from finanzmaschine.core.lots.base_lot import BaseLot


class NominalLot(BaseLot):
    """
    A lot representing a lot with an invariant unit balance.

    The number of units is invariant: units_open = units_in - units_out_total.
    """

    @property
    def units_open(self) -> float:
        return self.lot_record_in.units - self.units_out_total

    @property
    def is_open(self) -> bool:
        return self.units_open > 0

    @property
    def is_closed(self) -> bool:
        return self.units_open == 0

    @override
    def _validate_record_out(
        self,
        units: float,
        price: float,
        fee: float,
        dt: datetime,
    ) -> None:
        super()._validate_record_out(units, price, fee, dt)
        assert units <= self.units_open
