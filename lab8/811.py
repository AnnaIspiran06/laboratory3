def g(p):
    if p == 0:
        return 0
    t = p % 10
    return t * (1 + t) // 2 + p // 10 * 45 + g(p // 10)

def s(p, q):
    return g(q) - g(p - 1)

while True:
    p, q = map(int, input().split())
    if p < 0 and q < 0:
        break
    print(s(p, q))
