"""Проверяет строку на четное колличество букв"""
"""abcdefghijklmnopqrstuvwxyz";
   public static final String UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
   public static final String DIGITS = "0123456789";
   public static final String PUNCTUATION = "!@#$%&*()_+-=[]|,./?><"""



some_string = input("Please enter your string: ")

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
