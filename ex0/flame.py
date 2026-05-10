#!/usr/bin/env python3

from .creature_factory import CreatureFactory
from .creature import Creature, Flameling, Pyrodon


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling("Flameling", "Fire")

    def create_evolved(self) -> Creature:
        return Pyrodon("Pyrodon", "Fire/Flying")
