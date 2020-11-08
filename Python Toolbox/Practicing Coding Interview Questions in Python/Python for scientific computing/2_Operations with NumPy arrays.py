input_list1, input_list2, input_list3 = ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [[1, 2], [3, 4], [5, 6]])

# Substitute the code in the block 1 given the input_array1
output_array1 = 5 * input_array1
print(list(map(lambda x: [5*i for i in x], input_list1)))
print(output_array1)

# Substitute the code in the block 2 given the input_array2
output_array2 = input_array2[input_array2 % 2 == 0]
print(list(filter(lambda x: x % 2 == 0, input_list2)))
print(output_array2)

# Substitute the code in the block 3 given the input_array3
output_array3 = input_array3 * input_array3
print([[i*i for i in j] for j in input_list3])
print(output_array3)
