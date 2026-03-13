from finanzmaschine.catalog import registry
from finanzmaschine.catalog.asset_enum import Asset

instrument = registry.get_by_isin("GB00BLD4ZM24")
print(instrument)
# Share(isin='GB00BLD4ZM24', name='CoinShares Physical Staked Ethereum', asset=<Asset.ETH: 'ETH'>)

instrument = registry.get_by_asset(Asset.ETH)
print(instrument)
# [Share(isin='GB00BLD4ZM24', name='CoinShares Physical Staked Ethereum', asset=<Asset.ETH: 'ETH'>)]
