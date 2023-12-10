#!/usr/bin/env python3


def happy_new_year():
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Happy New Year!")
    pass


def square_integers(int_list):
    squared_int = [int**2 for int in int_list]
    return squared_int
    pass


def fizzbuzz():
    i = 0
    while i < 100:
        i += 1
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    pass
