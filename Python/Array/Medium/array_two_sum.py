# Write a Python program to find two numbers in an array whose sum equals a given target value.
# Return the indices of those two numbers.

def two_sum(arr,target):
    elems=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                return i,j



# def two_sum(arr,target):
#     map = {}
#     for index, num in enumerate(arr):
#         x = target-num
#         if x in map:
#             return (map[x], index)
#         else:
#             map[num] = index
        

arr = [2, 7, 11, 15]

print(two_sum(arr,26))
