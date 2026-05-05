# Write a Python program to count how many even numbers are present in an array.
# The program should traverse the array and count elements divisible by 2.


def count_even(arr):
    total_even_number=0
    for num in arr:
        if num%2==0:
            total_even_number+=1
    return total_even_number

arr = [4, 7, 2, 9, 6, 3]
print(count_even(arr))