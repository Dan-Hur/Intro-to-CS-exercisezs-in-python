##############################################################################
# FILE: asteroids_main.py
# WRITER: Daniel
# EXERCISE: intro2cs2 ex10
# a program that creates ateroid objects
##############################################################################

class Asteroid:
    """ a class that creates asteroid object for asteroids game"""
    def __init__(self, x_loc_spd, y_loc_spd, size):
        self.__x_location = x_loc_spd[0]
        self.__x_speed = x_loc_spd[1]
        self.__y_location = y_loc_spd[0]
        self.__y_speed = y_loc_spd[1]
        self.__size = size
        self.__radius = self.__size * 10 - 5

    def get_x_pos_spd(self):
        """getter that returns x position and speed"""
        return self.__x_location, self.__x_speed

    def get_y_pos_spd(self):
        """getter that returns y position and speed"""
        return self.__y_location, self.__y_speed

    def __calc_distance(self, obj):
        """calculates the distance between the asteroid and a given object"""
        obj_x = obj.get_x_pos_spd()[0]
        obj_y = obj.get_y_pos_spd()[0]
        distance = ((obj_x - self.__x_location) ** 2 +
                    (obj_y - self.__y_location) ** 2) ** 0.5
        return distance

    def get_radius(self):
        """gets the radius of the asteroid"""
        return self.__radius

    def get_size(self):
        """gets the size of the asteroid"""
        return self.__size

    def set_new_location(self, new_x, new_y):
        """sets a new location for the ship"""
        self.__x_location = new_x
        self.__y_location = new_y

    def has_intersection(self, obj):
        """checks if the asteroid had a collision with an object
        :return: True if a collision happened between
        asteroid and object, else: False"""
        obj_r = obj.get_radius()
        distance = self.__calc_distance(obj)
        if distance <= self.__radius + obj_r:
            return True
        return False

    def set_size(self, size):
        """sets a new size for the asteroid"""
        self.__size = size
