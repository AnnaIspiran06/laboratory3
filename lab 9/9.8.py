def count_unique_abs(numbers):
    unique_abs_numbers = {}
    for num in numbers:
        abs_num = abs(num)
        if abs_num in unique_abs_numbers:
            unique_abs_numbers[abs_num] += 1
        else:
            unique_abs_numbers[abs_num] = 1
    return len(unique_abs_numbers)

n = int(input())
numbers = list(map(int, input().split()))

result = count_unique_abs(numbers)
print(result)
