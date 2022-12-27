# digit count

num = int(input("Enter your number:"))

digit_count = 0

while num > 0:
    num = num // 10
    digit_count += 1
print("Digit count: ", digit_count)
