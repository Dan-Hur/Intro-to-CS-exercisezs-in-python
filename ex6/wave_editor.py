##############################################################################
# FILE: wave_editor.py
# WRITER: Daniel
# EXERCISE: intro2cs2 ex6
# a program that allows editing wav audio files, and compose melodies
##############################################################################

import scipy
import numpy
import math
import wave_helper as wh
import os
from copy import deepcopy

MAIN_ALTER = "1"
MAIN_COMPOSE = "2"
MAIN_EXIT = "3"
MAIN_MENU_CHOICE_LST = [MAIN_ALTER, MAIN_COMPOSE, MAIN_EXIT]
MAIN_MENU_MSG = """welcome to my audio editing program!
please select one of the following options: 
1 - alter a wav file
2 - compose a tune for wav format
3 - exit program
please enter your selection number: """
BAD_SELECTION_MSG = "this is not a valid selection, please select again: "
ALTER_REVERSE = "1"
ALTER_NEGATE = "2"
ALTER_SPEED_UP = "3"
ALTER_SLOW_DOWN = "4"
ALTER_VOLUME_UP = "5"
ALTER_VOLUME_DOWN = "6"
ALTER_LOW_PASS = "7"
ALTER_EXIT = "8"
ALTERING_MENU_MSG = """altering a wav file.
choose your alteration: 
1 - reverse audio
2 - negate audio
3 - speed-up audio
4 - slow-down audio
5 - increase audio volume
6 - decrease audio volume
7 - apply low pass filter on audio
8 - exit
please enter your selection number: """
ALTER_MENU_CHOICE_LST = [ALTER_REVERSE, ALTER_NEGATE, ALTER_SPEED_UP,
                         ALTER_SLOW_DOWN, ALTER_VOLUME_UP, ALTER_VOLUME_DOWN,
                         ALTER_LOW_PASS, ALTER_EXIT]
EXIT_ALTER_MSG = "please enter a file name, " \
                 "in which you would like to save the edited audio: "
BAD_FILE_NAME = "this is an incorrect file name or location, enter again: "
CHOOSE_WAV_MSG = "please specify the name and the path of the" \
                 " .wav file you would like to alter: "
SAVE_FILE_NAME_MSG = "please choose a name for your file: "
DONE_MSG = "Done"
MAX_VOLUME = 32767
MIN_VOLUME = -32768

##############################################################################
# the lists below show the different menus for the user
##############################################################################

def show_main_menu():
    """prints the the main menu to the user, returns the choice str"""
    user_choice = input(MAIN_MENU_MSG)
    while user_choice not in MAIN_MENU_CHOICE_LST:
        user_choice = input(BAD_SELECTION_MSG)
    return user_choice

def wav_alteration_menu():
    """prints the alteration menu to the user, returns the choice str"""
    user_choice = input(ALTERING_MENU_MSG)
    while user_choice not in ALTER_MENU_CHOICE_LST:
        user_choice = input(BAD_SELECTION_MSG)
    return user_choice

def read_wav_file():
    """reads a wav file, returns two parameters
    sample_rate = int and audio_data = is a list of lists with
    each inner list having two items, one for each channel"""
    wav_filename = input(CHOOSE_WAV_MSG)
    while wh.load_wave(wav_filename) == -1:
        wav_filename = input(BAD_FILE_NAME)
    sample_rate, audio_data = wh.load_wave(wav_filename)
    return sample_rate, audio_data

def show_exit_alter_menu(sample_rate, audio_lst):
    """presents exit menu to the user"""
    user_out_name = input(EXIT_ALTER_MSG)
    wh.save_wave(sample_rate, audio_lst, user_out_name)

def exit_program():
    return None

##############################################################################
# the lists below are used for audio manipulation
##############################################################################

def reverse_audio(lst):
    """reverses a list of lists while keeping the inner
    list items in the same order
    input: list of lists with two items inside them"""
    altering_lst = deepcopy(lst)
    for i in range(len(altering_lst)//2):
        altering_lst[i], altering_lst[-i-1] = \
            altering_lst[-i-1], altering_lst[i]
    print(DONE_MSG)
    return altering_lst

def negating_audio(lst):
    """this function will take a list of lists and
     multiply every inner item by -1
     input: list of lists with two items inside them"""
    altering_lst = deepcopy(lst)
    for i in range(len(altering_lst)):
        altering_lst[i][0] *= (-1)
        altering_lst[i][1] *= (-1)
    print(DONE_MSG)
    return altering_lst

def speed_up_audio(lst):
    """this function returns a list made of only the even indexes.
    this allows for speeding up audio
    input: list of lists with two items inside them"""
    altered_lst = []
    for item in range(0, len(lst), 2):
        altered_lst.append(lst[item])
    print(DONE_MSG)
    return altered_lst

def average_two_lists(lst1,lst2):
    """takes two lists with two items each and averages their
    items respectively"""
    average_lst = list()
    average_lst.append(int((lst1[0]+lst2[0]) / 2))
    average_lst.append(int((lst1[1]+lst2[1]) / 2))
    return average_lst

def slow_down_audio(lst):
    """this function will take two items in a list and
    insert their average between them.
    this allows for slowing down audio
    input: list of lists with two items inside them"""
    altered_lst = list()
    if len(lst) == 1:
        altered_lst.append([lst[0]*2])
    for i in range(len(lst)):
        altered_lst.append(lst[i])
        if i != len(lst)-1:
            average = average_two_lists(lst[i], lst[i+1])
            altered_lst.append(average)
    print(DONE_MSG)
    return altered_lst

def max_and_min_flattening(lst):
    """this function will go over a list of lists and lower to
    max values that are higher and raise values lower than the min.
    input: has to be a list of lists with two items inside them"""
    for i in lst:
        if i[0] > MAX_VOLUME:
            i[0] = MAX_VOLUME
        if i[0] < MIN_VOLUME:
            i[0] = MIN_VOLUME
        if i[1] > MAX_VOLUME:
            i[1] = MAX_VOLUME
        if i[1] < MIN_VOLUME:
            i[1] = MIN_VOLUME

def volume_up(lst):
    """multiplies every item by 1.2, if the result is higher than max,
    or lower than min, it gets reduced to the max/min value
    input: list of lists with two items inside them"""
    altered_lst = [[int(ch1*1.2), int(ch2*1.2)] for ch1, ch2 in lst]
    max_and_min_flattening(altered_lst)
    print(DONE_MSG)
    return altered_lst

def volume_down(lst):
    """divides every item by 1.2.
    input: list of lists with two items inside them"""
    altered__lst = [[int(ch1/1.2), int(ch2/1.2)] for ch1, ch2 in lst]
    print(DONE_MSG)
    return altered__lst

def average_three_lists(lst1,lst2,lst3):
    """takes three lists with two items each and averages their
    items respectively inside them"""
    average_lst = list()
    average_lst.append(int((lst1[0]+lst2[0]+lst3[0]) / 3))
    average_lst.append(int((lst1[1]+lst2[1]+lst3[1]) / 3))
    return average_lst

def low_pass_filter(lst):
    """averages each inner list with its neighbours,
    returns the list of averages
    input: list of lists with two items inside them"""
    if len(lst) == 1:
        return lst
    altered_lst = []
    for i in range(len(lst)):
        if i == 0:
            altered_lst.append(average_two_lists(lst[i], lst[i+1]))
        elif i == len(lst)-1:
            altered_lst.append(average_two_lists(lst[i], lst[i - 1]))
        else:
            altered_lst.append(average_three_lists(lst[i-1],lst[i],lst[i+1]))
    print(DONE_MSG)
    return altered_lst

##############################################################################
# the next part is for audio composition
##############################################################################

CHORD_DICT = {"A": 440, "B": 494, "C": 523, "D": 587,
              "E": 659, "F": 698, "G": 784, "Q": 0}
SAMPLE_RATE = 2000
ONE_SIXTEENTH_SAMPLE = int(SAMPLE_RATE/16)
PI = math.pi
INPUT_COMPOSITION_MSG = "please enter the name of the composition file: "

def samples_per_cycle(chord_freq):
    """calculates the number of samples per cycle"""
    if chord_freq == 0:
        return 0
    return SAMPLE_RATE/chord_freq

def calculate_audio_sample(chord_frq, sample_num):
    """calculates the audio sample"""
    if chord_frq == 0:
        calculation = 0
    else:
        calculation = MAX_VOLUME * math.sin(PI * 2 * (
                sample_num/samples_per_cycle(chord_frq)))
    calculation = int(calculation)
    return calculation

def check_chord_file_name(filename):
    """check if a given file name is correct"""
    if os.path.exists(filename):
        return True
    return False

def get_chord_file():
    """asks for a file name until a correct one is given, returns the name"""
    user_chord_comp = input(INPUT_COMPOSITION_MSG)
    while not check_chord_file_name(user_chord_comp):
        user_chord_comp = input(BAD_FILE_NAME)
    return user_chord_comp

def read_chord_file(file_name):
    """reads a file consisting from chord letters and play duration
    returns them in a list"""
    with open(file_name, "r") as chords:
        chord_lst = chords.read().split()
    return chord_lst

def translate_chord_to_freq(chord):
    """translates from chord str to freq int"""
    return CHORD_DICT[chord]

def note_composition(note,duration):
    """composes an audio list for one note"""
    play_lst = []
    freq = translate_chord_to_freq(note)
    sample_num = duration * ONE_SIXTEENTH_SAMPLE
    for sample in range(sample_num):
        value = calculate_audio_sample(freq, sample)
        play_lst.append([value,value])
    return play_lst

def melody_composition(note_and_time_lst):
    """composes a melody of many notes"""
    melody_lst = []
    for i in range(0,len(note_and_time_lst),2):
        note_lst = note_composition(note_and_time_lst[i],
                                    int(note_and_time_lst[i+1]))
        melody_lst.extend(note_lst)
    return melody_lst

def composition_process():
    """this is the whole composition process
     shown when the user chooses to compose"""
    note_file_name = get_chord_file()
    note_and_time_lst = read_chord_file(note_file_name)
    audio_lst = melody_composition(note_and_time_lst)
    print(DONE_MSG)
    return SAMPLE_RATE, audio_lst

###############################################################################
# routing and assembly
###############################################################################

def alteration_routing(user_input,audio_lst):
    """this func will rout the choice of the user
     to the respective function when altering audio"""
    new_audio_lst = audio_lst
    if user_input == ALTER_REVERSE:
        new_audio_lst = reverse_audio(new_audio_lst)
    if user_input == ALTER_NEGATE:
        new_audio_lst = negating_audio(new_audio_lst)
    if user_input == ALTER_SPEED_UP:
        new_audio_lst = speed_up_audio(new_audio_lst)
    if user_input == ALTER_SLOW_DOWN:
        new_audio_lst = slow_down_audio(new_audio_lst)
    if user_input == ALTER_VOLUME_UP:
        new_audio_lst = volume_up(new_audio_lst)
    if user_input == ALTER_VOLUME_DOWN:
        new_audio_lst = volume_down(new_audio_lst)
    if user_input == ALTER_LOW_PASS:
        new_audio_lst = low_pass_filter(new_audio_lst)
    return new_audio_lst

def alteration_menu_process(sample_rate,audio_lst):
    """this conducts the whole process of music alteration
    when the user chooses"""
    user_input = wav_alteration_menu()
    new_audio_lst = audio_lst
    while user_input != ALTER_EXIT:
        new_audio_lst = alteration_routing(user_input, new_audio_lst)
        user_input = wav_alteration_menu()
    show_exit_alter_menu(sample_rate, new_audio_lst)


def main_menu_routing():
    """this func will rout the users choice to the respective process
    chosen from main menu"""
    user_choice = show_main_menu()
    if user_choice == MAIN_ALTER:
        sample_rate, audio_lst = read_wav_file()
        alteration_menu_process(sample_rate, audio_lst)
        return True
    if user_choice == MAIN_COMPOSE:
        sample_rate, audio_lst = composition_process()
        alteration_menu_process(sample_rate, audio_lst)
        return True
    if user_choice == MAIN_EXIT:
        return exit_program()

def main():
    """the main func that runs the program"""
    cont = True
    while cont:
        check = main_menu_routing()
        if check is None:
            cont = False


if __name__ == "__main__":
    main()


