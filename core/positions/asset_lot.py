import datetime

from core.market.asset import Asset
from core.positions.base_lot import BaseLot


class AssetLot(BaseLot):
    def __init__(self, asset: Asset):
        super().__init__()
        self.asset: Asset = asset

    def buy(
        self,
        share_units_in: float,  # share units to buy
        entitlement_in: float,  # asset units per a share unit when buying
        price_in_implied: float,
        datetime_in: datetime.datetime,
    ) -> None:
        assert self.units_in == 0
        assert share_units_in > 0
        assert entitlement_in > 0
        assert price_in_implied > 0

        self.units_in: float = share_units_in * entitlement_in
        self.price_in: float = price_in_implied
        self.datetime_in: datetime.datetime = datetime_in

    def sell(
        self,
        share_units_out: float,  # share units to sell
        entitlement_out: float,  # asset units per a share unit when selling
        price_out_implied: float,
        datetime_out: datetime.datetime,
    ) -> None:
        assert self.units_in > 0
        assert share_units_out > 0
        assert entitlement_out > 0
        assert price_out_implied > 0

        self.units_out_list.append(share_units_out * entitlement_out)
        self.price_out_list.append(price_out_implied)
        self.datetime_out_list.append(datetime_out)
