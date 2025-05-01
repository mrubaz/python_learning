a = int(input("Enter a number : "))

try:
    for i in range(1, 11):
        print(f"{a} x {i} = {a*i}")
except Exception as e:
    print(f"Error: {e}")
