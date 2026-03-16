# Write a Python program to print the first n cube numbers.
def print_cube_number(n):
    for i in range(1,n+1):
        print(i*i*i,end=" ")
        
n=int(input("Enter the number :"))
print_cube_number(n)