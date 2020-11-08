# Reverse a string using reduce()
string = 'DataCamp'
inv_string = reduce(lambda x, y: y + x, string)
print('Inverted string = ' + inv_string)

# Find common items shared among all the sets in sets
sets = [{1, 4, 8, 9}, {2, 4, 6, 9, 10, 8}, {9, 0, 1, 2, 4}]
common_items = reduce(lambda x, y: set(x).intersection(y), sets)
print('common items = ' + str(common_items))

# Convert a number sequence into a single number
nums = [5, 6, 0, 1]
num = reduce(lambda x, y: str(x)+str(y), nums)
print(str(nums) + ' is converted to ' + str(num))
