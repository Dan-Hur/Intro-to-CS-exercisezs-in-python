##############################################################################
# FILE: wordsearch.py
# WRITER: Daniel
# EXERCISE: intro2cs2 ex5 
# a program that finds words (given in a txt file) in a
# matrix (also in txt file). creates a new file with the results
##############################################################################
from copy import deepcopy
import sys
import os

NUM_OF_ARGS = 4
FILE_NAME = 1
MATRIX_NAME = 2
OUTPUT_FILE_NAME = 3
DIRECTION_INPUT = 4
NOT_ENOUGH_INPUTS_MSG = "args list should have 4 parameters"
NEXT_LINE = "\n"
SEP = ","
DOWN_TO_UP = "u"
UP_TO_DOWN = "d"
LEFT_TO_RIGHT = "r"
RIGHT_TO_LEFT = "l"
UP_RIGHT_DIAGONAL = "w"
UP_LEFT_DIAGONAL = "x"
DOWN_RIGHT_DIAGONAL = "y"
DOWN_LEFT_DIAGONAL = "z"
FILE_DOESNT_EXSIST_MSG = "one of the files does not exist"
INVALID_DIREVTIONS = "you entered an invalid direction"
DIRECTION_LIST = [DOWN_TO_UP, UP_TO_DOWN, LEFT_TO_RIGHT, RIGHT_TO_LEFT,
                  UP_RIGHT_DIAGONAL, UP_LEFT_DIAGONAL, DOWN_RIGHT_DIAGONAL,
                  DOWN_LEFT_DIAGONAL]


def check_input_args(args):
    """this function will check if the args given are valid"""
    if len(args[1:]) != NUM_OF_ARGS:
        return NOT_ENOUGH_INPUTS_MSG
    if not(os.path.exists(args[FILE_NAME]) and os.path.exists(args[MATRIX_NAME])):
        return FILE_DOESNT_EXSIST_MSG
    for letter in args[DIRECTION_INPUT]:
        if letter not in DIRECTION_LIST:
            return INVALID_DIREVTIONS
    return None

def filter_backslash_n(string):
    """removes \n from the end of a string"""
    if "\n" in string:
        new_entry = string[:len(string) - 1]
        return new_entry
    else:
        return string

def filter_word_list(word_list):
    """filters \n's from the end of each string in a list"""
    filtered_list = []
    for word in word_list:
        new_entry = filter_backslash_n(word)
        filtered_list.append(new_entry)
    return filtered_list

def read_wordlist_file(filename):
    """creates a list of words from a file"""
    output_list = []
    with open(filename,'r') as f:
        for i in f:
            output_list.append(i)
    filtered_output_list = filter_word_list(output_list)
    return filtered_output_list

def read_matrix_file(filename):
    """reads a matrix from a file, returns a list of lists"""
    output_mtrx = []
    with open(filename,'r') as f:
        for item in f:
            filtered_item = filter_backslash_n(item)
            new_item = filtered_item.split(",")
            output_mtrx.append(new_item)
    return output_mtrx

def single_word_search(word, letter_list):
    """finds a word in a list of single letters returns it with its' counts"""
    created_str = "" # this string will receive letters until a word is formed
    count = 0
    indx = 0
    for letter in letter_list:
        created_str += letter
        if str(word) in created_str:
            count += 1
            created_str = created_str[indx - (len(word) - 1):]

    return count

def find_word_in_nested_lists(word, matrix):
    """searches for a single word in all rows of a matrix"""
    total_count = 0
    for row in matrix:
        count = single_word_search(word, row)
        total_count += count

    return total_count

def find_words_in_nested_lists(lst_of_words, matrix):
    """searches for many words in all rows of a matrix"""
    found_word_dict = {}
    for word in lst_of_words:
        total_count = find_word_in_nested_lists(word, matrix)
        if total_count != 0:
            found_word_dict[word] = total_count
    return found_word_dict

def reverse_inner_list_order(inner_lst):
    """reverses item order in a list"""
    reversed_lst = []
    for item in reversed(inner_lst):
        reversed_lst.append(item)
    return reversed_lst

def reverse_matrix_cols(list_of_lists):
    """reverses the items in the inner lists of a list"""
    # a very important function that allows reversing columns of a matrix
    # this can be used to seemingly change search directions!
    reversed_matrix = []
    for lst in list_of_lists:
        new_row = reverse_inner_list_order(lst)
        reversed_matrix.append(new_row)
    return reversed_matrix

def separate_items_to_lists(lst):
    """creates a separate list for each item in a given list,
    and puts them in a list"""
    new_lst = [[i] for i in lst]
    return new_lst

def insert_lst_into_inner_lists(og_lst, insertion_lst,indx):
    """this function inserts a given list into a list of lists in the
    designated index, starting from the second item of the list"""
    new_list = deepcopy(og_lst)
    for i in range(len(insertion_lst)):
        if i != (len(insertion_lst) - 1):
            new_list[i+indx].append(insertion_lst[i])
        else:
            new_list.append([insertion_lst[i]])
    return new_list

def inserting_lst_to_lst_several_times(matrix):
    """this function runs the 'insert_lst_into_inner_lists' function
    for a given matrix"""
    # inserting each row of a matrix into the previous rows as seen below,
    # creates a list of the down left diagonals of a matrix
    output_lst = separate_items_to_lists(matrix[0])
    indx = 1
    for i in range(1, len(matrix)):
        output_lst = insert_lst_into_inner_lists(output_lst, matrix[i], indx)
        indx += 1
    return output_lst

def create_list_of_down_left_diagonals(matrix):
    """creates a list of the down-left diagonals of a matrix"""
    output_lst = inserting_lst_to_lst_several_times(matrix)
    return output_lst

def create_list_of_down_right_diagonals(matrix):
    """creates a list of the down-right diagonals of a matrix"""
    new_matrix = reverse_matrix_cols(matrix)  # allows reversing readout order
    output_lst = inserting_lst_to_lst_several_times(new_matrix)
    return output_lst

def create_list_of_up_right_diagonals(matrix):
    """creates a list of the up-right diagonals of a matrix"""
    down_left_matrix = create_list_of_down_left_diagonals(matrix)
    output_list = reverse_matrix_cols(down_left_matrix)
    return output_list

def create_list_of_up_left_diagonals(matrix):
    """creates a list of the up-left diagonals of a matrix"""
    down_right_matrix = create_list_of_down_right_diagonals(matrix)
    output_list = reverse_matrix_cols(down_right_matrix)
    return output_list

def create_up_to_down_list(matrix):
    """creates a list of columns of a matrix from up to down"""
    up_to_down_matrix = []
    for col in range(len(matrix[0])):
        col_args = []
        for row in matrix:
            col_args.append(row[col])
        up_to_down_matrix.append(col_args)
    return up_to_down_matrix

def create_down_to_up_list(matrix):
    """creates a list of columns of a matrix from down to up"""
    up_to_down_matrix = (create_up_to_down_list(matrix))
    down_to_up_matrix = reverse_matrix_cols(up_to_down_matrix)
    return down_to_up_matrix

def right_word_search(word_list, matrix):
    """searches for words in a matrix from left to right"""
    output = find_words_in_nested_lists(word_list, matrix)
    return output

def left_word_search(word_list, matrix):
    """searches for words in a matrix from right to left"""
    lef_to_right_matrix = reverse_matrix_cols(matrix)
    output = find_words_in_nested_lists(word_list, lef_to_right_matrix)
    return output

def down_left_diagonal_search(word_list, matrix):
    """searches for words in a matrix from up-right to down-left diagonals"""
    dl_diagonal_matrix = create_list_of_down_left_diagonals(matrix)
    output = find_words_in_nested_lists(word_list, dl_diagonal_matrix)
    return output

def down_right_diagonal_search(word_list, matrix):
    """searches for words in a matrix from up-left to down-right diagonals"""
    dr_diagonal_matrix = create_list_of_down_right_diagonals(matrix)
    output = find_words_in_nested_lists(word_list, dr_diagonal_matrix)
    return output

def up_right_diagonal_search(word_list, matrix):
    """searches for words in a matrix from down-left to up-right diagonals"""
    ur_diagonal_matrix = create_list_of_up_right_diagonals(matrix)
    output = find_words_in_nested_lists(word_list, ur_diagonal_matrix)
    return output

def up_left_diagonal_search(word_list, matrix):
    """searches for words in a matrix from down-right to up-left diagonals"""
    ul_diagonal_matrix = create_list_of_up_left_diagonals(matrix)
    output = find_words_in_nested_lists(word_list, ul_diagonal_matrix)
    return output

def up_to_down_word_search(word_list, matrix):
    """searches for words in a matrix from up to down"""
    utd_matrix = create_up_to_down_list(matrix)
    output = find_words_in_nested_lists(word_list, utd_matrix)
    return output

def down_to_up_word_search(word_list, matrix):
    """searches for words in a matrix from down to up"""
    dtu_matrix = create_down_to_up_list(matrix)
    output = find_words_in_nested_lists(word_list, dtu_matrix)
    return output

def separate_sting(input_string):
    """returns a list of individual components of a string (no duplicates)"""
    comp_list = []
    for letter in input_string:
        if letter not in comp_list:
            comp_list.append(letter)
    return comp_list

def search_according_to_input_srt(word_list, matrix, input_string):
    """decides which search function should be summoned
    based on an input string"""
    output = None
    if input_string == DOWN_TO_UP:
        output = down_to_up_word_search(word_list, matrix)
    if input_string == UP_TO_DOWN:
        output = up_to_down_word_search(word_list, matrix)
    if input_string == LEFT_TO_RIGHT:
        output = right_word_search(word_list, matrix)
    if input_string == RIGHT_TO_LEFT:
        output = left_word_search(word_list, matrix)
    if input_string == UP_RIGHT_DIAGONAL:
        output = up_right_diagonal_search(word_list, matrix)
    if input_string == UP_LEFT_DIAGONAL:
        output = up_left_diagonal_search(word_list, matrix)
    if input_string == DOWN_RIGHT_DIAGONAL:
        output = down_right_diagonal_search(word_list, matrix)
    if input_string == DOWN_LEFT_DIAGONAL:
        output = down_left_diagonal_search(word_list, matrix)
    return output

def update_count_in_dict(input_dict, updating_dict):
    """updates the count values of existing keys,
     if a key does not exist in the input_dict, it is inserted a given val"""
    updated_dict = updating_dict.copy()
    for key in updated_dict:
        if key in input_dict:
            input_dict[key] += updated_dict[key]
        else:
            input_dict[key] = updated_dict[key]
    return updated_dict

def find_words_in_matrix(word_list, matrix, directions):
    """finds words in a matrix via specified search patterns"""
    output_dict = dict()
    if not matrix:
        return []
    list_of_directions = separate_sting(directions) # filters letter doubles
    for letter in list_of_directions:
        temp_dict = search_according_to_input_srt(word_list, matrix, letter)
        update_count_in_dict(output_dict, temp_dict)
    output_lst = list(output_dict.items())
    return output_lst

def extract_items_from_tuple_to_str_for_file(tup):
    """creates a string from a tuple"""
    out_str = ""
    for i in tup:
        out_str += str(i) + SEP
    out_str = out_str[:-1]
    out_str += NEXT_LINE
    return out_str

def write_output_file(results, output_filename):
    """creates an output file from a list"""
    if results:
        with open(output_filename,"w") as f:
            for tup in results:
                line = extract_items_from_tuple_to_str_for_file(tup)
                if tup is results[-1]:
                    line = line[:-1]
                f.writelines(line)

def main():
    """main function that searches for words (given by file) in a
    matrix (also given by file) and returns a file with the results"""
    args = sys.argv
    check_result = check_input_args(args)
    assert not(check_result), check_result
    file_name = args[FILE_NAME]
    matrix_name = args[MATRIX_NAME]
    output_filename = args[OUTPUT_FILE_NAME]
    directions = args[DIRECTION_INPUT]
    word_list = read_wordlist_file(file_name)
    matrix = read_matrix_file(matrix_name)
    results = find_words_in_matrix(word_list, matrix, directions)
    write_output_file(results, output_filename)


if __name__ == "__main__":
    main()
