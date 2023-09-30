import sys
sys.set_int_max_str_digits(6000)
a=int(input())
k=1
while a!=1:   
    k+=1
    a=a//k
print(k)
