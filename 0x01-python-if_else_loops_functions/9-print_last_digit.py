#!/usr/bin/env python3

def print_last_digit(number):
    
    x = number % 10
    d = str(number)
    f = '{}'.format(d[-1])
    print(f, end ="")
    return (f)
