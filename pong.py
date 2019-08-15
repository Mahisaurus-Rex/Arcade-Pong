import arcade 
import time
import random
from chars import *

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Arcade Pong"


class Pong(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        #set initial variables
        p1_x,p1_y=30,30
        p2_x,p2_y=(screen.get_width()-60),30
        ball_x,ball_y=((screen.get_width())/2),((screen.get_height())/2)
        slope_x,slope_y=2,2
        #set constants
        paddle_width = screen.get_width()/64
        paddle_height = screen.get_height()/3.6

        #set initial conditions
        p1_score,p2_score=0,0
        p1=Paddle(p1_x,p1_y)
        p2=Paddle(p2_x,p2_y)
        ball=Ball(ball_x,ball_y)

        pass

    def on_draw(self):
        """ Render the screen. """


        arcade.start_render()
        # Code to draw the screen goes here

    def on_key_press(self, key, modifiers):
        #controls
        #p1
        if pressed[pygame.K_w]:
            p1.up()
        if pressed[pygame.K_s]:
            p1.down()
        #p2
        if pressed[pygame.K_UP]:
            p2.up()
        if pressed[pygame.K_DOWN]:
            p2.down()


def main():
    """ Main method """
    window = Pong()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()