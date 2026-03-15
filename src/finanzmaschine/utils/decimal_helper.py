from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def round_to_quanta(x: Decimal, quantum: Decimal) -> Decimal:
    return x.quantize(quantum, rounding=ROUND_HALF_UP)


def round_to_cents(x: Decimal) -> Decimal:
    return round_to_quanta(x, CENT)
