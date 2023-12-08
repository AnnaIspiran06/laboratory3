def count_ones(a, b):
    total_ones = 0
    bit = 1
    while bit <= b:
        total_ones += (b // (bit * 2)) * bit + max(0, (b % (bit * 2)) - bit + 1)
        total_ones -= (a - 1) // (bit * 2) * bit + max(0, ((a - 1) % (bit * 2)) - bit + 1)
        bit <<= 1
    return total_ones

a, b = map(int, input().split())
result = count_ones(a, b)
print(result)
