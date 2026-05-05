# Write a Python program to print the first n odd numbers.
def print_odd_number(n):
    for i in range(1, n+1):
        print(2*i - 1, end=" ")

n = int(input("Enter the number: "))
print_odd_number(n)