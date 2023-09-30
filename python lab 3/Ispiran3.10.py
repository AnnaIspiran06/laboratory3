n = int(input())
n1=0
i=1
if n==0 :
    n1=1 


while 10 ** (i - 1) <= n :
    digit = (n % 10 ** i) // 10 ** (i - 1)
    if digit % 2==0 :
        digit += 1
    else :
        digit -= 1
    n1=n1 + digit * 10**(i-1)
    i += 1

print(n1)
