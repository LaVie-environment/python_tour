
"""
happy_android = "Doro"
letters = list(happy_android)
for char in letters:
    print('\t', char)
"""

happy_android = "Doro, the happy Android man"
letters = list(happy_android)
for char in letters[:6]:
    print('\t', char)
print()
for char in letters[-7:]:
    print('\t'*2, char)
print()
for char in letters[12:20]:
    print('\t'*3, char)