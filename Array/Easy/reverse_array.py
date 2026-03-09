# Write a Python program to reverse an array.
# The program should return the array with elements in reverse order.

# first way 
def reverse_array(arr):
    rev_array=[]
    for i in range(len(arr)-1, 0, -1):
        rev_array.append(arr[i])
    return rev_array + [arr[0]]
# second way
def reverse_array_1(arr):
    rev_array=[]
    for i in range(len(arr)):
        rev_array.append(arr.pop())
    return rev_array

arr = [1, 2, 3, 4, 5]
print(reverse_array(arr))
print(reverse_array_1(arr))
