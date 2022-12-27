def fizz_buzz(input):
    if (input % 3 == 0) & (input % 5 == 0):
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"


print(fizz_buzz(17))
