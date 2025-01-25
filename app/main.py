
from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100, hidden:
                 bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    @classmethod
    def remove(cls) -> None:

        cls.alive = [animal for animal in cls.alive if animal.health >= 0]

    def die(self) -> None:
        self.health = 0
        Animal.remove()


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if (isinstance(animal, Herbivore)
                and animal.health > 0 and not animal.hidden):
            animal.health -= 50
            if animal.health <= 0:
                animal.die()
