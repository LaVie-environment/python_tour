#!/usr/bin/python

def my_product():

    try:
        for i in ['a','b','c']:
            print(i**2)
    except:
        print("General Error")

my_product()