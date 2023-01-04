mylist = ["chreey", "apple", 34, "salami", False, True]

print(mylist)
print(mylist[3])
print(mylist[-2])

for item in mylist:
    print(item)

if "salami" in mylist:
    print("salami found")
else:
    print("salami not found")

print(len(mylist))

second_list = list(range(1, 13))
print(second_list)
reversed_list = second_list[::-1]
print(reversed_list)
print(reversed_list[0])

# list comprehension

mylist = list(range(1, 15))

square_list = [i*i for i in mylist]

print(square_list)
print(mylist)
