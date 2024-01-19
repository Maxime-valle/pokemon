import pytmx
import pyscroll
from screen import Screen
from entity import Entity
from tool import tool

class GameMap:
    def __init__(self, screen: Screen):
        self.screen = screen
        self.tmx_data = None
        self.map_layer = None
        self.group = None
        self.switch_map("Map")

    def switch_map(self, map_name: str):
        self.tmx_data = pytmx.load_pygame(f"Map.tmx")
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=7)

    def add_player(self, player):
        self.group.add(player, layer=player._layer)

    def update(self):
        self.group.update()
        self.group.draw(self.screen.get_display())