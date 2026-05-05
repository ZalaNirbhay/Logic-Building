# Write a Python program to print the first n even numbers.
def print_even_number(n):
    for i in range(1, n+1):
        print(2*i, end=" ")

n = int(input("Enter the number: "))
print_even_number(n)