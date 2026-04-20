# if condition:
#     -- code
# else:
#     -- code

n = int(input("Enter a num: "))


# if n > 10:
#     print(n, "is greater then 10")
# else:
#     print(n, "is less then 10")
    
    
# if n > 10 and n < 100:
#     print(n, "is greater then 10 and less then 100")
# elif n >= 100:
#     print(n, "is greater then or equals to 100")    
# else:
#     print(n, "is less then 10")


# short hand notation
result = f"{n} is Even" if n % 2 == 0 else  f"{n} is Odd"
print(result)



    


# string formatters

# 1. .format()

name = "Vamsi"
age = 20
city = "Bangalore"


# print("Hi, this is", name, "and I'm", age, "years's old", "and I'm from", city)

# print("Hi, this is {0} and I'm {1} years's old and I'm from {2}".format(name, age, city))
# print("Hi, this is {n} and I'm {a} years's old and I'm from {c}".format(n=name, a=age, c=city))

    
# # 2. short hand notation (f"")
# print(f"Hi, this is {name} and I'm {age} years's old and I'm from {city}")

# ""
# ''
# """ """

# print(f"Hi, this is {name} and I'm {age} year's old and I'm from {city}")
