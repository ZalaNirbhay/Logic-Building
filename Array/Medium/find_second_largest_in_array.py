# Write a Python program to find the second largest element in an array.
# The program should return the second highest value present in the array.


def find_second_largest(arr):
    largest=arr[0]
    second_largest=float('-inf')
    for i in  range(len(arr)):
        # chek is number is larger that the existing
        # largest number then it set second largest number as
        # current largest number and then set the founded
        # new largest number as largets number
        if arr[i]>largest:
            second_largest=largest
            largest=arr[i]
            # cheking if number is greater than second largest
            # and not equal to largest then store it as second largest
        elif arr[i]>second_largest and arr[i] !=largest:
            second_largest=arr[i] 
            
    return [second_largest]

arr = [10, 5, 20, 8, 15]

print(find_second_largest(arr))