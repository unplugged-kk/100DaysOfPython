mydict = {"name": "rosy", "age": 28, "city": "Jajpur", "country": "india"}
print(mydict)

value = mydict["age"]
print(value)

print(mydict)
new_dict = mydict["email"] = "cool-stuff@gmail.com"
print(new_dict)
print(mydict)

if "city" in mydict:
    print(mydict["city"])

try:
    print(mydict["cityy"])
except:
    print("Error Invalid key")


for key in mydict:
    print(key)
    print(mydict[key])


for key, value in mydict.items():
    print(key, value)
