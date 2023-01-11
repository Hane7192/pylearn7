import random
import arcade


class Missiles(arcade.Sprite):
    def __init__(self, game):
        super().__init__("missile.png")
        self.center_x = game.width // 2
        self.center_y = 100
        self.width = 130
        self.height = 130
        self.angle = 40
        self.speed = 8

class Airplane(arcade.Sprite):
    def __init__(self , game):
        super().__init__("airplane.png")
        self.center_x = 0
        self.center_y = random.randint(3*game.height//5, 4*game.height//5)
        self.width = 280
        self.height = 280
        self.speed_x = 4
        self.speed_y = 1


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width= 1000, height=800, title="PS752")
        arcade.set_background_color(arcade.color.SPACE_CADET)
        self.background = arcade.load_texture("bloody_ background.jpg")
        self.missiles = Missiles(self)
        self.airplane = Airplane(self)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self._height, self.background)
        self.missiles.draw()
        self.airplane.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        
        if symbol == 97: #left
           self.missiles.center_x -= self.missiles.speed
        elif symbol == 100: #right
           self.missiles.center_x += self.missiles.speed

    def on_update(self, delta_time: float):
        self.airplane.center_x += self.airplane.speed_x
        self.airplane.center_y += self.airplane.speed_y

window = Game()
arcade.run()