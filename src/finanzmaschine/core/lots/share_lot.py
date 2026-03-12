from datetime import datetime

from finanzmaschine.core.lots.asset_lot import AssetLot
from finanzmaschine.core.lots.nominal_lot import NominalLot
from finanzmaschine.core.market.instruments import Share


class ShareLot(NominalLot):
    """
    A nominal lot corresponding to a share-based instrument.

    Units are invariant in share terms: units_open = units_in - units_out_total.
    Each share unit carries an entitlement to an underlying asset.

    Examples of such instruments include ETPs such as ETFs, ETNs, and ETCs.
    """

    def __init__(self, share: Share):
        super().__init__()
        self.share: Share = share
        self.asset_lot = AssetLot(self.share.require_asset())


def buy_share_lot(
    share_lot: ShareLot,
    share_units: float,  # share units to buy
    share_price: float,
    fee: float,
    dt: datetime,
    entitlement: float | None = None,  # asset units per a share unit when buying
) -> float:
    if entitlement is not None:
        asset_units =share_units * entitlement
        asset_price = share_price / entitlement
        share_lot.asset_lot.record_in(
            units=asset_units,  # implied units
            price=asset_price,  # implied price
            fee=fee,
            dt=dt,
        )

    share_lot.record_in(
        units=share_units,
        price=share_price,
        fee=fee,
        dt=dt,
    )

    cash_out = -(share_units * share_price + fee)
    return cash_out


def sell_share_lot_part(
    share_lot: ShareLot,
    share_units: float,  # share units to sell
    share_price: float,
    fee: float,
    dt: datetime,
    entitlement: float | None = None,  # asset units per a share unit when selling
) -> float:
    if (
        entitlement is not None and
        share_lot.asset_lot.lot_record_in is not None
    ):
        asset_units =share_units * entitlement
        asset_price = share_price / entitlement
        share_lot.asset_lot.record_out(
            units=asset_units,  # implied units
            price=asset_price,  # implied price
            fee=fee,
            dt=dt,
        )

    share_lot.record_out(
        units=share_units,
        price=share_price,
        fee=fee,
        dt=dt,
    )

    cash_in = share_units * share_price - fee
    return cash_in
