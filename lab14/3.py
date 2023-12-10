runtime_errors = 0
type_errors = 0
value_errors = 0

while True:
    user_input = input("Введіть число або 'досить' для завершення: ")

    if user_input == 'досить':
        break

    try:
        num = int(user_input)

        if num > 9:
            raise RuntimeError("Введене число більше за 9")
        elif num < 0:
            raise TypeError("Введене число менше за 0")
        elif 0 <= num <= 9:
            raise ValueError("Введене число з діапазону від 0 до 9")

    except RuntimeError:
        runtime_errors += 1
    except TypeError:
        type_errors += 1
    except ValueError:
        value_errors += 1

print(f"Кількість виключень RuntimeError: {runtime_errors}")
print(f"Кількість виключень TypeError: {type_errors}")
print(f"Кількість виключень ValueError: {value_errors}")
