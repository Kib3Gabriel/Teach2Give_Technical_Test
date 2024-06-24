"""
Q1

Design a function that reverses the digits of an integer. For example, 50 
should become 5 and -12 should become -21."""

def reverse(number):
    rev = 0
    
    negative_num = number < 0
    number = abs(number)
    
    while number > 0:
        digit = number % 10
        rev = rev * 10 + digit
        number = number // 10
    
    return -rev if negative_num else rev

number = int(input("Enter a number: "))

print('Number reversed:',reverse(number))
