# Write a Python program to print the first n natural numbers in a series.
def print_n_natural_number(n):
    for i in range(1,n+1):
        print(i,end=" ")
        
n=int(input("Enter the number :"))
print_n_natural_number(n)