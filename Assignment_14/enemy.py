import random
import arcade

class Enemy(arcade.Sprite):
    def __init__(self , game):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = random.randint(30, game.width-30)
        self.center_y = game.height - 60
        self.angle = 180
        self.width = 60
        self.height = 60
        self.speed_y = game.enemy_speed
        
    def move(self):
        self.center_y -= self.speed_y