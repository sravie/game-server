from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .OutfitItem import OutfitItem

@dataclass
class ShopOutfit:
    outfitId: int = 0
    quality: int = 0
    showInCatalog: int = 0
    specialType: int = 0
    status: int = 0
    howAcquired: int = 0
    createdById: int = 0
    backgroundId: int = 0
    modelId: int = 0

    items: list[OutfitItem] = field(default_factory=list)

    @classmethod
    def unpackFromTuple(cls, data: Sequence) -> ShopOutfit:
        if len(data) != 10:
            raise ValueError(f"Expected 10 values for ShopOutfit, got {len(data)}")

        outfit = cls()
        (
            outfit.outfitId,
            outfit.quality,
            outfit.showInCatalog,
            outfit.specialType,
            outfit.status,
            outfit.howAcquired,
            outfit.createdById,
            outfit.backgroundId,
            outfit.modelId,
            itemsData,
        ) = data

        outfit.items = [
            OutfitItem.unpackFromTuple(itemData)
            for itemData in itemsData
        ]

        return outfit

    def asTuple(self) -> tuple:
        return (
            self.outfitId,
            self.quality,
            self.showInCatalog,
            self.specialType,
            self.status,
            self.howAcquired,
            self.createdById,
            self.backgroundId,
            self.modelId,
            [
                item.asTuple()
                for item in self.items
            ]
        )
