# 1. Simple if statement with user input\
'''
x = int(input("1. Enter a number (x): "))
if x > 5:
    print("x is greater than 5")
'''
# 2. if-else statement
'''
x = int(input("2. Enter a number (x): "))
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
'''
# 3. if-elif-else statement
'''
x = int(input("3. Enter a number (x): "))
if x > 0:
    print("Positive number")
elif x == 0:
    print("Zero")
else:
    print("Negative number")
'''
# 4. Multiple elif conditions for grading
'''
marks = int(input("4. Enter your marks (0–100): "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: F")
'''
# 5. Nested if statements
'''
x = int(input("5. Enter a number (x): "))
if x > 10:
    print("x is greater than 10")
    if x < 20:
        print("x is also less than 20")
    else:
        print("x is 20 or more")
'''
# 6. Logical operators
'''
a = int(input("6. Enter value for a: "))
b = int(input("6. Enter value for b: "))

if a > 0 and b > 0:
    print("Both are positive")

if a > 0 or b < 0:
    print("At least one is positive")

if not (a < 0):
    print("a is not negative")
'''
# 7. One-line if
'''
x = int(input("7. Enter a number (x): "))
if x > 0: print("Positive")
'''
# 8. Ternary if-else
'''
x = int(input("8. Enter a number to check even/odd: "))
print("Even" if x % 2 == 0 else "Odd")
'''
# 9. Chained ternary (if-elif-else style)
'''
score = int(input("9. Enter your score (0–100): "))
print("Grade A" if score >= 90 else "Grade B" if score >= 80 else "Grade C")
'''
