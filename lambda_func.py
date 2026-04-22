# lambda functions (single line/anonymous)


# Write a function to find the square roots of the numbers in a given list
# and place those square root numbers in the list

num = [1, 2, 3, 4, 5]

# def get_square_roots(nums: list) -> list:
#     result = []
#     for i in nums:
#         result.append(i**2)
#     return result
        
# print(get_square_roots(num))


# result = list(map(lambda x: x**2, num))
# print(result)


# def add(a, b):
#     return a+b

add_num = lambda a, b: a+b

# print(add_num(1, 2))
# print(add_num(10, 45))

# is_even = lambda num: True if num%2 == 0 else False
# print(is_even(3))
# print(is_even(4))
# print(is_even(5))


# 1. map
# 2. filter
# 3. reduce

# iterable datatypes - strings, list, tuple
# syntax - map(function, iterable_item)

num = [1, 2, 3, 4, 5]
result = list(map(lambda x: x**2, num))
# print(result)

names = ('ram', 'vamsi', 'madhu')
result = list(map(lambda name: name.capitalize(), names))
# print(result)

# 2. filter

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = list(filter(lambda x: x%2 == 0, nums))
# print(result)

# applying map to the below
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = list(map(lambda x: x%2 == 0, nums))
# print(result)


# 3. reduce

from functools import reduce

# reduce(func, iterable)

nums = [1, 2, 3, 4]

result = reduce(lambda x, y: x+y, nums)
print(result)

result = reduce(lambda x, y: x*y, nums)
print(result)


# find the max number in a given list
nums = [20, 30, 50, 10, 25, 80, 70, 100]
# def find_max(nums: list) -> int:
#     max_num = nums[0]
#     for i in range(1, len(nums)):
#         if nums[i] > max_num:
#             max_num = nums[i]
#     return max_num
    
# print(f"max number in the given list is - {find_max(nums)}")

result = reduce(lambda a, b: a if a>b else b, nums)
print(result)
