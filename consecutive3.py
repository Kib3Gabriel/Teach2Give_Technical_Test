"""
Q5

Design a function that takes a list of integers as input. The function should
return True if the list contains two consecutive threes (3 next to a 3) anywhere
within the list. Otherwise, it should return False. For example, the function
should return True for [1, 3, 3] and False for [1, 3, 1, 3]."""
    

def three_consecutive(nums):
    
    for i in range(len(nums) - 1):
        
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

list_nums = [2,4,3,3]
list_nums2 =[3,5,6,3,9,3]
print(three_consecutive(list_nums))   

print(three_consecutive(list_nums2))

