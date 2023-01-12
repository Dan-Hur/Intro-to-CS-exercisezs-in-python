##############################################################################
# FILE: ex7.py
# WRITER: Daniel
# EXERCISE: intro2cs2 ex7
# a collection of recursive functions
##############################################################################

def print_to_n(n):
    """prints all the numbers from 1 up to n"""
    if n >= 1:
        print_to_n(n-1)
        print(n)


def digit_sum(n):
    """sums the digits of the number n"""
    if n == 0:
        return n
    digit = n % 10
    return digit + digit_sum(n//10)


def is_prime(n):
    """checks if n is prime"""
    return has_divisor_smaller_than(n,int(n**0.5))


def has_divisor_smaller_than(n,i):
    """checks if n is devisable by i"""
    if i == 1:
        return True
    if n % i == 0:
        return False
    return has_divisor_smaller_than(n,i-1)


def play_hanoi(hanoi, n, src, dst, temp):
    """plays tower of hanoi game"""
    if n>0:
        play_hanoi(hanoi, n-1, src, temp, dst)
        _base_hanoi_case(hanoi, src, dst)
        play_hanoi(hanoi, n - 1, temp, dst, src)


def _base_hanoi_case(hanoi, src, dst):
    """the base case for the tower of hanoi recursion"""
    hanoi.move(src, dst)


def print_sequences(char_lst, n):
    """prints a list of strings separately"""
    for i in create_lst_of_options(char_lst, n):
        print(i)


def create_lst_of_options(char_lst, n):
    """creates a list with all string combinations (with length of n)
     of letters given in a list"""
    if n == 1:
        return char_lst
    elif n == 0:
        return ""
    else:
        return [i + j
                for i in create_lst_of_options(char_lst, 1)
                for j in create_lst_of_options(char_lst, n-1)]


def print_no_repetition_sequences(char_lst, n):
    """prints a string of n characters built from a combinations
    of characters from the char_lst, without character repetition"""
    _no_repetition_seq_help(char_lst, n, "")


def _no_repetition_seq_help(char_lst, n, out_str):
    """"a helper function for the function above that constructs
    and prints the strings"""
    if len(out_str) == n:
        print(out_str)
    else:
        for i in range(len(char_lst)):
            char = char_lst.pop(i)
            _no_repetition_seq_help(char_lst, n, out_str + char)
            char_lst.insert(i,char)


OPEN_PARENTHESES = "("
CLOSE_PARENTHESES = ")"


def parentheses(n):
    """returns a list of strings representing all options
    of n parentheses opening an closing"""
    return_lst = []
    _parentheses_helper(n, 0, 0, "", return_lst)
    return return_lst


def _parentheses_helper(n, open, close,return_str,return_lst):
    """a recursive function that creates the list for the main
    parentheses function"""
    if close == n and open == n:
        return_lst.append(return_str)
        return
    if open < n:
        _parentheses_helper(n, open + 1, close,
                            return_str + OPEN_PARENTHESES, return_lst)
    if close < open:
        _parentheses_helper(n, open, close + 1,
                            return_str + CLOSE_PARENTHESES, return_lst)
    if n == 0:
        return ""


MOVE_DICT = {"u":(-1,0), "d":(1,0), "l":(0,-1), "r":(0,1)}


def is_legal_move(move, image):
    """checks if a move can be made in the image"""
    return (move[0] >= 1 and move[0] <= len(image) - 1
            and 1 <= move[1] <= len(image) - 1
            and image[move[0]][move[1]] != "*")


def flood(image,position):
    """fills a cell with * string"""
    image[position[0]][position[1]] = "*"


def flow_to(position, change):
    """changes the cell position"""
    return (position[0] + change[0], position[1] + change[1])


def print_image(image):
    """prints the whole give image (which is a matrix)"""
    for line in image:
        for cell in line:
            print(cell.center(2), end = " ")
        print()


def flood_fill(image, start):
    """the main function that prints a filled image"""
    print_image(_flood_fill_helper(image, start))


def _flood_fill_helper(image, start):
    """a helper function for the flood fill that fills an image
    meaning - inserts '*' string instead of nearby '.' string
    and returns it"""
    if not is_legal_move(start, image):
        return
    else:
        flood(image,start)

    for direction in MOVE_DICT:
        new_start = flow_to(start, MOVE_DICT[direction])
        _flood_fill_helper(image, new_start)

    return image
