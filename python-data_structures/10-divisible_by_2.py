#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    listo = []
    for i in my_list:
        if i % 2 == 0:
            listo.append(True)
        else:
            listo.append(False)
    return listo
