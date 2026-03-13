from datetime import datetime
from typing import override

from finanzmaschine.core.lots.base_lot import BaseLot
from finanzmaschine.core.lots.lot_state import LotState


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
        return self.state == LotState.OPEN

    @property
    def is_closed(self) -> bool:
        return self.state == LotState.CLOSED

    @override
    def record_out(
        self,
        *,
        units: float,
        price: float,
        fee: float,
        dt: datetime,
    ) -> None:
        assert units <= self.units_open

        super().record_out(
            units=units,
            price=price,
            fee=fee,
            dt=dt,
        )

        if self.units_open == 0:
            self.state = LotState.CLOSED
