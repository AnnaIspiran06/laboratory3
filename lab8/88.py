n = int(input())

bin_n = bin(n)[3:]  

operations = ''
for bit in bin_n:
    if bit == '1':
        operations += 'SX'
    else:
        operations += 'S'


print(operations)
