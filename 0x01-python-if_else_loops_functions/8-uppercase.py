#!/usr/bin/python3
def uppercase(str):
    
   
    for x in str[:]: 
        if ord(x) >= ord('a') and ord(x) <= ord('z'):
            capital = ord(x)-32
            v = chr(capital)
            print(v , end=(''))
        else:
            print(x, end=(''))

    
    print()
