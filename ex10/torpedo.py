##############################################################################
# FILE: torpedo.py
# WRITER: Daniel
# EXERCISE: intro2cs2 ex10
# a program that creates torpedo objects
##############################################################################

class Torpedo:
    """creates torpedo objects for asteroids game"""
    __TORP_RADIUS = 4
    __TORP_TIMER = 0

    def __init__(self, x_loc_spd, y_loc_spd, dir_deg):
        self.__x_location = x_loc_spd[0]
        self.__x_speed = x_loc_spd[1]
        self.__y_location = y_loc_spd[0]
        self.__y_speed = y_loc_spd[1]
        self.__direction = dir_deg
        self.__radius = Torpedo.__TORP_RADIUS
        self.__timer = Torpedo.__TORP_TIMER

    def get_x_pos_spd(self):
        """getter that returns x position and speed"""
        return self.__x_location, self.__x_speed

    def get_y_pos_spd(self):
        """getter that returns y position and speed"""
        return self.__y_location, self.__y_speed

    def get_head_dir(self):
        """gets the heading of the object"""
        return self.__direction

    def get_radius(self):
        """gets the radius of the object"""
        return self.__radius

    def get_timer(self):
        """gets the timer of the torpedo"""
        return self.__timer

    def set_timer(self, time):
        """sets a new timer for the torpedo"""
        self.__timer = time

    def set_new_location(self, new_x, new_y):
        """sets a new location for the ship"""
        self.__x_location = new_x
        self.__y_location = new_y
