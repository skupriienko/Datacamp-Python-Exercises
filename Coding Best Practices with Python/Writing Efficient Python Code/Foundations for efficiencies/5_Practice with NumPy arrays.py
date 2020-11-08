import numpy as np
import timeit

nums = np.array([[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10]])

# Print second row of nums
print(nums[1,:])

# Print all elements of nums that are greater than six
print(nums[nums > 6])

# Double every element of nums
nums_dbl = nums *2
print(nums_dbl)

# Replace the third column of nums
nums[:,2] = nums[:,2] + 1
print(nums)
