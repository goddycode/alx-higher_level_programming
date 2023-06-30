#!/usr/bin/python3
""" The script in this module returns the peak of the list
"""


def find_peak(tobe_testedl_list_of_integers):
    """ This function returns the peak of the list
    """
    if (len(tobe_testedl_list_of_integers) == 0):
        return None

    else:
        baseline = tobe_testedl_list_of_integers[0]
        for i in range(len(tobe_testedl_list_of_integers)):
            if tobe_testedl_list_of_integers[i] > baseline:
                baseline = tobe_testedl_list_of_integers[i]
        return baseline
