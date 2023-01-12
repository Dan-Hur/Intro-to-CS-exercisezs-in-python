##############################################################################
# FILE: board.py
# WRITER:Daniel
# EXERCISE: intro2cs2 ex9
# a class representing a board in rush hour game
##############################################################################


class Board:
    """
    Board class creates objects that represent a game board for Rush Hour game
    """
    __BOARD_HEIGHT = 7
    __BOARD_WIDTH = 7
    __TARGET_ROW = 3
    __TARGET_COL = 7
    __TARGET = (3, 7)
    __FIRST_ROW = 0
    __FIRST_COL = 0
    __BLANK = " "
    __EXIT = " >] "

    def __init__(self):
        self.__cars = []
        self.__taken_cells = []
        self.__height = Board.__BOARD_HEIGHT
        self.__width = Board.__BOARD_WIDTH

    def __create_mat_from_lst(self, lst):
        """creates a matrix with 7 rows from the cell_list function output"""
        new_lst = []
        for i in range(self.__height):
            row = []
            for coord in lst:
                if coord[0] == i:
                    row.append(coord)
            new_lst.append(row)
        return new_lst

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        out_str = ""
        for row in self.__create_mat_from_lst(self.cell_list()):
            for col in row:
                if self.cell_content(col):
                    out_str += (Board.__BLANK  +
                                self.cell_content(col) + Board.__BLANK)
                else:
                    out_str += " _ "
            # the next conditions determines the target coordinates
            # if there is a car in the target coord - prints it's name
            # otherwise, prints target string representation
            if row[0][0] == 3 and self.cell_content(self.target_location()):
                out_str += (Board.__BLANK +
                            self.cell_content(self.target_location()) +
                            Board.__BLANK)
            elif row[0][0] == 3:
                out_str += Board.__EXIT
            out_str += "\n"
        return out_str

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        ret_lst = []
        for i in range(self.__height):
            for j in range(self.__width):
                ret_lst.append((i,j))
                if i == Board.__TARGET_ROW and j == Board.__TARGET_COL - 1:
                    ret_lst.append(self.target_location())
        return ret_lst

    def ___car_moves(self, car):
        """for a car object, returns a list of tuples with the name
        of the car and its possible moves"""
        items = car.possible_moves().items()
        car_name = car.get_name()
        ret_lst = []
        for i in items:
            ret_lst.append((car_name, i[0], i[1]))
        return ret_lst


    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        moves_lst = []
        if self.__cars == []:
            return []
        for car in self.__cars:
            moves_lst.append(self.___car_moves(car))
        return moves_lst

    def target_location(self):
        """
        This function returns the coordinates of
         the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        #In this board, returns (3,7)
        return Board.__TARGET

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        for car in self.__cars:
            if coordinate in car.car_coordinates():
                return car.get_name()

        return None

    def __multi_cell_contents(self, coords):
        """ checks for a list of coordinates if each coordinate is empty
        :param coords: a list of coordinates
        :return: False if cell is empty, True if not empty"""
        for co in coords:
            if self.cell_content(co):
                return True
        return False

    def __coord_out_of_bound(self, coord):
        """checks if a coordinate is out of bounds
        :param coord: tuple of (row,col) of the coordinate to check
        :return: True in out of bounds, False if not"""
        if coord[0] >= self.__height:
            return True
        if coord[1] >= self.__width:
            return True
        if coord[0] < Board.__FIRST_ROW:
            return True
        if coord[1] < Board.__FIRST_COL:
            return True
        return False

    def __coords_out_of_bound(self, coords):
        """checks if a coordinate is out of bounds
        :param coords: a list of coordinates
        :return: True in out of bounds, False if not"""
        for coord in coords:
            if coord == (3,7):
                return coord
            if self.__coord_out_of_bound(coord):
                return True
        return False

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        
        moves = self.possible_moves()
        
        if car in self.__cars:
            return False
        if self.__multi_cell_contents(car.car_coordinates()):
            return False
        if self.__coords_out_of_bound(car.car_coordinates()):
            return False

        self.__cars.append(car)
        return True
    
    def __convert_name_to_car(self, name):
        """returns the car associated with the given name, if 
        not found returns None"""
        for car in self.__cars:
            if car.get_name() == name:
                return car
        return None

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        car = self.__convert_name_to_car(name)
        if car is None:
            return False
        possible_moves = car.movement_requirements(movekey)
        if self.__multi_cell_contents(possible_moves):
            print("a car is in the way")
            return False
        if (self.__coords_out_of_bound(possible_moves) and
                self.__coords_out_of_bound(possible_moves) !=
                self.target_location()):
            print("out of bounds")
            return False
        return car.move(movekey)
