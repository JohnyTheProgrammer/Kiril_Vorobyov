"""Проверяет строку на нечетное колличество цифр"""

def _validate_numbers_odd(input_str):
    counter = 0
    for i in input_str:
        if i.isdigit():
            counter += 1
    if counter % 2 == 1:
        return True
    if counter % 2 == 0:
        return False

