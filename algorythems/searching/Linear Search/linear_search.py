# Given an array of integers, find the index of the target element.
# If the element is not present, return -1.

# def linear_search(arr,target):
#     for i in range(len(arr)):
#         if arr[i]==target:
#             return i
#     return -1

def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

arr = [15, 22, 9, 33, 7]
target = 33

print(linear_search(arr,target))