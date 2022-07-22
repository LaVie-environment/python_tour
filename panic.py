#!/usr/bin/env
phrase = "Don't panic!"
plist = list(phrase)

new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])
print(new_phrase)

"""
for i in range(4): #pops the last four objects from "plist"
    plist.pop()
plist.pop(0) # get rid of the object at index 0 of "plist"
plist.remove("'") # find then remove the apostrophe from the list
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
"""