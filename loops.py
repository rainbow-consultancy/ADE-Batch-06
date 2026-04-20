# print(1)
# print(2)
# print(3)

# loops in python

# for loop
# while loop

# for i in range(start, end, step=1):
#     code

# for i in range(1, 101):
#     if i == 90:
#         continue  # skip
#     print(i)
    # if i == 90:
    #     break
    
    


# for i in range(1, 101, 2):
#     print(i)


# while -- dangerous loop

i = 1
# while i < 101:
#     print(i)
#     i += 1


# pattern programs

# for i in range(5, 0, -1):
#     print(i * "*")
    
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()