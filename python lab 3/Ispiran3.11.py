n = int(input())
k = -1
i=1
if n==0:
    k=0
while 10 ** (i - 1) <= n :
    digit = (n % 10 ** i) // 10 ** (i - 1)
    i += 1
    if digit % 2 == 0 :
        if k==-1:
            k=0
        k += digit

print(k)
