n=5
num=1
for i in range(n):
    row=[]
    for j in range(n):
        row.append(num)
        num +=1
        
    if i%2==0:
        for x in row:
            print(x,end=" ")
    else:
        for x in row[::-1]:
            print(x,end=" ")
    print()
