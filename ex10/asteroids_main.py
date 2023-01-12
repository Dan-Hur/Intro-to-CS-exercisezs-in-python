##############################################################################
# FILE: asteroids_main.py
# WRITER: Daniel
# EXERCISE: intro2cs2 ex10
# a program that creates and runs asteroid game object
##############################################################################

from screen import Screen
import sys
from random import randint
import math as m
from ship import Ship
from asteroid import Asteroid
from torpedo import Torpedo

DEFAULT_ASTEROIDS_NUM = 5
COLLISION_MSG = "your ship collided with an asteroid!"
TORPEDO_TIMEOUT = 200
WIN_HEADLINE = "win"
WIN_MSG = "You Win!!!"
LOSE_HEADLINE = "Game Over"
LOSE_MSG = "You Lose :("
EXIT_HEADLINE = "exit game"
EXIT_MSG = "You chose to quit, bye"


def convert_deg_to_rad(deg):
    """converts degrees to radians"""
    return m.radians(deg)


class GameRunner:
    """ a class that creates an asteroid game object"""

    def __init__(self, asteroids_amount):
        self.__screen = Screen()
        self.__game_start = 1
        self.__points = 0

        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y

        self.__ship = None
        self.__asteroids = []
        self.__asteroid_num = asteroids_amount
        self.__torpedoes = []

    def run(self):
        """runs the game"""
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You should not to change this method!
        self._game_loop()
        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def __rand_position(self):
        """returns a random x,y tuple values, limited by screen size"""
        x_pos = randint(self.__screen_min_x, self.__screen_max_x)
        y_pos = randint(self.__screen_min_y, self.__screen_max_y)
        return x_pos, y_pos

    def __set_ship(self):
        """creates a new ship in the game and draws is"""
        x_pos, y_pos = self.__rand_position()
        speed = 0.0
        self.__ship = Ship((x_pos,speed), (y_pos,speed), 0.0)
        self.__screen.draw_ship(x_pos, y_pos, 0.0)
        return self.__ship

    def __calc_new_x(self, old_x_spot, old_x_spd):
        """calculates a new x position apter movement"""
        x_min = self.__screen_min_x
        x_delta = self.__screen_max_x - x_min
        new_spot = x_min + ((old_x_spot + old_x_spd - x_min) % x_delta)
        return new_spot

    def __calc_new_y(self, old_y_spot, old_y_spd):
        """calculates a new x position apter movement"""
        y_min = self.__screen_min_y
        y_delta = self.__screen_max_y - y_min
        new_spot = y_min + ((old_y_spot + old_y_spd - y_min) % y_delta)
        return new_spot

    def __object_movement(self, object):
        """calculates new position after movement and moves the object"""
        x_loc, x_speed = object.get_x_pos_spd()
        y_loc, y_speed = object.get_y_pos_spd()
        new_x = self.__calc_new_x(x_loc, x_speed)
        new_y = self.__calc_new_y(y_loc, y_speed)
        object.set_new_location(new_x, new_y)

    def __l_r_user_command(self):
        """:return: True if Right, False if Left, -1 otherwise"""
        if self.__screen.is_right_pressed():
            return True
        if self.__screen.is_left_pressed():
            return False
        return -1

    def __head_dir_change(self, user_comm):
        """changes the head direction of our ship"""
        new_dir = self.__ship.get_head_dir()
        if user_comm and user_comm != -1:
            new_dir -= 7
        if not user_comm:
            new_dir += 7
        self.__ship.set_new_head_dir(new_dir)

    def __set_new_x_spd(self, x_speed, head_dir):
        """calculates the new speed for one coordinate"""
        new_speed = x_speed + m.cos(head_dir)
        return new_speed

    def __set_new_y_spd(self, y_speed, head_dir):
        """calculates the new speed for one coordinate"""
        new_speed = y_speed + m.sin(head_dir)
        return new_speed

    def __up_user_comm(self):
        """:return: True if up is pressed, False otherwise"""
        return self.__screen.is_up_pressed()

    def __speed_up(self, up_comm):
        """sets a new speed for the ship if up is pressed"""
        if up_comm:
            x_spd = self.__ship.get_x_pos_spd()[1]
            y_spd = self.__ship.get_y_pos_spd()[1]
            head_dir = convert_deg_to_rad(self.__ship.get_head_dir())
            new_x_spd = self.__set_new_x_spd(x_spd, head_dir)
            new_y_spd = self.__set_new_y_spd(y_spd, head_dir)
            self.__ship.set_new_x_speed(new_x_spd)
            self.__ship.set_new_y_speed(new_y_spd)

    def __check_placement(self, ast_x, ast_y):
        """checks if asteroid placement is valid"""
        if ((ast_x == self.__ship.get_x_pos_spd()[0]) and
                (ast_y == self.__ship.get_y_pos_spd()[0])):
            return True
        return False

    def __get_ast_position(self):
        """returns a valid (x,y) position for asteroid placement"""
        x_pos, y_pos = self.__rand_position()
        while self.__check_placement(x_pos, y_pos):
            x_pos, y_pos = self.__rand_position()
        return x_pos,y_pos

    def _generate_speed(self):
        """generates moving speed for asteroid"""
        speed = randint(-4, 4)
        while speed == 0:
            speed = randint(-4, 4)
        return speed

    def __set_asteroid(self):
        """sets one asteroid and adds it to self"""
        x_pos, y_pos = self.__get_ast_position()
        x_spd, y_spd = self._generate_speed(), self._generate_speed()
        initial_size = 3
        asteroid = Asteroid((x_pos, x_spd), (y_pos, y_spd), initial_size)
        self.__asteroids.append(asteroid)
        self.__screen.register_asteroid(asteroid, initial_size)
        self.__screen.draw_asteroid(asteroid, x_pos, y_pos)

    def __set_n_asteroids(self):
        """sets multiple asteroids"""
        for i in range(self.__asteroid_num):
            self.__set_asteroid()

    def __set_ship_lives(self, life):
        """sets lives for the ship object"""
        self.__ship.set_lives(life)

    def __one_asteroid_ship_collision(self, asteroid):
        """checks if a collision happened between
        asteroid object and ship object, if true - reduce ship lives
        and returns True, else: False"""
        if asteroid.has_intersection(self.__ship):
            ship_life = self.__ship.get_lives()
            ship_life -= 1
            self.__ship.set_lives(ship_life)
            self.__screen.show_message("collision!", COLLISION_MSG)
            self.__screen.remove_life()
            self.__asteroids.remove(asteroid)
            return True
        return False

    def __check_for_asteroid_collision(self):
        """checks collision for every asteroid with the ship object
        if True, remove asteroid and life"""
        for ast in self.__asteroids:
            if self.__one_asteroid_ship_collision(ast):
                self.__screen.unregister_asteroid(ast)

    def __add_points(self, asteroid):
        """adds points to self if a torpedo hit an asteroid"""
        if asteroid.get_size() == 3:
            self.__points += 20
        elif asteroid.get_size() == 2:
            self.__points += 50
        elif asteroid.get_size() == 1:
            self.__points += 100
        self.__screen.set_score(self.__points)

    def __calc_new_ast_speed(self, ast_spd, torp_spd, axis):
        """calculates the new asteroid speed"""
        new_ast_spd = 0
        if axis == "x":
            new_ast_spd = (torp_spd[0] + ast_spd[0]) / \
                          m.sqrt((ast_spd[0] ** 2) + (ast_spd[1] ** 2))
        elif axis == "y":
            new_ast_spd = (torp_spd[1] + ast_spd[1]) / \
                          m.sqrt((ast_spd[0] ** 2) + (ast_spd[1] ** 2))
        return new_ast_spd

    def __add_asteroid(self, asteroid, x_pos, y_pos, size):
        """adds one asteroid"""
        self.__asteroids.append(asteroid)
        self.__screen.register_asteroid(asteroid, size)
        self.__screen.draw_asteroid(asteroid, x_pos, y_pos)

    def __create_2_asteroids(self, asteroid, torpedo, new_size):
        """creates 2 asteroids from one"""
        x_pos, x_spd = asteroid.get_x_pos_spd()
        y_pos, y_spd = asteroid.get_y_pos_spd()
        torp_x_spd = torpedo.get_x_pos_spd()[1]
        torp_y_spd = torpedo.get_y_pos_spd()[1]
        new_x_spd = self.__calc_new_ast_speed((x_spd, y_spd),
                                                (torp_x_spd, torp_y_spd), "x")
        new_y_spd = self.__calc_new_ast_speed((x_spd, y_spd),
                                                (torp_x_spd, torp_y_spd), "y")
        asteroid1 = Asteroid((x_pos, new_x_spd),
                             (y_pos, -1 * new_y_spd), new_size)
        asteroid2 = Asteroid((x_pos, -1 * new_x_spd),
                             (y_pos, new_y_spd), new_size)
        self.__add_asteroid(asteroid1, x_pos, y_pos, new_size)
        self.__add_asteroid(asteroid2, x_pos, y_pos, new_size)

    def __split_asteroid(self, asteroid, torpedo):
        """splits a collided asteroid based on its'
        size, if the size is 1: remove it"""
        if asteroid.get_size() == 3:
            new_size = 2
            self.__create_2_asteroids(asteroid, torpedo, new_size)
        elif asteroid.get_size() == 2:
            new_size = 1
            self.__create_2_asteroids(asteroid, torpedo, new_size)
        self.__screen.unregister_asteroid(asteroid)
        self.__asteroids.remove(asteroid)

    def __one_asteroid_torp_collision(self, asteroid, torpedo):
        """checks if a collision happened between
                asteroid object and torpedo object, if true - blows asteroid
                and returns True, else: False"""
        if asteroid.has_intersection(torpedo):
            self.__add_points(asteroid)
            self.__split_asteroid(asteroid, torpedo)
            self.__screen.unregister_torpedo(torpedo)
            self.__torpedoes.remove(torpedo)

    def __asts_torps_collision(self):
        """checks for collision across all asteroids and torpedoes"""
        for ast in self.__asteroids:
            for torp in self.__torpedoes:
                self.__one_asteroid_torp_collision(ast, torp)

    def __one_torp_life_cycle(self, torpedo):
        """checks if the torpedo should stay on screen or not,
         based on timeout timer"""
        torpedo_timer = torpedo.get_timer()
        if torpedo_timer < TORPEDO_TIMEOUT:
            torpedo_timer += 1
            torpedo.set_timer(torpedo_timer)
        else:
            self.__torpedoes.remove(torpedo)
            self.__screen.unregister_torpedo(torpedo)

    def __calc_torpedo_speed(self):
        """calculates torpedo speed"""
        x_spd = self.__ship.get_x_pos_spd()[1]
        y_spd = self.__ship.get_y_pos_spd()[1]
        ship_head = convert_deg_to_rad(self.__ship.get_head_dir())
        torp_spd_x = x_spd + 2 * m.cos(ship_head)
        torp_spd_y = y_spd + 2 * m.sin(ship_head)
        return torp_spd_x, torp_spd_y

    def __make_shot(self):
        """shoots a torpedo"""
        if self.__screen.is_space_pressed() and len(self.__torpedoes) <\
                self.__ship.get_torpedoes_max():

            x_pos = self.__ship.get_x_pos_spd()[0]
            y_pos = self.__ship.get_y_pos_spd()[0]
            x_spd, y_spd = self.__calc_torpedo_speed()
            heading = self.__ship.get_head_dir()
            torpedo = Torpedo((x_pos, x_spd), (y_pos, y_spd), heading)
            self.__torpedoes.append(torpedo)
            self.__screen.register_torpedo(torpedo)
            self.__screen.draw_torpedo(torpedo, x_pos, y_pos, heading)

    def __start_of_game(self):
        """initiates all objects at the start of the game"""
        if self.__game_start == 1:
            self.__set_ship()
            self.__set_ship_lives(3)
            self.__set_n_asteroids()
            self.__game_start = 0

    def __run_ship(self):
        """runs the ship inside game loop"""
        l_r_comm = self.__l_r_user_command()
        up_comm = self.__screen.is_up_pressed()
        self.__speed_up(up_comm)
        self.__head_dir_change(l_r_comm)

    def __move_objects(self):
        """moves objects in our game"""
        # moves ship
        self.__object_movement(self.__ship)
        self.__screen.draw_ship(self.__ship.get_x_pos_spd()[0],
                                self.__ship.get_y_pos_spd()[0],
                                self.__ship.get_head_dir())
        # moves asteroids
        for ast in self.__asteroids:
            self.__object_movement(ast)
            self.__screen.draw_asteroid(ast, ast.get_x_pos_spd()[0],
                                        ast.get_y_pos_spd()[0])
        # moves torpedoes
        for torp in self.__torpedoes:
            self.__object_movement(torp)
            self.__screen.draw_torpedo(torp, torp.get_x_pos_spd()[0],
                                       torp.get_y_pos_spd()[0],
                                       torp.get_head_dir())
            self.__one_torp_life_cycle(torp)

    def __end_game(self):
        """checks all conditions for ending the game
        :return: True if end game conditions are made, False otherwise"""
        if not self.__asteroids:
            self.__screen.show_message(WIN_HEADLINE, WIN_MSG)
            return True
        if not self.__ship.get_lives():
            self.__screen.show_message(LOSE_HEADLINE, LOSE_MSG)
            return True
        if self.__screen.should_end():
            self.__screen.show_message(EXIT_HEADLINE, EXIT_MSG)
            return True
        return False

    def _game_loop(self):
        """runs the game loop"""
        self.__start_of_game()
        self.__run_ship()
        self.__check_for_asteroid_collision()
        self.__make_shot()
        self.__asts_torps_collision()
        self.__move_objects()
        if self.__end_game():
            self.__screen.end_game()
            sys.exit()


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
