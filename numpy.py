import numpy as np
array=np.array(10)
values_greater_than_4=array[array>4]
print(values_greater_than_4)


# 2 answer

import numpy AS np
random_array = np.random.rand(5, 3)

mean_along_columns = np.mean(random_array, axis=0)
median_along_columns = np.median(random_array, axis=0)
std_dev_along_columns = np.std(random_array, axis=0)

print("Mean along columns:", mean_along_columns)
print("Median along columns:", median_along_columns)
print("Standard deviation along columns:", std_dev_along_columns)

#3 answer
array = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])


flipped_horizontally = np.fliplr(array)

flipped_vertically = np.flipud(array)

print("Original array:")
print(array)
print("\nHorizontally flipped array:")
print(flipped_horizontally)
print("\nVertically flipped array:")
print(flipped_vertically)

#4 answer
fruits = np.array(['apple', 'banana', 'orange', 'cherry'])

fruits_uppercase = fruits.astype(str).upper()

print(fruits_uppercase)

#5 answer
fruits = np.array(['apple', 'banana', 'orange', 'cherry'])


fruits_replaced = np.char.replace(fruits, 'a', '@')

print(fruits_replaced)

#6 answer
array = np.random.randint(-5, 6, (4, 4))
array_multiplied = array * 5
array_transposed = np.transpose(array)





