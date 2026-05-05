# Print the following series:2 6 7 21 22 66

def pattern_switching(n):
    num=2
    for i in range(n):
        print(num,end=" ")
        if i%2==0:
            num *=3
        else:
            num+=1
n=int(input("Enter the number: "))
pattern_switching(n)
