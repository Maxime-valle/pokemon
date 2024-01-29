# pokedex.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QInputDialog

class Pokedex:
    def __init__(self):
        self.pokemon_data = {}

    def display_pokedex(self):
        if not self.pokemon_data:
            print("Le Pokédex est vide!")
        else:
            print("Pokédex:")
            for name, data in self.pokemon_data.items():
                print(f"{name} - Type: {data['type']}, Defense: {data['defense']}, Attaque: {data['attack_power']}, PV: {data['hp']}")

    def add_to_pokedex(self, pokemon):
        self.pokemon_data[pokemon.name] = {
            "type": pokemon.type,
            "defense": pokemon.defense,
            "attack_power": pokemon.attack_power,
            "hp": pokemon.hp
        }

    def update_pokedex_display(self):
        if not self.pokemon_data:
            print("Le Pokédex est vide!")
        else:
            print("Pokédex:")
            for name, data in self.pokemon_data.items():
                print(f"{name} - Type: {data['type']}, Defense: {data['defense']}, Attaque: {data['attack_power']}, PV: {data['hp']}")


class PokedexApp(QWidget):
    def __init__(self):
        super().__init__()

        self.pokedex = Pokedex()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Pokédex')
        self.setGeometry(100, 100, 400, 400)

        self.setStyleSheet("""
            QLabel {
                font-size: 18px;
                color: #333;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 15px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
            }
            #pokemon_info_label {
                font-size: 16px;
                color: #007BFF;  /* Couleur bleue */
            }
        """)

        self.pokemon_info_label = QLabel('Informations du Pokémon:', self)
        self.pokemon_info_label.setObjectName("pokemon_info_label")

        self.add_button = QPushButton('Ajouter au Pokédex', self)
        self.add_button.clicked.connect(self.add_pokemon_to_pokedex)

        self.pokedex_display = QTextEdit(self)
        self.pokedex_display.setReadOnly(True)

        layout = QVBoxLayout(self)
        layout.addWidget(self.pokemon_info_label)
        layout.addWidget(self.add_button)
        layout.addWidget(self.pokedex_display)

    def add_pokemon_to_pokedex(self):
        name, ok = QInputDialog.getText(self, 'Ajouter un Pokémon', 'Nom du Pokémon:')
        if ok:
            type, ok = QInputDialog.getText(self, 'Ajouter un Pokémon', 'Type du Pokémon:')
            if ok:
                defense, ok = QInputDialog.getInt(self, 'Ajouter un Pokémon', 'Défense du Pokémon:')
                if ok:
                    attack_power, ok = QInputDialog.getInt(self, 'Ajouter un Pokémon', 'Puissance d\'attaque du Pokémon:')
                    if ok:
                        hp, ok = QInputDialog.getInt(self, 'Ajouter un Pokémon', 'Points de vie du Pokémon:')
                        if ok:
                            new_pokemon = Pokemon(name, type, defense, attack_power, hp)
                            self.pokedex.add_to_pokedex(new_pokemon)
                            self.update_pokedex_display()

    def update_pokedex_display(self):
        if not self.pokedex.pokemon_data:
            self.pokedex_display.setPlainText("Le Pokédex est vide!")
        else:
            text = "Pokédex:\n"
            for name, data in self.pokedex.pokemon_data.items():
                text += f"{name} - Type: {data['type']}, Defense: {data['defense']}, Attaque: {data['attack_power']}, PV: {data['hp']}\n"
            self.pokedex_display.setPlainText(text)


# Si vous exécutez ce module directement, vous pouvez tester votre interface graphique.
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    pokedex_app = PokedexApp()
    pokedex_app.show()
    sys.exit(app.exec_())
