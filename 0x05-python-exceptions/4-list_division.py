#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            a = my_list_1[i] if i < len(my_list_1) else 0
            b = my_list_2[i] if i < len(my_list_2) else 0
            if b == 0:
                raise ZeroDivisionError
            if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
                raise TypeError
            division_result = a / b
        except ZeroDivisionError:
            division_result = 0
            print("division by 0")
        except TypeError:
            division_result = 0
            print("wrong type")
        except IndexError:
            division_result = 0
            print("out of range")
        finally:
            result.append(division_result)
    return result
