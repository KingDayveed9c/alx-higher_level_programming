#!/usr/bin/python3
for dig in range(100):
    print("{:d}".format(dig).rjust(2, "0"), end="\n" if dig == 99 else ", ")
