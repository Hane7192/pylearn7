import random
import time
import arcade
from snake import Snake
from apple import Apple
from pear import Pear
from poop import Poop

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width = 800, height = 600, title = "Super Snake 🐍 V1")
        self.background = arcade.load_texture("pics\grass.jpg")
        self.game_over_background = arcade.load_texture("pics\Game-Over.png")
        self.game_over_sound = arcade.load_sound(":resources:sounds/lose5.wav")
        self.food = Apple(self)
        self.food_type = "apple"
        self.second_food = None
        self.second_food_type = None
        self.snake = Snake(self)
        self.state = "Normal"
        self.timeout = time.time()


    def on_draw(self):
        if self.state == "Normal":
            arcade.start_render()
            arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self._height, self.background)
            self.food.draw()
            if self.second_food != None:
                self.second_food.draw()
            self.snake.draw()       
            score_text = f"Score: {self.snake.score}"
            arcade.draw_text(score_text, self.width - 120 , 20, arcade.csscolor.BLACK, 20, 5, "left", "arial", True)
        
        elif self.state == "Game Over":
            arcade.draw_lrwh_rectangle_textured(0, 0, 800, 600, self.game_over_background)
        
        arcade.finish_render()

    def on_key_release(self, symbol: int, modifiers: int):
       
        if symbol == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1

        elif symbol == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1

        elif symbol == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0

        elif symbol == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0

    def on_update(self, delta_time: float):
        self.snake.move()
        if self.snake.center_x == 10 or self.snake.center_x == self.width-10 or self.snake.center_y == 9 or self.snake.center_y == self.height -9:
            self.state = "Game Over"
            self.on_draw()
            arcade.play_sound(self.game_over_sound,1,0,False,1)
            time.sleep(5)
            exit(0)

        for part in self.snake.body:
            if self.snake.center_x == part["x"] and self.snake.center_y == part["y"]:
                self.state = "Game Over"
                self.on_draw()
                arcade.play_sound(self.game_over_sound,1,0,False,1)
                time.sleep(5)
                exit(0)

        if arcade.check_for_collision(self.snake, self.food):
            self.snake.eat(self.food, self.food_type)
            food_choice = random.randint(1,100)

            if food_choice >= 45:
                self.food = Apple(self)
                self.food_type = "apple"

            elif food_choice >= 15:
                self.food = Poop(self)
                self.food_type = "poop"
            
            else:
                self.food = Pear(self)
                self.food_type = "pear"
            
            if self.second_food == None:
                food_choice = random.randint(1,100)

                if food_choice >= 45:
                    self.second_food = Apple(self)
                    self.second_food_type = "apple"

                elif food_choice >= 15:
                    self.second_food = Poop(self)
                    self.second_food_type = "poop"
                
                else:
                    self.second_food = Pear(self)
                    self.second_food_type = "pear"

            if self.snake.score == 0:
                self.state = "Game Over"
                self.on_draw()
                arcade.play_sound(self.game_over_sound,1,0,False,1)
                time.sleep(5)
                exit(0)

        if self.second_food != None:
            if arcade.check_for_collision(self.snake, self.second_food):
                self.snake.eat(self.second_food, self.second_food_type)
                food_choice = random.randint(1,100)

                if food_choice >= 45:
                    self.second_food = Apple(self)
                    self.second_food_type = "apple"

                elif food_choice >= 15:
                    self.second_food = Poop(self)
                    self.second_food_type = "poop"
                
                else:
                    self.second_food = Pear(self)
                    self.second_food_type = "pear"
                
                if self.snake.score == 0:
                    self.state = "Game Over"
                    self.on_draw()
                    arcade.play_sound(self.game_over_sound,1,0,False,1)
                    time.sleep(5)
                    exit(0)

                


if __name__ == "__main__":
    game = Game()
    arcade.run()
