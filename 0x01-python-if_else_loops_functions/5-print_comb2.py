#!/usr/bin/python3
for i in range(0, 100):
    a = "{0:02d}".format(i)
    if a != "99":
         x = a+","
    else:
        x = "99"

    print(x , end="")  

