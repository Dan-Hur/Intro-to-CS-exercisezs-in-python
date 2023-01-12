###############################################################################
# FILE: temperature.py
# WRITER:Daniel
# EXCERCISE: intro2cs2 ex2
# a function that compares 3 temperatures with a threshold
###############################################################################

def is_it_summer_yet(threshold_temp,day1,day2,day3):
    """this function compares three temperatures to threshold temp"""
    days = [day1, day2, day3]
    hotter_than_threshold = []
    for i in days:
        if i > threshold_temp:
            hotter_than_threshold.append(i)
    if len(hotter_than_threshold) >= 2:
        return True
    else:
        return False
