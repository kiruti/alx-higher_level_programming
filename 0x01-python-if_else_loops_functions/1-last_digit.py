#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    buff=number * -1
else:
    buff=number
last_dig = abs(number) % 10
print(f"Last digit of {number}is {last_dig}")
if last_dig > 5:
    print("and is greater than 5")
elif last_dig == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
