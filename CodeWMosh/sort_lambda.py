
numbers = [3, 56, 78, 1, 0]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
print(sorted(numbers, reverse=True))
print(numbers)

item = [
    ("product1", 10),
    ("product2", 4),
    ("product3", 17)
]

item.sort()
print(item)


# def sort_it(item):
#     return item[1]


# item.sort(key=sort_it)

# we can improve the code using lambda
# lambda example (key=lambda parameters: expression)
item.sort(key=lambda item: item[1])

print(item)
