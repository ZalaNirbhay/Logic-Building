# Print the following series:1 4 9 2 5 10 3 6 11
def alternate_number(n):
    a,b,c=1,4,9
    for i in range(n):
        if i%3==0:
            print(a,end=" ")
            a +=1
        elif i%3==1:
            print(b,end=" ")
            b +=1
        else:
            print(c,end=" ")
            c +=1
         
n = int(input("Enter number: "))
alternate_number(n)

