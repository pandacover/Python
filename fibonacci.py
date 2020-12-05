def fibonacci(n):
    a = 0
    b = 1
    if n <= 0:
        print("Invalid input")
    
    elif n == 1:
        return a
    
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b

print(fibonacci(int(input("Enter the index for the term: "))))