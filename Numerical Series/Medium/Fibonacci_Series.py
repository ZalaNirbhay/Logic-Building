# Write a Python program to print the first n Fibonacci numbers.
def print_fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")

        next = a + b
        a = b
        b = next


n = int(input("Enter number: "))
print_fibonacci(n)