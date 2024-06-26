"""
Домашнее задание №1
Функции и структуры данных
"""


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def power_numbers(*number):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    result = []
    for n in number:
        result.append(pow(n, 2))
    return result
    
def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5 + 1)):
        if a % i == 0:
            return False
    else:
        return True

def filter_numbers(list_numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return list(filter(lambda n: n % 2 == 1, list_numbers))
    elif filter_type == EVEN:
        return list(filter(lambda n: n % 2 == 0, list_numbers))
    elif filter_type == PRIME:
        return list(filter(is_prime, list_numbers))

