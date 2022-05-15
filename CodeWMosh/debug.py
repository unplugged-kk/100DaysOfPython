def multiplyyy(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("Start")
print(multiplyyy(1, 2, 3))
