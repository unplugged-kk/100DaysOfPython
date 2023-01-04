my_tuple = ("Zookeeper", "Ramya", "silu")
print(type(my_tuple))


item = my_tuple[2]
print(item)

new_tuple = ("max", "xro", 45, "zoraver")

first, second, third, fourth = new_tuple

print(third, fourth)

neuu_tuple = (0, 1, 1, 3, 7, 9)
a1, b1, c1, *d1, e1 = neuu_tuple

print(a1, c1, *d1, e1)
