# Part 01
class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def details(self):
        return print(f"My Name is {self.name} and my age is {self.age}.")


# Decorator function
def decorator(func):
    def returner():
        print("Hi, Good Morning")
        func()
        print("Thanks for using")

    return returner


# Creating Objects
name = str(input("ENter your name: "))
age = int(input("Enter your age: "))
per = Person(name, age)


@decorator
def greet():
    per.details()


greet()
