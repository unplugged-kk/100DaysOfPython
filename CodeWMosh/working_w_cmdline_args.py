import sys

print(sys.argv)

if len(sys.argv) == 1:
    print("USAGE: python3 working_w_cmdline_args.py <password>")
else:
    password = sys.argv[1]
    print("Password", password)
