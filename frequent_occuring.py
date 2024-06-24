"""
Q3
Design a function that takes a string or sequence of characters as input and
returns the character that appears most frequently."""

def most_frequent_char(input_string):

    char_frequency = {}

    for char in input_string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    
    max_char = max(char_frequency, key=char_frequency.get)
    
    return max_char

string_number = input("Enter a a number or a string:")

print(most_frequent_char(string_number))
