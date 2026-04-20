# 1. Take a input name from the user and count the no.of vowel chars in his name.

name = input("Enter a name: ")
print(f"name: {name}")

vowels = 'aeiou'
cnt = 0

for ch in name.lower():
    if ch in vowels:
        cnt += 1
        
print(f"The no.of vowels in {name} is - {cnt}")

# 2. Print 2 table
# 2 * 1 = 2
# 2 * 2 = 4
# .
# 2 * 10 = 20


for i in range(1, 11):
    print(f"2 * {i} = {2*i}")


# 3. Print 2 - 5 tables

# 2 * 1 = 2
# 2 * 2 = 4
# .
# 2 * 10 = 20

# 3 * 1 = 3
# 3 * 2 = 6
# .
# 3 * 10 = 30


for i in range(2, 6):
    for j in range(1, 11):
        print(f"{i} * {j} = {i*j}")
