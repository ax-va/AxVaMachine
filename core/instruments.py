from dataclasses import dataclass, field
from typing import Dict

from core.exchange import Exchange


@dataclass(frozen=True)
class Instrument:
    isin: str
    name: str
    local_ids: Dict[str, str] = field(default_factory=dict),
    tickers: Dict[Exchange, str] = field(default_factory=dict),


@dataclass(frozen=True)
class ShareInstrument:
    base: Instrument
    asset_name: str = ""

    @property
    def isin(self) -> str:
        return self.base.isin

    @property
    def name(self) -> str:
        return self.base.name

    @property
    def local_ids(self) -> Dict[str, str]:
        return self.base.local_ids

    @property
    def tickers(self) -> Dict[Exchange, str]:
        return self.base.tickers


@dataclass(frozen=True)
class Etp(ShareInstrument):
    pass


COINSHARES_PHYSICAL_STAKED_ETH = Etp(
    base=Instrument(
        isin="GB00BLD4ZM24",
        name="CoinShares Physical Staked Ethereum",
        local_ids={"WKN": "A3GQ2N"},
        tickers={Exchange.EIX: "CETH"},
    ),
    asset_name= "ETH",
)
