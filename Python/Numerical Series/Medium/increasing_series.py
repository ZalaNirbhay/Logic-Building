# Print the following series: 2 5 9 14 20
def increasing_series(n):
    increse=3
    val=2
    for i in range(n):
        print(val,end=" ")
        val= val + increse
        increse +=1
    
n=int(input("Enter the number :"))
increasing_series(n)

        