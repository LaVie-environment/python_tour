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