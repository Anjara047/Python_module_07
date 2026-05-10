#!/usr/bin/env python3`

from .creature_factory import CreatureFactory
from .creature import Creature, Aquabub, Torragon


class AquaFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Aquabub("Aquabub", "Water")

    def create_evolved(self) -> Creature:
        return Torragon("Torragon", "Water")
