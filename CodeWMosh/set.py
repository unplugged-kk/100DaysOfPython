numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}
print(first | second)
print(first & second)
print(first - second)

print(first ^ second)
# | = union , & = intersection , - = difference , ^ = schematic difference (nos present either in 1st or second)
