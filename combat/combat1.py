import pygame
import sys
import os
import json

MIN_DAMAGE = 10
MAX_DAMAGE = 30

class Pokemon:
    def __init__(self, nom, points_de_vie, attaque):
        self._nom = nom
        self._points_de_vie = points_de_vie
        self._attaque = attaque

    @property
    def nom(self):
        return self._nom

    @property
    def points_de_vie(self):
        return self._points_de_vie

    @property
    def attaque(self):
        return self._attaque

    def est_vaincu(self):
        return self.points_de_vie <= 0

    def attaquer(self, autre_pokemon):
        if not self.est_vaincu():
            autre_pokemon.points_de_vie -= self.attaque
            print(f"{self.nom} attaque {autre_pokemon.nom} et inflige {self.attaque} points de dégâts.")

    def to_dict(self):
        return {
            "nom": self.nom,
            "points_de_vie": self.points_de_vie,
            "attaque": self.attaque
        }

    def __str__(self):
        return f"{self.nom} (PV: {self.points_de_vie}, Attaque: {self.attaque})"

def combat(pokemon1, pokemon2):
    while not pokemon1.est_vaincu() and not pokemon2.est_vaincu():
        pokemon1.attaquer(pokemon2)
        if not pokemon2.est_vaincu():
            pokemon2.attaquer(pokemon1)

    if pokemon1.est_vaincu():
        print(f"{pokemon2.nom} a gagné le combat.")
    else:
        print(f"{pokemon1.nom} a gagné le combat.")

def main():
    doexys = Pokemon("Doexys", 100, 25)
    giratina = Pokemon("Giratina", 120, 20)

    combat(doexys, giratina)

    pokemon_data = [pokemon.to_dict() for pokemon in [doexys, giratina]]
    json_data = json.dumps(pokemon_data, indent=4)

    print(json_data)

if __name__ == "__main__":
    main()