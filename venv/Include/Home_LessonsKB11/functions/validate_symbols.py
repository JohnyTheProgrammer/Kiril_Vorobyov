"""Проверяет строку на наличие запрещенных символов (метод проверяющий строку на наличие только букв и цифр"""

some_string = input("Please enter your string: ")

def _validate_symbols(input_str):
    symbol_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for i in input_str:
        if i not in symbol_list:
            print(i)
            return False
    return True


print(_validate_symbols(some_string))