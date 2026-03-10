# Write a Python program to find the largest element in an array.
# The program should traverse the array and determine the maximum value present in the array.

def find_max(arr):

    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    return largest


arr = [4, 7, 1, 9, 3]

print(find_max(arr))