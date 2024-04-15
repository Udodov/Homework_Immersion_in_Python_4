"""Напишите функцию для транспонирования матрицы.
Если матрица задаётся пользователем."""

from typing import List


def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Транспонирует заданную матрицу.

    :param matrix: Исходная матрица для транспонирования
    :type matrix: List[List[int]]
    :return: Транспонированная матрица
    :rtype: List[List[int]]
    """
    # Получение размеров исходной матрицы
    rows, cols = len(matrix), len(matrix[0])

    # Создание новой матрицы с перевернутыми размерами
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    # Заполнение новой матрицы элементами из исходной
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix


def input_matrix() -> List[List[int]]:
    """
    Запрашивает у пользователя ввод матрицы.

    :return: Матрица, заданная пользователем
    :rtype: List[List[int]]
    """
    rows = int(input("Введите количество строк матрицы: "))
    matrix = []

    print("Введите элементы матрицы построчно, разделяя числа пробелами:")
    for _ in range(rows):
        inner_row = list(map(int, input().split()))
        matrix.append(inner_row)

    return matrix


# Запрашиваем у пользователя данные для создания матрицы
user_matrix = input_matrix()

# Транспонируем матрицу и выводим результат
transposed = transpose_matrix(user_matrix)
print("Транспонированная матрица:")
for row in transposed:
    print(row)
