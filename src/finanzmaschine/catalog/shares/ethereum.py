from finanzmaschine.catalog.asset_enum import Asset
from finanzmaschine.catalog.instrument_registry import registry
from finanzmaschine.core.market.share import Share


GB00BLD4ZM24 = registry.register(
    Share(
        isin="GB00BLD4ZM24",
        name="CoinShares Physical Staked Ethereum",
        asset=Asset.ETH,
    )
)
