# Write a Python program to print the following series:1 4 3 16 5 36 7 64

def series_odd_square(n):
    a,b=1,2
    for i in range(n):
        if i%2==0:
            print(a,end=" ")
            a +=2
        else:
            print(b*b,end=" ")
            b+=2
            
            
n=int(input("Enter the number:"))
series_odd_square(n)