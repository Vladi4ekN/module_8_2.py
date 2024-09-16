def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple, set)):
            raise TypeError('В numbers записан некорректный тип данных')

        total_sum, incorrect_data = personal_sum(numbers)

        count = len(numbers) - incorrect_data
        if count == 0:
            return 0

        return total_sum / count

    except ZeroDivisionError:
        return 0
    except TypeError as e:
        print(e)
        return None

print(calculate_average([1, 2, 3, 4, 5]))
print(calculate_average([1, 'a', 3, None, 5]))
print(calculate_average([]))
print(calculate_average(1.23))
print(calculate_average([1, 2, 'b', 4, 'c']))
