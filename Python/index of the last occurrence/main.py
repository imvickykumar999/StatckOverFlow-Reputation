
'''
Find the index of the rightmost maximum value 
in a list of numbers without using iterations
'''

nums = [8,5,15,2,15,7,3,4]
max_index = len(nums) - nums[::-1].index(max(nums)) - 1
print(max_index)

# ----------------------------------------------

nums = [8, 5, 15, 2, 15, 7, 3, 4]
last_max_index = max((i for i, x in enumerate(nums) if x == max(nums)))
print(last_max_index)

# -----------------------------------------------

nums = [8, 5, 15, 2, 15, 7, 3, 4]
indexed_nums = [(value, index) for index, value in enumerate(nums)]
indexed_nums.sort()
_, last_max_index = indexed_nums[-1]
print(last_max_index)
