# Write a Python program to print the first n square numbers.
def print_square_number(n):
    for i in range(1,n+1):
        print((i*i),end=" ")
        
n=int(input("Enter the number :"))
print_square_number(n)