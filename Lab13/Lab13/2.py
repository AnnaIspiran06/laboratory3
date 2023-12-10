def create_text_file():
    text = input("Введіть текст: ")
    with open('output.txt', 'w', encoding='utf-8') as file:
        while len(text) > 0:

            line = text[:40]

            line = line.ljust(40)

            file.write(line + '\n')

            text = text[40:]

create_text_file()
