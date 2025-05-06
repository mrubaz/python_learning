# def double(x):
#     return x * 2

# when you want to use lambda then you need to declare the function, you can use anonymous function

sum = lambda x: x + 2
double = lambda x: x * x
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print(sum(5))
print(double(2))
print(cube(3))
print(avg(3, 3, 3))
