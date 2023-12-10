import os

def read_numbers_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = [float(line.strip()) for line in file.readlines()]
            return numbers
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено")
        return []
    except PermissionError:
        print(f"Немає доступу до файлу {file_path}")
        return []
    except ValueError:
        print(f"Файл {file_path} містить не лише дійсні числа")

def process_files_from_content_file(content_file):
    try:
        with open(content_file, 'r') as file:
            file_list = file.read().splitlines()

            total_sum = 0.0

            for file_name in file_list:
                file_path = os.path.join(os.path.dirname(content_file), file_name)
                if os.path.exists(file_path):
                    numbers = read_numbers_from_file(file_path)
                    if numbers:
                        total_sum += sum(numbers)
                else:
                    print(f"Файл {file_name} не знайдено")

            print(f"Загальна сума чисел з файлів: {total_sum}")

    except FileNotFoundError:
        print(f"Файл {content_file} не знайдено")
    except PermissionError:
        print(f"Немає доступу до файлу {content_file}")


content_file_path = 'content.txt'

if os.path.exists(content_file_path):
    process_files_from_content_file(content_file_path)
else:
    print(f"Файл {content_file_path} не існує або не доступний для читання")
