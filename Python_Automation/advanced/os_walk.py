import os
path = "/Users/kishore/Desktop/temp/"
# print(list(os.walk(path)))

# print("=======================")

# for each in os.walk(path):
#     print(each)

# print("------------------------")

# for root_dir, dir, files in os.walk(path):
#     print(root_dir, dir)
#     print("********************************")
#     print(root_dir, files)

# print("################################")

# for root_dir, dir, files in os.walk(path, topdown=True):
#     print(root_dir, dir)
#     print("********************************")
#     print(root_dir, files)

for r, d, f in os.walk(path, topdown=True):
    if len(f) != 0:
        print(r)
        for each_file in f:
            # print(each_file)
            print(os.path.join(r, each_file))
