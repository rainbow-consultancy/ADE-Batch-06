# non - primitive data_types


# 1. list 

# nums = [1, 2, 3, 4, 5, 1, 1, 1]

# nums2 = [9, 8, 7]

# # add new items
# nums.append(6)
# print(nums)

# print(nums.count(1))

# nums.extend(nums2)
# print(nums)

# nums.reverse()
# print(nums)

# nums.sort()
# print(nums)

# nums.sort(reverse=True)
# print(nums)

# # print(nums[::2])
# # print(nums[::-1])

# print(nums.index(9))
# print(nums.index(3))

# nums.pop()
# print(nums)

# nums.remove(5)
# print(nums)

# nums[6] = 5
# print(nums)


# tuple

# nums = (1, 1, 1, 2, 3, 3, 3, 3, 4, 5)
# print(nums[0])

# nums[0] = 100
# print(nums)

# print(nums.count(3))
# print(nums.index(3))


# set

# nums = {1, 1, 7, 'a', 'b', 8, 1, 2, 3, 3, 3, 3, 4, 5}
# nums2 = {1, 2, 3, 4, 5}
# print(nums)

# print(nums[0])  -- not supported

# nums.add(10)
# print(nums)

# nums.pop()
# print(nums)

# nums.remove("a")
# print(nums)

# print(nums.intersection(nums2))

# print(nums2.issubset(nums))


# dictionary

# emp_info = {
#     "emp_id": 100,
#     "emp_name": "Karthik",
#     "emp_salary": 40000
# }
# print(emp_info)

# print(emp_info["emp_salary"])

# # add
# emp_info["city"] = "Bengaluru"
# print(emp_info)


# print(emp_info.keys())
# print(emp_info.values())

# emp_info["emp_salary"] = 50000
# print(emp_info)

# emp_info.pop("city")
# print(emp_info)
