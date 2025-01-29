#!/usr/bin/python3

import max_test_module

def max():
    print('max:local namespace called')

print(max_test_module.test_max())