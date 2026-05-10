#!/usr/bin/env python3

from ex0 import FlameFactory, AquaFactory
from ex0.creature_factory import CreatureFactory
from ex0.creature import Creature


def test_factory(factory: CreatureFactory) -> None:
    base: Creature = factory.create_base()
    evolved: Creature = factory.create_evolved()

    print(base.describe())
    print(base.attack())

    print(evolved.describe())
    print(evolved.attack())


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    c1: Creature = factory1.create_base()
    c2: Creature = factory2.create_base()

    print(c1.describe())
    print("vs.")
    print(c2.describe())
    print("fight!")

    print(c1.attack())
    print(c2.attack())


if __name__ == "__main__":
    flame_factory: CreatureFactory = FlameFactory()
    aqua_factory: CreatureFactory = AquaFactory()

    print("Testing factory")
    test_factory(flame_factory)

    print("\nTesting factory")
    test_factory(aqua_factory)

    print("\nTesting battle")
    battle(flame_factory, aqua_factory)
