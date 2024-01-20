import re

def find_longest_word(file_name):
    with open(file_name, 'r') as file:
        words = file.read().split()
        longest_word = max(words, key=len)
        return longest_word

def count_words(file_name):
    with open(file_name, 'r') as file:
        words = file.read().split()
        return len(words)

def remove_extra_spaces(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        content = re.sub(r'\b\w\b|\s{2,}', '', content)
        return content

def remove_extra_spaces_lines(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        cleaned_lines = [line.strip() for line in lines]
        return cleaned_lines

def insert_spaces_between_words(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        result = []
        for line in lines:
            words = line.split()
            if len(words) > 1:
                word_gaps = len(words) - 1
                spaces_count, extra_spaces = divmod(80 - len(line), word_gaps)
                adjusted_line = (" " * spaces_count).join(words[:-1]) + " " * extra_spaces + words[-1]
                result.append(adjusted_line)
            else:
                result.append(line.strip())
        return result


longest = find_longest_word('Н.txt')
print(f"Найдовше слово: {longest}")


word_count = count_words('Н.txt')
print(f"Кількість слів: {word_count}")


cleaned_content = remove_extra_spaces('Н.txt')
with open('Н.txt', 'w') as output_file:
    output_file.write(cleaned_content)


cleaned_lines = remove_extra_spaces_lines('Н.txt')
with open('Н.txt', 'w') as output_file:
    output_file.write('\n'.join(cleaned_lines))


adjusted_lines = insert_spaces_between_words('Н.txt')
with open('Н.txt', 'w') as output_file:
    output_file.write('\n'.join(adjusted_lines))
