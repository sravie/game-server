from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

@dataclass
class OutfitItem:
    itemId: int = 0
    color1: int = 0
    color2: int = 0
    price: int = 0
    goldPrice: int = 0
    memberGoldPrice: int = None

    # This is used by the server-side only.
    itemType: str = ""

    def __post_init__(self):
        if self.memberGoldPrice is None:
            self.memberGoldPrice = self.goldPrice

    @classmethod
    def unpackFromTuple(cls, data: Sequence[int]) -> OutfitItem:
        if len(data) != 6:
            raise ValueError(f"Expected 6 values for OutfitItem, got {len(data)}")

        return cls(*data)

    def asTuple(self) -> tuple[int, ...]:
        return (
            self.itemId,
            self.color1,
            self.color2,
            self.price,
            self.goldPrice,
            self.memberGoldPrice
        )
