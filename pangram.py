"""
Q4
Design a function that determines whether a given string is a pangram. A
pangram is a sentence or phrase containing every letter of the alphabet at
least once. Punctuation and case are typically ignored. For example, the
string "The quick brown fox jumps over the lazy dog" is a pangram, while
"Hello, world!" is not.
"""

def isPangram(string):
    alphabet_char = "abcdefghijklmnopqrstuvwxyz"

    for char in alphabet_char:
        if char not in string.lower():
            return False
        
    return True

string_input = input(("Enter a sententence or word :"))

if (isPangram(string_input) == True):
    print("Is a paragram")
else:
    print("Not a paragram")
