def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("Список пуст")

    minimum = min(nums)
    maximum = max(nums)
    return (minimum, maximum)


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    unique_nums = set(nums)
    sorted_nums = sorted(unique_nums)
    return sorted_nums


def flatten(mat: list[list | tuple]) -> list:
    result_list = []
    for element in mat:
        if type(element) == list or type(element) == tuple:
            for sub_element in element:
                result_list.append(sub_element)
        elif type(element) == str:
            raise TypeError("строка не строка строк матрицы")

        else:
            result_list.append(element)

    return result_list


# Тест-кейсы (минимум)

print(flatten([[1, 2], [3, 4]]))  # [1, 2, 3, 4]
print(flatten([[1, 2], (3, 4, 5)]))  # [1, 2, 3, 4, 5]
print(flatten([[1], [], [2, 3]]))  # [1, 2, 3]
print(flatten([[1, 2], "ab"]))  # TypeError («строка не строка строк матрицы»)