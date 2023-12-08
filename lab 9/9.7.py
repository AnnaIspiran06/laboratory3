n = int(input())
found_cubes = input().split()


count_found = {}
for cube in found_cubes:
    for letter in cube:
        count_found[letter] = count_found.get(letter, 0) + 1


count_alphabet = {letter: 0 for letter in 'abcdefghijklmnopqrstuvwxyz'}


for letter, count in count_found.items():
    count_alphabet[letter] = count


missing_letter = ''
for letter, count in count_alphabet.items():
    if count % 2 != 0:
        missing_letter = letter
        break

if missing_letter:
    print(missing_letter)
else:
    print("Ok")
