s=input()
n=int(input())
for i in s:
    print(chr((ord(i)-65-n)%26+65),end="")
