#  Recursive Sum Function (1 to n)
# def fibonacci(n):
#     if n < 1:
#         return n
#     else:
#         return n * fibonacci(n)


# num = int(input("Enter a number: "))
# result = fibonacci(num)
# print(f"Result = {result}")
# print(f"The {n}th Fibonacci number is {fibonacci(n)}")


# find the nth number in the Fibonacci sequence using recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("Enter a number: "))
print(f"The {num}th Fibonacci number is {fibonacci(num)}")
