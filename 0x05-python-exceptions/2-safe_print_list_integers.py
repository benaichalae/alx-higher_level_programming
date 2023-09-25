#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_count = 0
    i = 0
    try:
        while i < x:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                printed_count += 1
            i += 1
    except IndexError:
        pass
    print("")
    return printed_count
