def transpose(mat):
    if not mat:
        return []

    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("Рваная матрица")

    return [list(row) for row in zip(*mat)]


def row_sums(mat):
    if not mat:
        return []

    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("Рваная матрица: строки разной длины")

    sums = []
    for row in mat:
        row_sum = sum(row)
        sums.append(row_sum)

    return sums


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []

    num_cols = len(mat[0])
    for row in mat:
        if len(row) != num_cols:
            raise ValueError("Рваная матрица")

    sums = [0] * num_cols
    for row in mat:
        for j in range(num_cols):
            sums[j] += row[j]

    return sums


# Тест-кейсы (минимум)

print(col_sums([[1, 2, 3], [4, 5, 6]]))  # [5, 7, 9]
print(col_sums([[-1, 1], [10, -10]]))  # [9, -9]
print(col_sums([[0, 0], [0, 0]]))  # [0, 0]
print(col_sums([[1, 2], [3]]))  # ValueError