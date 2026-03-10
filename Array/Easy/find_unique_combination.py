n=int(input("enter you number :"))

def unique_combinations(n):
    uniques=[]
    for row in range(1,n+1):
        for col in range(row+1,n+1):
            uniques.append((row,col)) 
    return uniques

print(unique_combinations(n))
        