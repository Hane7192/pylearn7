import random
import arcade

class Apple(arcade.Sprite):
    def __init__(self, game):
        super().__init__("pics\_apple.png")
        self.width = 50
        self.height = 70
        self.center_x = random.randint(15 , game.width - 15)
        self.center_y = random.randint(15 , game.height - 15)
        self.change_x = 0
        self.change_y = 0
