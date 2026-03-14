from collections import defaultdict
from typing import DefaultDict, Dict, List

from finanzmaschine.catalog.asset_enum import Asset
from finanzmaschine.core.market.instrument import Instrument


class InstrumentRegistry:

    def __init__(self):
        self._by_isin: Dict[str, Instrument] = {}
        self._by_asset: DefaultDict[Asset, List[Instrument]] = defaultdict(list)

    def register(self, instrument: Instrument) -> Instrument:

        if instrument.isin in self._by_isin:
            raise ValueError(f"Duplicate instrument {instrument.isin}")

        self._by_isin[instrument.isin] = instrument

        asset = getattr(instrument, "asset", None)
        if asset is not None:
            self._by_asset[asset].append(instrument)

        return instrument

    def get_by_isin(self, isin: str) -> Instrument:
        return self._by_isin.get(isin)

    def get_by_asset(self, asset: Asset) -> List[Instrument]:
        return self._by_asset.get(asset, [])


registry = InstrumentRegistry()
