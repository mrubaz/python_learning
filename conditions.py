# Print Even and Odd numbers
# num = int(input("Enter your number : "))

# if num > 0 and num % 2 == 0:
#     print("Your number is Even")
# else:
#     print("Oops! Your number is Odd")

# Print Prime Numbers
num = int(input("Enter your number : "))

if num <= 1:
    print("0 and 1 are not prime numbers")

for i in range(2, num):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, "is a prime number")
