##############################################################################
# FILE: ship.py
# WRITER: Daniel
# EXERCISE: intro2cs2 ex10
# a program that creates ship objects
##############################################################################

class Ship:
    """a class that creates ship objects for asteroids game"""
    __SHIP_RADIUS = 1
    __SHIP_LIVES = 0
    __SHIP_TORPEDOES = 10

    def __init__(self, x_loc_spd, y_loc_spd, head_dir):
        self.__x_location = x_loc_spd[0]
        self.__x_speed = x_loc_spd[1]
        self.__y_location = y_loc_spd[0]
        self.__y_speed = y_loc_spd[1]
        self.__head_dir = head_dir
        self.__radius = Ship.__SHIP_RADIUS
        self.__lives = Ship.__SHIP_LIVES
        self.__max_torpedoes = Ship.__SHIP_TORPEDOES

    def get_x_pos_spd(self):
        """getter that returns x position and speed"""
        return self.__x_location, self.__x_speed

    def get_y_pos_spd(self):
        """getter that returns y position and speed"""
        return self.__y_location, self.__y_speed

    def get_head_dir(self):
        """gets the heading of the object"""
        return self.__head_dir

    def get_radius(self):
        """gets the radius of the object"""
        return self.__radius

    def get_lives(self):
        """returns the number of lives that the ship has"""
        return self.__lives

    def get_torpedoes_max(self):
        return self.__max_torpedoes

    def set_new_location(self, new_x, new_y):
        """sets a new location for the ship"""
        self.__x_location = new_x
        self.__y_location = new_y

    def set_new_head_dir(self, new_dir):
        """sets a new head direction for the object"""
        self.__head_dir = new_dir

    def set_new_x_speed(self, x_speed):
        """sets a new x speed"""
        self.__x_speed = x_speed

    def set_new_y_speed(self, y_speed):
        """sets a new y speed"""
        self.__y_speed = y_speed

    def set_lives(self, live_num):
        """sets a new amount of lives for the ship"""
        self.__lives = live_num
