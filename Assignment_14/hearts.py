import arcade

class Hearts(arcade.Sprite):
    def __init__(self, x):
        super().__init__("pics\heart.png")
        self.center_x = 30*x
        self.center_y = 60
        self.width = 35
        self.height = 30

    # def point(self):
    #     self.point = 0