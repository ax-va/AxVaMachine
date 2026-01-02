from enum import Enum

class Mode(Enum):
    VACUUM = "VACUUM"
    BATTERY = "BATTERY"
    HUNTER = "HUNTER"


def detect_mode(price, vacuum_limit, battery_upper) -> Mode:
    if price <= vacuum_limit:
        return Mode.VACUUM
    elif price <= battery_upper:
        return Mode.BATTERY
    else:
        return Mode.HUNTER


if __name__ == "__main__":
    local_high = 4000
    profit_p = 0.2  # take profit
    loss_p = profit_p * 2
    vacuum_limit = local_high * (1 - loss_p)
    print("vacuum_limit:", vacuum_limit)

    etp_price_bid = 2610  # sell
    etp_price_ask = 2613  # buy
    etp_price_spread = etp_price_ask - etp_price_bid
    print("etp_price_spread:", etp_price_spread)

    battery_upper = vacuum_limit / (1 - profit_p)
    print("battery_upper:", battery_upper)

    mode = detect_mode(etp_price_ask, vacuum_limit, battery_upper)
    print("mode:", mode)

    limit_order = etp_price_ask * (1 + profit_p)
    print("limit_order:", limit_order)

    stop_loss = max(vacuum_limit, etp_price_ask * (1 - loss_p))
    print("stop_loss:", stop_loss)

    cash_input = 0
    etp_amount_bought = cash_input / etp_price_ask
    print("etp_amount_bought:", etp_amount_bought)
