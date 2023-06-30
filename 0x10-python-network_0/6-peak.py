#!/usr/bin/python3
""" The script will return from list of int passed
"""


def find_peak(list_of_integers):
    """ find_peak function return peak
    """
    if (len(list_of_integers) == 0):
        return None

    else:
        mypeak = list_of_integers[0]
        for i in range(len(list_of_integers)):
            if list_of_integers[i] > list_of_integers:
                 mypeak = list_of_integers[i]
        return  mypeak
