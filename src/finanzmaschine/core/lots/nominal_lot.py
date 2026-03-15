from datetime import datetime
from decimal import Decimal
from typing import override

from finanzmaschine.core.lots.base_lot import BaseLot
from finanzmaschine.utils.float_helper import is_zero


class NominalLot(BaseLot):
    """
    A lot representing a lot with an invariant unit balance.

    The number of units is invariant:
    units_open = units_in - units_closed.
    """

    @property
    def units_open(self) -> float:
        return self.lot_record_in.units - self.units_closed

    @property
    def is_open(self) -> bool:
        return not self.is_closed

    @property
    def is_closed(self) -> bool:
        return is_zero(self.units_open)

    @override
    def _validate_record_out(
        self,
        units: float,
        price: Decimal,
        fee: Decimal,
        dt: datetime,
    ) -> None:
        super()._validate_record_out(units, price, fee, dt)
        assert units <= self.units_open
