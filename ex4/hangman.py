##############################################################################
# FILE: hangman.py
# WRITER:Daniel
# EXERCISE: intro2cs2 ex4
# a program that runs the hangman game
##############################################################################
import hangman_helper as hh

BLANK = "_"
LETTER = hh.LETTER
WORD = hh.WORD
HINT = hh.HINT
HINT_LENGTH = hh.HINT_LENGTH
BAD_INPUT_MSG = "Bad Input >:("
REPEATED_CHOICE_MSG = "You guessed that letter already!"
WIN_MSG = "You Win!!"
LOSE_MSG = "You Lose :("
GAMES_PLAYED_MSG = "The number of games you played so far is: {} "
GAMES_SURVIVED_MSG = "The number of games you survived is: {} "
YOUR_SCORE_MSG = "Your score is: {} "
CONT_MSG = "Do you want to continue"
POINT = 1

def input_validation(inpt):
    """checks if the input for the game is valid (is a lowercase letter)"""
    check1 = len(inpt) == 1
    check2 = inpt.isalpha()
    check3 = inpt == inpt.lower()

    if check1 and check2 and check3:
        return True
    else:
        return False

def point_calculation(pattern, user_input, input_type):
    """calculates points for our game. used in run_single_game function"""
    n = 0
    point_addition = 0
    if input_type == LETTER:
        for i in pattern:
            if user_input == i:
                n += 1
        point_addition = n * (n+1) // 2
        return point_addition

    if input_type == WORD:
        for i in range(len(user_input)):
            if user_input[i] != pattern[i]:
                n += 1
        point_addition = n * (n+1) // 2
        return point_addition

def final_message(points, word):
    """prints a final win/lose message accordingly"""
    if points == 0:
        msg = LOSE_MSG + " the word is " + word
    else:
        msg = WIN_MSG
    return msg

def update_word_pattern(word, pattern, letter):
    """this function creates a new pattern based on
    guessed letter"""
    new_pattern = ""
    for i in range(len(word)):
        if pattern[i].isalpha():
            new_pattern += pattern[i]
        elif letter == word[i]:
            new_pattern += letter
        else:
            new_pattern += BLANK
    return new_pattern

def letter_guess_chain(user_input,pattern,rand_word,points,wrong_guess_list):
    """this function will run a letter guessing round
    as part of the single game function"""
    new_msg = "next round"
    adjusted_points = points
    new_pattern = pattern
    if not (input_validation(user_input)):
        new_msg = BAD_INPUT_MSG
    elif user_input in wrong_guess_list or user_input in new_pattern:
        new_msg = REPEATED_CHOICE_MSG
    else:
        adjusted_points -= POINT
        if user_input in rand_word:
            new_pattern = update_word_pattern(rand_word,
                                              new_pattern, user_input)
            adjusted_points += point_calculation(new_pattern,
                                                 user_input, LETTER)
        else:
            wrong_guess_list.append(user_input)
    return adjusted_points, new_msg, new_pattern


def length_validation(words_lst, pattern):
    """a function that checks if words from a list
    have the same length as a given pattern"""
    filtered_lst = []
    for word in words_lst:
        if len(word) == len(pattern):
            filtered_lst.append(word)
    return filtered_lst

def character_validation(words_lst, pattern):
    """a function that checks if words from a list
    have the same characters as a given pattern.
    the pattern has to be the same length as the words"""
    filtered_lst = []
    index_list = []
    letter_list = []
    for word in words_lst:
        char_validation = 0
        for i in range(len(pattern)):
            if pattern[i].isalpha():
                if word[i] != pattern[i]:
                    char_validation += 1
            else:
                continue
        if char_validation == 0:
            filtered_lst.append(word)
    return filtered_lst

def double_char_validation(word_lst, pattern):
    """filters words that have repeated letters in an incorrect place"""
    filtered_lst = []
    for word in word_lst:
        char_validation = 0
        for i in range(len(word)):
            if word[i] in pattern and word[i] != pattern[i]:
                char_validation += 1
        if char_validation == 0:
            filtered_lst.append(word)
    return filtered_lst

def bad_guess_filter(word_lst, wrong_guess_lst):
    """this function filters words from a list
    that have an incorrect letter (given by wrong_guess_lst)"""
    filtered_lst = []
    # I didn't want to change the given list, thus i added a counter
    # to check if there are characters from
    # the wrong guess list inside the word
    if not wrong_guess_lst:
        return word_lst
    for word in word_lst:
        flse_counter = 0
        for letter in wrong_guess_lst:
            if letter in word:
                flse_counter += 1
        if flse_counter == 0:
            filtered_lst.append(word)
    return filtered_lst

def filter_words_list(words, pattern, wrong_guess_lst):
    """filters words from the list for a hint in the game"""
    filtered_lst = length_validation(words, pattern)
    filtered_lst = character_validation(filtered_lst, pattern)
    filtered_lst = double_char_validation(filtered_lst, pattern)
    filtered_lst = bad_guess_filter(filtered_lst, wrong_guess_lst)
    return filtered_lst

def take_n_words(word_lst,hint_length):
    """takes 'n' words out of a list in a specific order,
    'n' being the hint_length"""
    n = len(word_lst)
    hint_lst = []
    for i in range(hint_length):
        hint_lst.append(word_lst[i * n//hint_length])
    return hint_lst

def hint_guess_chain(words_list,pattern, wrong_guess_list):
    """this function will determine the hint given to the player
    under the function - run single game"""
    filtered_lst = filter_words_list(words_list, pattern, wrong_guess_list)
    if len(filtered_lst) > HINT_LENGTH:
        hint_lst = take_n_words(filtered_lst, HINT_LENGTH)
    else:
        hint_lst = filtered_lst
    msg = "continue"
    return hint_lst, msg

def run_single_game(words_list, score):
    """runs a single game, returns the final score"""
    # initiation / preparation
    rand_word = hh.get_random_word(words_list)
    wrong_guess_list = []
    points = score
    pattern = BLANK * len(rand_word)
    msg = "Start Game!"
    # game course
    while BLANK in pattern and points > 0:
        hh.display_state(pattern,wrong_guess_list,points,msg)
        input_type, user_input = hh.get_input()
        if input_type == LETTER:
            points, msg, pattern = letter_guess_chain(user_input, pattern,
                                                      rand_word, points,
                                                      wrong_guess_list)
            continue
        if input_type == WORD:
            points -= POINT
            if user_input == rand_word:
                points += point_calculation(pattern, user_input, input_type)
                break
        if input_type == HINT:
            points -= POINT
            hint_lst, msg = hint_guess_chain(words_list,
                                             pattern, wrong_guess_list)
            hh.show_suggestions(hint_lst)
            continue
    # end of game
    msg = final_message(points, rand_word)
    hh.display_state(pattern, wrong_guess_list, points, msg)
    return points

def main():
    """runs the game sa many times as wanted by the player"""
    words_list = hh.load_words()
    play_again_choice = True
    score = hh.POINTS_INITIAL
    games_played = 0
    while play_again_choice:
        score = run_single_game(words_list, score)
        games_played += 1
        if score == 0:
            play_again_choice = \
                hh.play_again(GAMES_SURVIVED_MSG.format(games_played)
                              +CONT_MSG)
            if play_again_choice:
                score = hh.POINTS_INITIAL
                games_played = 0
                continue
            else:
                break
        play_again_choice = \
            hh.play_again(GAMES_PLAYED_MSG.format(games_played)
                          + YOUR_SCORE_MSG.format(score) + CONT_MSG)



if __name__ == "__main__":
    main()

