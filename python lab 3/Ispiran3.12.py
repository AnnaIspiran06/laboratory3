n = int(input())
k = 0
n1 = 0
while n != n1 :
    i = 1
    n1 = 0
    while 10 ** (i - 1) <= n :
        digit = (n % 10 ** i) // 10 ** (i - 1)
        i += 1
        n1 = n1 * 10 + digit

    if n==n1 :
        print(k)
    else:
        n=n1+n
        k += 1
