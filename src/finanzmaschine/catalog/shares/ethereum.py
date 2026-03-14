from finanzmaschine.catalog import registry
from finanzmaschine.catalog.asset_enum import Asset
from finanzmaschine.core.market.share import Share

GB00BLD4ZM24 = Share(
    isin="GB00BLD4ZM24",
    name="CoinShares Physical Staked Ethereum",
    asset=Asset.ETH,
)

registry.register(GB00BLD4ZM24)

