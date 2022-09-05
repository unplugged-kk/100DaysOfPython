import sys
# print(sys.version)
# print(sys.version_info)
# print(sys.modules)

# print(sys.argv)
# Run script normally
# # sys.exit()  # helps to exit the script
# # print(sys.path)

# usr_str = input("Enter Your String: ")
# usr_action = input(
#     "Enter your actions on the string (valid actions are lower/upper/title): ")

# if usr_action == "lower":
#     print(usr_str.lower())
# if usr_action == "upper":
#     print(usr_str.upper())
# if usr_action == "title":
#     print(usr_str.title())

# Run script using sys.argv
print(sys.argv)
usr_str = sys.argv[1]
usr_action = sys.argv[2]

if usr_action == "lower":
    print(usr_str.lower())
if usr_action == "upper":
    print(usr_str.upper())
if usr_action == "title":
    print(usr_str.title())
