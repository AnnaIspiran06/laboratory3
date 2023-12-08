from itertools import permutations

n = int(input())


perms = permutations(range(1, n + 1))


for perm in perms:
    print(*perm)
