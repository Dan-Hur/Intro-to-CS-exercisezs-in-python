##############################################################################
# FILE: car.py
# WRITER:Daniel
# EXERCISE: intro2cs2 ex9 
# a class representing cars in rush hour game
##############################################################################


class Car:
    """
    car class creates objects representing cars in a rush our game
    """

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.__name = name
        self.__length = length
        self.__loc = location
        self.__orientation = orientation


    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        coord_lst = []
        first_coord = self.__loc
        first_coord_row = first_coord[0]
        first_coord_col = first_coord[1]
        coord_lst.append(first_coord)

        if self.__length == 1:
            return coord_lst
        elif self.__orientation == 0:
            for i in range(1, self.__length):
                coord_lst.append((first_coord_row + i, first_coord_col))
        elif self.__orientation == 1:
            for i in range(1, self.__length):
                coord_lst.append((first_coord_row, first_coord_col + i))

        return coord_lst

    def possible_moves(self):
        """
        :return: A dictionary of strings describing
                 possible movements permitted by this car.
        """

        UP_MSG = "moves the car up"
        DOWN_MSG = "moves the car down"
        LEFT_MSG = "moves the car left"
        RIGHT_MSG = "moves the car right"
        vertical_moves = {"u": UP_MSG, "d": DOWN_MSG}
        horizontal_moves = {"l": LEFT_MSG, "r": RIGHT_MSG}

        if self.__orientation == 0:
            return vertical_moves
        if self.__orientation == 1:
            return horizontal_moves

    def __determine_car_boundaries(self):
        """
        :return: a list containing cat rear location and car front location
        """
        car_rear = self.car_coordinates()[0]
        car_front = self.car_coordinates()[-1]
        if car_rear == car_front:
            return [car_rear]
        else:
            return [car_rear, car_front]

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty
                 in order for this move to be legal.
        """
        car_bounds = self.__determine_car_boundaries()
        car_rear = car_bounds[0]
        car_rear_row = car_rear[0]
        car_rear_col = car_rear[1]
        car_front = car_bounds[-1]
        car_front_row = car_front[0]
        car_front_col = car_front[1]
        ret_lst = []
        if movekey == "u":
            ret_lst.append((car_rear_row - 1, car_rear_col))
        if movekey == "d":
            ret_lst.append((car_front_row + 1, car_front_col))
        if movekey == "r":
            ret_lst.append((car_front_row, car_front_col + 1))
        if movekey == "l":
            ret_lst.append((car_rear_row, car_rear_col - 1))
        return ret_lst

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        car_coord = self.__loc
        if movekey not in self.possible_moves():
            print("not a valid direction")
            return False
        else:
            if movekey == "u":
                self.__loc = (car_coord[0] - 1, car_coord[1])
            if movekey == "d":
                self.__loc = (car_coord[0] + 1, car_coord[1])
            if movekey == "r":
                self.__loc = (car_coord[0], car_coord[1] + 1)
            if movekey == "l":
                self.__loc = (car_coord[0], car_coord[1] - 1)
        return True

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.__name



