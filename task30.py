# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки

# pytest -v tests\test_30.py

def arithmetic_progression(first: int,
                           diff: int,
                           quantity: int) -> list[int]:
    """Возвращает список арифметической прогрессии по заданным:
    1) первый элемент
    2) разность
    3) количество элементов"""

    list = []
    for i in range(1, quantity + 1):
        list1.append(first + diff*(i - 1)
    return list1
                     
                     
                     
