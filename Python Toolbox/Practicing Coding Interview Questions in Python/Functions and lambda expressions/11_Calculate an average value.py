def average(nums):

    result = 0

    for num in nums:
        result += num

    return result/len(nums)

# Calculate an average value of the sequence of numbers
def average(nums):

    # Base case
    if len(nums) == 1:
        return nums[0]

    # Recursive call
    n = len(nums)
    return (nums[0] + (n - 1) * average(nums[1:])) / n

# Testing the function
print(average([1, 2, 3, 4, 5]))
