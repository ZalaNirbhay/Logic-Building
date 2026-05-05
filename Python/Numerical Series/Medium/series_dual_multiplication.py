# Series:2 4 12 24 72 144
def series_dual_multiplication(n):
    a=2
    for i in range(n):
        print(a,end=" ")
        if i%2==0:
            a*=2
        else:
            a*=3

n=int(input("Enter the number :"))
series_dual_multiplication(n)
        