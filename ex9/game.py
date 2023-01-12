##############################################################################
# FILE: game.py
# WRITER:Daniel
# EXERCISE: intro2cs2 ex9
# a class representing the rush hour game, and a program that runs it
##############################################################################
import json

CAR_NAMES = ["Y", "B", "O", "W", "G", "R"]
DIRECTIONS = "udlr"
BAD_INPUT_MSG = "Bad input"
BAD_NAME_MSG = "Incorrect car name, use either: Y, B, O, W, G or R: "
BAD_MOVE_MSG = "Incorrect move, use either: u, d, l or r: "
SEP = ","
INPUT_MSG = "Please select a car to move and the move direction: "
STAR_MSG = "Let's Start!!"
GAME_OVER_MSG = "Game Over"
WIN_MSG = "You Win!!!"
EXIT_GAME = "!"
ORIENTATIONS = [0,1]
INSERT_FILE_MSG = "Please enter a file name and location: "

class Game:
    """
    a class which creates the rush our game object, which contains
     the game process and components
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.board = board

    def __check_input(self, user_input):
        """
        this function checks if the given input is of the correct format
        :param user_input: a string with car name, a comma and move direction
        :return: True if condition above are met, False otherwise
        """
        if len(user_input) != 3 or user_input[1] != SEP:
            if user_input != "!":
                print(BAD_INPUT_MSG)
            return False
        if user_input[0] not in CAR_NAMES:
            print(BAD_NAME_MSG)
            return False
        if user_input[2] not in DIRECTIONS:
            print(BAD_MOVE_MSG)
            return False
        return True

    def __get_user_input(self):
        """
        gets input from the user checks it,
        and returns the chosen car and direction. if the player chooses to
        end the game - returns '!'
        """
        user_input = input(INPUT_MSG)
        while not self.__check_input(user_input):
            if user_input == EXIT_GAME:
                return user_input
            user_input = input(INPUT_MSG)
        car_name, move_dir = user_input.split(",")
        return car_name, move_dir

    def __single_turn(self):
        """
        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.
        """
        first_try = self.__get_user_input()
        if first_try == EXIT_GAME:
            return False
        else:
            car_name, movekey = first_try

        move = self.board.move_car(car_name, movekey)
        while not move:
            retry = self.__get_user_input()
            if retry == EXIT_GAME:
                return False
            else:
                car_name, movekey = retry
            move = self.board.move_car(car_name, movekey)
        print("Successful move")
        print(self.board)
        return True

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        print(STAR_MSG)
        print(self.board)
        turn = self.__single_turn()
        while turn:
            if self.board.cell_content(self.board.target_location()):
                print(WIN_MSG)
                return
            turn = self.__single_turn()
        print(GAME_OVER_MSG)
        return

def load_json(filename):
    """ loads a .json file"""
    json_file = filename
    with open(json_file, 'r') as file:
        car_config = json.load(file)
    return car_config

def check_car_inputs(length, location, orient):
    """checks if parameters for car object are correct"""
    if not (2 <= length <= 4):
        return False
    if orient not in ORIENTATIONS:
        return False
    for i in location:
        if i < 0:
            return False
    return True

def create_cars(car_dict):
    """creates car objects from car dictionary given by json file"""
    car_lst = []
    for name in car_dict:
        length = car_dict[name][0]
        location = tuple(car_dict[name][1])
        orient = car_dict[name][2]
        if check_car_inputs(length, location, orient):
            car_lst.append(Car(name, length, location, orient))
    return car_lst

def initiate_board(car_lst):
    """creates a board object and adds cars to it"""
    board = Board()
    if car_lst != []:
        for car in car_lst:
            board.add_car(car)
    return board

def main():
    filename = input(INSERT_FILE_MSG)
    car_dict = load_json(filename)
    car_lst = create_cars(car_dict)
    board = initiate_board(car_lst)
    game = Game(board)
    game.play()


if __name__== "__main__":
    from car import Car
    from board import Board
    main()
