#exericse - fizzbuzz
#if number is divided by 3 print Fizz, it is divided by 5 print Buzz,
#if it is divided by both print Fizzbuzz

for fizzbuzz in range(51):
    number = int(input('What number? '))
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print('not fizzbuzz')