# Print the series:1 11 2 10 3 9 4 8 5 7 6
def two_pointer_series(n):
    a,b=1,11
    for i in range(n):
        if i%2==0:
            print(a,end=" ")
            a +=1
        else:
            print(b,end=" ")
            b -=1
        
n=int(input("Enter the number :"))
two_pointer_series(n)