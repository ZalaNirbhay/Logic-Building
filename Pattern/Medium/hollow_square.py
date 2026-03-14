n=5
for i in range(n+1):
    for j in range(n+1):
        if i==0 or i==n or j==0 or j==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()
