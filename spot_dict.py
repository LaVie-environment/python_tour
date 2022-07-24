#!/usr/bin/env

"""
Using list to search for vowels in a user's input

vowels = ['a', 'e', 'i', '0', 'u']
word = raw_input("Provide a word to search for vowels: ")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)

"""

"""
Using a dictionary to store the found vowels
Dictionary stores objects as key/value pair
Initialize a dictionary with zeroed data
Iterate over a dictionary using key/value pair
When iterating over a dictionary with for loop, the interpreter only processed the dictionary's keys
Put each key within square brackets and use it together with the dictionary name to gain access to the values associated with the key

Think of a dictionary as a collection of rows, with each row containing exactly two columns

The built-in items method returns a list of key/value pairs.
"""


vowels = ['a', 'e', 'i', 'o', 'u']
word = raw_input("Provide a word to search for vowels: ")
found = {}

for letter in word:
    if letter in vowels:
       found.setdefault(letter, 0)
       found[letter] += 1
for key, value in sorted(found.items()):
    print(key, 'was found', value, 'time(s).')