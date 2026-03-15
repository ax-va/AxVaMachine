from finanzmaschine.core.lots.base_lot import BaseLot
from finanzmaschine.catalog.asset_enum import Asset


class AssetLot(BaseLot):
    """
    A lot representing effective exposure to an underlying asset.

    Unit balance is not invariant and may change over time due to
    entitlement adjustments, fees, or asset-specific mechanics.

    Asset units may become negative.
    This does NOT represent a short position, but rather
    a mismatch between share exposure and implied asset exposure.

    Asset units and price are defined by the formulas:

    asset_units = share_units * entitlement,
    asset_price = share_price / entitlement,

    where entitlement is a time-dependent mapping that determines
    how many asset units are represented by a single share unit.
    """

    def __init__(self, asset: Asset):
        super().__init__()
        self.asset: Asset = asset
