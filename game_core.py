import numpy as np

def game_core_v2(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)
    
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count

def game_core_v3(number: int = 1) -> int:
    """Функция угадывает число методом бинарного поиска.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # Счетчик попыток
    predict = 50 # Начинаем с середины диапазона
    left = 0 # Левая граница диапазона
    right = 100 # Правая граница диапазона
    while number != predict:
        count += 1
        if number > predict:
            left = predict + 1 # Сдвигаем левую границу диапазона
        elif number < predict:
            right = predict - 1 # Сдвигаем правую границу диапазона
            
        predict = (left + right) // 2 # Новое предполагаемое число из середины диапазона
    
    return count # Выход из цикла, если угадали