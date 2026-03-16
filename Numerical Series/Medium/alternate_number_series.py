# Write a Python program to print the following series: 1 4 2 5 3 6 
def alternate_number(n):
    a,b=1,4
    for i in range(n):
        if i%2==0:
            print(a,end=" ")
            a +=1
        else:
            print(b,end=" ")
            b +=1
         
n = int(input("Enter number: "))
alternate_number(n)