def hpt(a,b):
    if (b == 0): return a
    return hpt(b, a % b)

def lcm(a,b):
    return a*b//hpt(a,b)

n=int(input())
c=1
for i in range(1,n+1):
    c=lcm(c,i)
print(c)
