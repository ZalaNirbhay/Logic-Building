# Print the series:2 3 5 9 17 33
def series_exponential(n):
    num,diff=2,1
    for i in range(n):
        print(num,end=" ")
        num = num+diff
        diff=diff*2

n=int(input("Enter the number:"))
series_exponential(n)