from finanzmaschine.catalog import registry
from finanzmaschine.catalog.asset_enum import Asset
from finanzmaschine.core.market.etp import Etp

COINSHARES_PHYSICAL_STAKED_ETHEREUM = Etp(
    isin="GB00BLD4ZM24",
    name="CoinShares Physical Staked Ethereum",
    asset=Asset.ETH,
)

registry.register(COINSHARES_PHYSICAL_STAKED_ETHEREUM)

