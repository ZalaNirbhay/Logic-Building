# Print the series:3 9 27 81 82 83 84

def multiplication_number(n):
    num=3
    for i in range(n):
        print(num,end=" ")
        if i<3:
            num=num*3
        else:
            num +=1

n=int(input("Enter the number:"))
multiplication_number(n)
        