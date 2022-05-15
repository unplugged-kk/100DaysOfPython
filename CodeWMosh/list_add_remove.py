from operator import le


letters = ["a", "b", "c", "d"]

# Add

letters.append("e")
print(letters)
letters.insert(0, "f")
print(letters)

# Remove

letters.pop(0)
print(letters)
letters.remove("d")
print(letters)

del letters[0:2]
print(letters)
letters.clear()
print(letters)
