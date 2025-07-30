''''''
# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
first_element = my_list[0]
last_element = my_list[-1]

# Slicing
sub_list = my_list[1:4]

# Adding elements
my_list.append(6)
my_list.insert(2, 10)

# Extending list
my_list.extend([7, 8])

# Removing elements
my_list.remove(10)
popped_element = my_list.pop()
del my_list[0]

# Finding elements
index_of_3 = my_list.index(3)
count_of_2 = my_list.count(2)

# Sorting and reversing
my_list.sort()
my_list.reverse()

# Copying a list
copied_list = my_list.copy()

# Clearing a list
my_list.clear()

# List comprehension
squared = [x**2 for x in range(5)]

# Printing results
print("First element:", first_element)
print("Last element:", last_element)
print("Sub list:", sub_list)
print("Popped element:", popped_element)
print("Index of 3:", index_of_3)
print("Count of 2:", count_of_2)
print("Squared:", squared)
print("Copied list:", copied_list)

sample_list = [10, 20, 30, 40, 50]
sample_list = sample_list[:1] + sample_list[2:]
print("List after removing second position value:", sample_list)