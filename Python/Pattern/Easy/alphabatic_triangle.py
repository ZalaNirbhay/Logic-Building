# ch ='A'
# n=6
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(i):
#         print(ch,end=" ")
#         ch=chr(ord(ch)+1)
#     print()
    
        

n=6
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        if k%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()
    
        
            