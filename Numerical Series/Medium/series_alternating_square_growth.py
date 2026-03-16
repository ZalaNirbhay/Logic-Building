# Print the series:1 2 4 3 9 4 16 5 25
def series_alternating(n):
    squares,num=1,2
    for i in range(n):
        if i%2==0:
            print(squares,end=" ")
            squares=num*num
        else:
            print(num,end=" ")
            num +=1

n=int(input("Enter the number :"))
series_alternating(n)
            