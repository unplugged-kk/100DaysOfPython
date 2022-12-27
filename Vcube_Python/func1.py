def info(name, age):
    output = 'my friend name is {} and age is {}'
    output = output.format(name, age)
    print(output)


info("raju", 34)


def info(*args, **kwargs):
    print(kwargs)
    print(args)


info(10, 5689, name="kk", age=33, gender="Male")
