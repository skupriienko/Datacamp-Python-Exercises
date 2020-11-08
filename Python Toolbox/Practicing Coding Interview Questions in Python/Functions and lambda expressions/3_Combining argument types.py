# Define the arguments passed to the function
def sort_all_types(*args, **kwargs):

    # Find all the numbers and strings in the 1st argument
    nums1, strings1 = sort_types(*args)

    # Find all the numbers and strings in the 2nd argument
    nums2, strings2 = sort_types(*kwargs.values())

    return (nums1 + nums2, strings1 + strings2)

res = sort_all_types(
	1, 2.0, 'dog', 5.1, num1 = 0.0, num2 = 5, str1 = 'cat'
)
print(res)
