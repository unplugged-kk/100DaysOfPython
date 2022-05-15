numbers = list(range(5))
a, b, c, d, e = numbers

print(a, b, c, d, e)

numbers2 = list(range(10))
first, second, *other = numbers2

print(first, other, second)
