def evenNumbers(start, end):
    for i in range(start, end+1):
        if i % 2 == 0:
            return i


res = evenNumbers(1, 10)
print(res)
