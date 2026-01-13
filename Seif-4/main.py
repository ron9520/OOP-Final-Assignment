# לולאת REPL לבדיקת מכפלות
import math_utils

while True:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    if a == '-1' or b == '-1':
        break
    try:
        a = int(a)
        b = int(b)
        if math_utils.check_if_multiple(a, b):
            print("One number is a multiple of the other.")
        else:
            print("Neither number is a multiple of the other.")
    except ValueError:
        print("Invalid input. Please enter integers.")