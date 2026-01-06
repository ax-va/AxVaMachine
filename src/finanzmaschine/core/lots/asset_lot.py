import datetime

from finanzmaschine.core.lots.base_lot import BaseLot
from finanzmaschine.core.lots.base_lot_record import BaseLotRecord
from finanzmaschine.core.market.asset import Asset


class AssetLot(BaseLot[BaseLotRecord]):
    record_cls = BaseLotRecord

    def __init__(self, asset: Asset):
        super().__init__()
        self.asset: Asset = asset
