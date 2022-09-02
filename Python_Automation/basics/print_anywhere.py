import os
tw = os.get_terminal_size().columns
given_str = input("Enter your String: ")

print(given_str.center(tw))
print(given_str.ljust(tw))
print(given_str.rjust(tw))
