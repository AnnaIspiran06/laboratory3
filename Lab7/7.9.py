def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def reverse_number(n):
    return int(str(n)[::-1])


def get_next_lucky_prime(K):
    found_primes = 0
    current_number = 2 

    while True:
        if is_prime(current_number):
            reversed_number = reverse_number(current_number)
            if current_number != reversed_number and is_prime(reversed_number):
                found_primes += 1
                if found_primes == K:
                    return current_number
        current_number += 1

    return -1  



K = int(input())


result = get_next_lucky_prime(K)

# Виводимо результат
print(result)
