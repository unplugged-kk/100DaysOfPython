item = [
    ("product1", 10),
    ("product2", 4),
    ("product3", 17)
]

# pricess = []

# for item in item:
#     pricess.append(item[1])
# print(pricess)

prices = list(map(lambda item: item[1], item))
print(prices)
