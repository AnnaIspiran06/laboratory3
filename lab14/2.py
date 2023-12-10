import math

def count_elements(my_list):
    return sum(map(lambda x: 1, my_list))

def calculate_sum(my_list):
    return sum(map(lambda x: x, my_list))

def calculate_max_ratio(my_list):
    max_ratio = max(map(lambda x: x[0] / x[1] if x[1] != 0 else float('-inf'), zip(my_list, my_list[1:])))
    assert not math.isinf(max_ratio), "Помилка: Неможливо обчислити максимальне відношення"
    return max_ratio


my_list = list(map(float, input("Введіть числа через пробіл: ").split()))


count = count_elements(my_list)
assert count >= 0, "Помилка: Кількість елементів у списку не може бути від'ємною"
print("Кількість елементів у списку:", count)


total_sum = calculate_sum(my_list)
assert total_sum >= 0, "Помилка: Сума елементів у списку не може бути від'ємною"
print("Сума елементів у списку:", total_sum)


max_ratio = calculate_max_ratio(my_list)
print("Найбільше відношення серед елементів:", max_ratio)
