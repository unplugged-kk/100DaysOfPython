def evenNumbers(start, end):
    output = []
    for i in range(start, end+1):
        if i % 2 == 0:
            output.append(i)
            return output


res = evenNumbers(1, 10)
print(res)
