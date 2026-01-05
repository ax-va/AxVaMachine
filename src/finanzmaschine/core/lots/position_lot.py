import datetime
from typing import override

from finanzmaschine.core.lots.base_lot import BaseLot


class PositionLot(BaseLot):
    """A lot that represents a position with an invariant unit balance."""

    @property
    def units_open(self) -> float:
        return self.units_in - self.units_out_total

    @property
    def is_open(self) -> bool:
        return self.units_open > 0

    @property
    def is_closed(self) -> bool:
        return not self.is_open

    @override
    def record_out(
        self,
        *,
        units_out: float,
        price_out: float,
        datetime_out: datetime.datetime,
        **kwargs,
    ) -> None:
        assert units_out <= self.units_open
        return super().record_out(
            units_out=units_out,
            price_out=price_out,
            datetime_out=datetime_out,
            **kwargs,
        )
