def has_unique_digits(number):
    
    digits = str(number)
    return len(set(digits)) == len(digits)

def print_unique_numbers(a, b):
    
    for num in range(a, b + 1):
        if has_unique_digits(num):
            print(num, end=' ')


a, b = map(int, input().split())


print_unique_numbers(a, b)
