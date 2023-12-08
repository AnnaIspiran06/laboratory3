n = int(input())


thirteen_digits = '0123456789ABC'  

thirteen_representation = ''
while n > 0:
    remainder = n % 13  
    thirteen_representation = thirteen_digits[remainder] + thirteen_representation  # Додаємо нову цифру зліва
    n //= 13  

print(thirteen_representation)
