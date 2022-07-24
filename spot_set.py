#!/usr/bin/env


"""
Modified lines of code

vowels = ['a', 'e', 'i', 'o', 'u']
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
Modified using set data structure
"""
vowels = set('aeiou')
word = raw_input("Provide a word to search for vowels: ")
found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)