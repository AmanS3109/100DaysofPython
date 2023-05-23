for number in range(0, 16):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(number)
