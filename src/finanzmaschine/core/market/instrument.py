from dataclasses import dataclass


@dataclass(frozen=True)
class Instrument:
    isin: str
    name: str
