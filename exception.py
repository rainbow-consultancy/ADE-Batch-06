# Exception Handling

def divide(a, b):
    return a/b

# print(divide(10, 2)) 
# print(divide(10, 0)) # error - zero division
# print(divide(100, 4))

# def divide(a, b):
#     result = ''
#     try:
#         result = a/b
#     except ZeroDivisionError:
#         print("Can't divide by zero")
        
#     return 'Fix the error' if result == '' else result
        
# print(divide(10, 2)) 
# print(divide(10, 0))
# print(divide(100, 2))

# def divide(a, b):
#     result = ''
#     try:
#         result = a/b
#     except ZeroDivisionError :
#         print("Can't divide by zero")
#     except ValueError:
#         raise Exception
#     finally:
#         return 'Fix the error' if result == '' else result
        

# print(divide(10, 2)) 
# print(divide(10, 0))
# print(divide(8, 'qwer'))
# print(divide(100, 4))


# try:
#     age = int(input("Enter your age: "))
#     print(age)
# except:
#     print("Please enter numbers only")


# try:
#     age = int(input("Enter your age: "))
#     print(age)
# except ValueError:
#     print("ValueError - Please enter numbers only")
    
# try:
#     age = int(input("Enter your age: "))
#     print(age)
# except Exception as e:
#     print(e)
    
    
    
    

try:
    print(10/2)
except Exception as e:
    print(e)
finally:
    print("program ended")