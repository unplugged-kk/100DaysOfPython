from operator import le


letters = ["a", "b", "c"]

for letter in letters:
    print(letter)

for letter in enumerate(letters):
    print(letter)

for index, letter in enumerate(letters):
    print(index, letter)
