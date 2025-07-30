# ALL LOOPS

# 1. Basic while loop
'''
i = 1
while i <= 5:
    print("1.", i)
    i += 1
'''
# 2. while loop with else
'''
i = 1
while i <= 3:
    print("2.", i)
    i += 1
else:
    print("2. Done with while loop")
'''
# 3. Infinite while loop with break
'''
i = 0
while True:
    print("3.", i)
    i += 1
    if i == 3:
        break
'''
# 4. while loop with continue
'''
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print("4.", i)
'''
# 5. for loop over a list
'''
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("5.", fruit)
'''
# 6. for loop with range()
'''
for i in range(5):  # 0 to 4
    print("6.", i)
'''
# 7. for loop with range(start, stop, step)
'''
for i in range(1, 10, 2):  # 1, 3, 5, 7, 9
    print("7.", i)
'''
# 8. for loop with else
'''
for i in range(3):
    print("8.", i)
else:
    print("8. Finished loop without break")
'''
# 9. for loop with break and else
'''
for i in range(5):
    if i == 3:
        break
    print("9.", i)
else:
    print("9. This won't print because of break")
'''
# 10. Nested for loops
'''
for i in range(1, 4):
    for j in range(1, 3):
        print(f"10. i={i}, j={j}")
'''
# 11. Nested while loops
'''
i = 1
while i <= 2:
    j = 1
    while j <= 2:
        print(f"11. i={i}, j={j}")
        j += 1
    i += 1
'''
