import time
import arcade
from snake import Snake
from apple import Apple


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width = 800, height = 600, title = "Super Snake 🐍 V1")
        self.background = arcade.load_texture("pics\grass.jpg")
        self.game_over_background = arcade.load_texture("pics\Game-Over.png")
        self.game_over_sound = arcade.load_sound(":resources:sounds/lose5.wav")
        self.food = Apple(self)
        self.food_type = "apple"
        self.snake = Snake(self)
        self.state = "Normal"
        self.timeout = time.time()

    def on_draw(self):
        if self.state == "Normal":
            arcade.start_render()
            arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self._height, self.background)
            self.food.draw()
            self.snake.draw()       
            score_text = f"Score: {self.snake.score}"
            arcade.draw_text(score_text, self.width - 120 , 20, arcade.csscolor.BLACK, 20, 5, "left", "arial", True)
        
        elif self.state == "Game Over":
            arcade.draw_lrwh_rectangle_textured(0, 0, 800, 600, self.game_over_background)
        
        arcade.finish_render()   

    def on_update(self, delta_time: float):
        # self.snake.move()
        if self.snake.center_x < self.food.center_x:
                self.snake.change_x = 1
                self.snake.change_y = 0
                self.snake.move()

        elif self.snake.center_x > self.food.center_x:
            self.snake.change_x = -1
            self.snake.change_y = 0
            self.snake.move()
        

        if self.snake.center_y < self.food.center_y:
            self.snake.change_x = 0
            self.snake.change_y = 1
            self.snake.move()

        elif self.snake.center_y > self.food.center_y:
                self.snake.change_x = 0
                self.snake.change_y = -1
                self.snake.move()
          

        if arcade.check_for_collision(self.snake, self.food):
            self.snake.eat(self.food, self.food_type)
            self.food = Apple(self)
            self.food_type = "apple"

        if self.snake.center_x == 10 or self.snake.center_x == self.width-10 or self.snake.center_y == 9 or self.snake.center_y == self.height -9:
            self.state = "Game Over"
            self.on_draw()
            arcade.play_sound(self.game_over_sound,1,0,False,1)
            time.sleep(5)
            exit(0)

        # for part in self.snake.body:
        #     if self.snake.center_x == part["x"] and self.snake.center_y == part["y"]:
        #         self.state = "Game Over"
        #         self.on_draw()
        #         arcade.play_sound(self.game_over_sound,1,0,False,1)
        #         time.sleep(5)
        #         exit(0)
        
        # if self.snake.score == 0:
        #         self.state = "Game Over"
        #         self.on_draw()
        #         arcade.play_sound(self.game_over_sound,1,0,False,1)
        #         time.sleep(5)
        #         exit(0)

if __name__ == "__main__":
    game = Game()
    arcade.run()
