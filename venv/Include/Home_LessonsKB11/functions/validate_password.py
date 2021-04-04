"""Функция принимает пароль строкой и проверяет его тремя функциями
1. содержит только a-z, A-Z ,0-9
2. Содержит четное колличество букв
3. Содержит нечетное колличество цифр

основная функция возвращает True если пароль валидный

если пароль не валидный возвращает лист стрингов, в которых причины неуспешной проверки
["содержит запрещенные символы"]

"""

some_string = input("Please enter your string: ")

def _validate_symbols(input_str):
    symbol_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for i in input_str:
        if i not in symbol_list:
            return False
    return True

def _validate_letters_even(input_str):
    """Проверяет строку на четное колличество букв"""
    symbol_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counter = 0
    for i in input_str:
        if i in symbol_list:
            counter += 1
    if counter % 2 == 1:
        return False
    if counter % 2 == 0:
        return True

def _validate_numbers_odd(input_str):
    counter = 0
    for i in input_str:
        if i.isdigit():
            counter += 1
    if counter % 2 == 1:
        return True
    if counter % 2 == 0:
        return False

def validate_password(password):
    list_stringov = ["Invalid Symbol!", "Number of Letters is odd!", "Numbers is even!"]
    #_validate_symbols(password)
    #_validate_letters_even(password)
    #_validate_numbers_odd(password)

    if (_validate_symbols(password) == True) and (_validate_letters_even(password) == True) and (_validate_numbers_odd(password) == True):
        return True

    if (_validate_symbols(password) == False) and (_validate_letters_even(password) == False):
        return [list_stringov[0], list_stringov[1]]
    if (_validate_letters_even(password) == False) and (_validate_numbers_odd(password) == False):
        return [list_stringov[1], list_stringov[2]]
    if (_validate_symbols(password) == False) and (_validate_numbers_odd(password) == False):
        return list_stringov[0], list_stringov[2]

    if (_validate_symbols(password) == False):
        return list_stringov[0]
    if (_validate_letters_even(password) == False):
        return list_stringov[1]
    if (_validate_numbers_odd(password) == False):
        return list_stringov[2]

print(validate_password(some_string))
