"""Напишите функцию для транспонирования матрицы"""

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


# Пример использования
original_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = transpose_matrix(original_matrix)
for row in transposed:
    print(row)
