for count in range(1,31):
    if count % 3 == 0:
        print("Fizz")
    elif count % 5==0:
        print("Buzz")
    elif count % 15==0:
        print("FizzBuzz")
    else:
        print(count)

