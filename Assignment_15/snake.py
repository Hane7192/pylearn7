import arcade

class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 30
        self.height = 30
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.color1 = arcade.color.DARK_KHAKI
        self.color2 = arcade.color.LIGHT_BROWN
        self.change_x = 0
        self.change_y = 0
        self.speed = 3
        self.score = 0
        self.body = []

    def draw(self):
        i = 0
        arcade.draw_circle_filled(self.center_x, self.center_y, 21, self.color1)
        
        for part in self.body:
            if i%2 == 0:
                arcade.draw_circle_filled(part["x"], part["y"], 21, self.color2)
                
            else :
                arcade.draw_circle_filled(part["x"], part["y"], 21, self.color1)
            i += 1

    def move(self):
        self.body.append({"x": self.center_x, "y": self.center_y})
        if len(self.body)> self.score:
            self.body.pop(0)
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed
    
    def eat(self, food , food_type):
        del food

        if food_type == "apple":
            self.score += 1
        elif food_type == "pear":
            self.score += 2
        elif food_type == "poop":
            self.score -= 1
        