import datetime
from typing import Dict

from core.asset_lot import AssetLot
from core.exchange import Exchange
from core.instruments import Instrument, ShareInstrument
from core.lot import Lot


class ShareLot(Lot):
    def __init__(self, instrument: ShareInstrument):
        self.instrument: ShareInstrument = instrument
        self.units: float = 0  # amount
        self.asset_lot = AssetLot(self.asset_name)
        self.entitlement_bought: float | None = None  # asset per share
        self.entitlement_sold: float | None = None  # asset per share
        super().__init__()

    @property
    def share_isin(self) -> str:
        return self.instrument.isin

    @property
    def share_name(self) -> str:
        return self.instrument.name

    @property
    def share_local_ids(self) -> Dict[str, str]:
        return self.instrument.local_ids

    @property
    def share_tickers(self) -> Dict[Exchange, str]:
        return self.instrument.tickers

    @property
    def asset_name(self) -> str:
        return self.instrument.asset_name

    def buy(
        self,
        cash_in: float,
        price: float,
        price_dt: datetime.datetime,
    ) -> None:
        assert cash_in > 0
        assert price > 0
        assert self.units == 0

        self.units: float = cash_in / price
        self.price_bought: float = price
        self.price_bought_dt: datetime.datetime = price_dt

    def sell(
        self,
        price: float,
        price_dt: datetime.datetime,
    ) -> float:
        assert self.units > 0

        cash_out: float = self.units * price
        self.price_sold: float = price
        self.price_sold_dt: datetime.datetime = price_dt
        return cash_out


def buy_share_lot(
    share_lot: ShareLot,
    cash_in: float,
    share_price: float,
    entitlement: float,  # asset per share
    price_dt: datetime.datetime,
) -> None:
    share_lot.buy(cash_in, share_price, price_dt)
    share_lot.entitlement_bought = entitlement
    asset_price_implied: float = share_price / entitlement
    share_lot.asset_lot.buy(share_lot.units, entitlement, asset_price_implied, price_dt)


def sell_share_lot(
    share_lot: ShareLot,
    share_price: float,
    entitlement: float,  # asset per share
    price_dt: datetime.datetime,
) -> float:
    cash_out: float = share_lot.sell(share_price, price_dt)
    share_lot.entitlement_sold = entitlement
    asset_price_implied: float = share_price / entitlement
    share_lot.asset_lot.sell(share_lot.units, entitlement, asset_price_implied, price_dt)
    return cash_out
