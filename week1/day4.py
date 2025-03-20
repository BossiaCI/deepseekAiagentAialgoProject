# data structures
#Lists
numbers = [1, 2, 3, 4]
fruits = ["Apple", "Banana", "Cherry"]

combined_list = [1, "Apple", True]

# Accessing lists elements by indexing
# print(numbers[2])
# print(fruits[0])
# print(combined_list[1])
# print(fruits[-1])

fruits.append("orange")
fruits.insert(1,"grape")

# print(fruits)

fruits.remove("Banana") # remove at a specific index

# print(fruits)

del fruits[0] #remove a specific element

fruits.pop() # remove from last index

# print(fruits)

# slicing list
sliced_fruits = fruits[1:3]
# print(sliced_fruits)


#Tuples
colors = ("red", "green", "blue")
single_item = ("glass",)

# print(colors[0])
# print(colors[-1])

#Dictionaries

student = {"name": "Alice", "age": 25, "grade": "A"}
# print(student)
# print(student["name"])

# add element to dictionary
student["subject"] = "Math"
# print(student)

# update age
student["age"] = 24


# del pairs in dictionary

del student["grade"]
# print(student)

student.pop("subject")
# print(student)


# iterate through dictionary
for key, value in student.items():
    print(key, value)


# create a set

numbers = {1, 2, 3 , 4}
empty_set = set()

# add and remove element from/to set
numbers.add(5)
print(numbers)

numbers.add(4)
print(numbers)

numbers.remove(2)

# set operations
set1 = {1,2,3}
set2 = {3,4,5}

print(set1 | set2) # union
print(set1 & set2) #intersection
print(set1 - set2) # differences


