def count_even_numbers(file_name):
    with open(file_name, 'r') as file:
        numbers = [int(number) for number in file.read().split()]
    count = sum(1 for num in numbers if num % 2 == 0)
    return count

def count_squares_of_odd_numbers(file_name):
    with open(file_name, 'r') as file:
        numbers = [int(number) for number in file.read().split()]
    count = sum(1 for num in numbers if num % 2 != 0 and int(num ** 0.5) ** 2 == num)
    return count

def difference_max_min(file_name):
    with open(file_name, 'r') as file:
        numbers = [int(number) for number in file.read().split()]
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    max_even = max(even_numbers) if even_numbers else float('-inf')
    min_odd = min(odd_numbers) if odd_numbers else float('inf')
    difference = max_even - min_odd if max_even != float('-inf') and min_odd != float('inf') else None
    return difference

def longest_increasing_sequence_length(file_name):
    with open(file_name, 'r') as file:
        numbers = [int(number) for number in file.read().split()]
    longest_length = 0
    current_length = 1
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            current_length += 1
        else:
            longest_length = max(longest_length, current_length)
            current_length = 1
    longest_length = max(longest_length, current_length)
    return longest_length


file_name = 'file.txt'

result1 = count_even_numbers(file_name)
result2 = count_squares_of_odd_numbers(file_name)
result3 = difference_max_min(file_name)
result4 = longest_increasing_sequence_length(file_name)

print("Кількість парних чисел:", result1)
print("Кількість квадратів непарних чисел:", result2)
print("Різниця між найбільшим парним і найменшим непарним числами:", result3)
print("Кількість компонент у найдовшій зростаючій послідовності:", result4)
