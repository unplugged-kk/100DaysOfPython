# 153 = 1+ 5 + 3

num = int(input("Enter the number: "))  # 142
sum = 0
while num > 0:   # 142 > 0  14 > 0 1 > 0
    t = num % 10  # t=142%10 = 2 t = 14%10 = 4 t = 1%10 = 1
    sum = sum + t  # s = 0+2+4+1
    num = num // 10  # num = 142 //10 = 14 num = 14 //10 =1 num = 1 //10 = 0

print(sum)
