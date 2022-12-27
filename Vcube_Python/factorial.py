# factorial

# 5 - 5*4*3*2*1

num = int(input("Enter a Number: "))
fact = 1
while num >= 1:
    fact = fact * num
    num = num - 1
print(fact)
