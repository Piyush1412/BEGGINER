# Print counting 1 to 100
'''
for i in range(1, 101):
    print(i, end=", ")
'''
# Print counting 1 to 100 all even numbers
'''
for i in range(2, 101, 2):
    print(i,end=' ')
'''
# Print counting 1 to 100 all odd numbers
'''
for i in range(1, 101, 2):
    print(i,end=' ')
'''    
# Left-aligned triangle
'''
n = 5
for i in range(1, n + 1):
    print("*" * i)
'''
# Right-aligned triangle
'''
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
'''
# pyramid by numbers
'''
for i in range(1,5):
    for j in range(1,6-i):
        print(" ",end=' ')
    for j in range(i,0,-1):
        print(j,end=' ')
    for j in range(2,i+1):
        print(j,end=' ')
    print()
'''
# pyramid by *

# Centered pyramid
'''
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
'''
# Inverted left triangle by *
'''
n = 5
for i in range(n, 0, -1):
    print("*" * i)
'''
# inverted right triangle by numbers
'''
for i in range(1,5):
    for j in range(1,5):
        if j>=5-i:
            print(j,end=' ')
        else:
            print(' ',end=' ')
    print()
'''    
#inverted left triangle by numbers
'''
for i in range(1,5):
    for j in range(1,5):
        if j<=5-i:
            print(j,end=' ')
        else:
            print(' ',end=' ')
    print()   
'''
# Inverted pyramid
'''
n = 5
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
'''
# opposite pyramid
'''
for i in range(4, 0, -1):
    print("  " * (4 - i), end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    for j in range(2, i + 1):
        print(j, end=" ")
    print()
'''
# Number triangle
'''
for i in range(1, 5 + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
'''
# Floyd's triangle                     # wrong code
'''
for i in range(1, 5 + 1):
    for j in range(i):
        print(1, end=" ")
    print()
'''
# Alphabet triangle
'''
for i in range(1, 5 + 1):
    for j in range(65, 65 + i):
        print(chr(j), end=" ")
    print()
'''
# Diamond pattern by *
'''
for i in range(1, 5 + 1):
    print(" " * (5 - i) + "*" * (2 * i - 1))
for i in range(5 - 1, 0, -1):
    print(" " * (5 - i) + "*" * (2 * i - 1))
'''
# diamond pattern by numbers                 # wrong pattern
'''
for i in range(1, 5 + 1):
    print(" " * (5 - i), end=" ")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()
for i in range(5 - 1, 0, -1):
    print(" " * (5 - i), end=" ")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()
'''
# new pattern
# **********
# ****  ****
# ***    ***
# **      **
# *        *

for i in range(5):
    print("*" * (5 - i), end="")
    print(" " * (2 * i), end="")
    print("*" * (5 - i))








    














