from typing import List, Optional
from pakuri import Pakuri


class Pakudex:
    def __init__(self, capacity: int = 20):
        self.capacity = capacity
        self._creatures: List[Pakuri] = []

    def get_size(self) -> int:
        return len(self._creatures)

    def get_capacity(self) -> int:
        return self.capacity

    def get_species_array(self) -> Optional[List[str]]:
        if not self._creatures:
            return None
        return [p.get_species() for p in self._creatures]

    def _find_index(self, species: str) -> int:
        for i, p in enumerate(self._creatures):
            if p.get_species() == species:
                return i
        return -1

    def get_stats(self, species: str) -> Optional[List[int]]:
        idx = self._find_index(species)
        if idx == -1:
            return None
        p = self._creatures[idx]
        return [p.get_attack(), p.get_defense(), p.get_speed()]

    def sort_pakuri(self) -> None:
        self._creatures.sort(key=lambda p: p.get_species())

    def add_pakuri(self, species: str) -> bool:
        if self.get_size() >= self.capacity:
            return False
        if self._find_index(species) != -1:
            return False
        self._creatures.append(Pakuri(species))
        return True

    def evolve_species(self, species: str) -> bool:
        idx = self._find_index(species)
        if idx == -1:
            return False
        self._creatures[idx].evolve()
        return True
