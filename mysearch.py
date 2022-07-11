#!/usr/bin/env

def searchVowels():
    vowels = set('aeiou')
    anyword = raw_input('Please provide a word to search for vowels: ')
    found = vowels.intersection(set(anyword))
    for vowel in found:
        if vowel in found:
            print("The {} word exist in {} vowel" .format(anyword, vowels))
        else:
            return "It does not exist"

searchVowels()

"""
An alternative is written below
"""

def searchVowels(phrase: str) -> set:
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

searchVowels() #pass in a string as a parameter