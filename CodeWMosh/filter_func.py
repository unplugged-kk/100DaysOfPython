items = [
    ("product1", 10),
    ("product2", 4),
    ("product3", 17)
]

filtered = list(filter(lambda item: item[1] >= 10, items))

print(filtered)
