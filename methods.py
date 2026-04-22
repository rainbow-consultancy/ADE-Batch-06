# methods/functions

def FunctionName():
    pass

# static funtion
def greet():
    print("Hello, world!")
    
 
# greet()  # function call


# dynamic function
def greet(name):
    print(f"Hello, {name}")


# greet("Dileep")
# greet("Kalyan")


def add(a, b):
    print(a+b)
    
# add(10, 20)
# add(30, 23)

# function with return value
def multiply(a, b):
    return a * b

result = multiply(10, 4)
# print(result)

# write a function to check if a given number is even or odd
def check_number(num: int) -> str:
    return f"{num} is Even" if num%2==0 else f"{num} is Odd"

# print(check_number(33))
# print(check_number(20))

# funtions with default values
def add(a: int, b: int = 0) -> int:
    return a + b

# print(add(20, 35))
# print(add(10))


def add(a, c, b=0):
    return a+b+c

# print(add(10, 30))
# print(add(10, 30, 30))


def math_operations(a:int, b:int) -> int:
    return a+b, a-b, a*b

# a, b, c = math_operations(10, 20)
# print(a, b, c)


# Write a function to find the factorial of a given number
# 5 ->  5*4*3*2*1 = 120
# 1*2*3*4*5 = 120

def find_factorial(num: int) -> int:
    f = 1
    for i in range(2, num+1):
        f = f*i
    return f


# print(find_factorial(5))
# print(find_factorial(7))
