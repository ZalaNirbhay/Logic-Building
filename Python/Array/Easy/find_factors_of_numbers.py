n=int(input("enter you number :"))

def find_factores(n):
    factores={1,n}
    sqrt_n=int(n**0.5)
    for i in range(2,sqrt_n+1):
        if n%i==0:
            factores.add(i)
            factores.add(n//i)
    return factores
        
print(find_factores(n))