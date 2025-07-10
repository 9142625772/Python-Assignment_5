'''ASSIGNMENT 5:
Module 6: Data Structures and Strings in Python
Task 1: Create a Dictionary of Student Marks
'''
# Create a dictionary with student names and marks
students = {
    "Alice": 85,
    "Emma": 92,
    "Michael": 78,
    "Sophia": 95,
    "William": 88
}

# Ask the user to input a student's name
name = input("Enter a student's name: ")

# Retrieve and display the corresponding marks
if name in students:
    print("{}'s marks:{}".format(name,students[name]))
else:
    print("student not found")
    
#Task 2: Demonstrate List Slicing
#1. Creates a list of numbers from 1 to 10.
list=[1,2,3,4,5,6,7,8,9,10]
print("Original list:",list)
#2. Extracts the first five elements from the list.
a=list[0:5]
print("Extracted first five elements:",a)
#3. Reverses these extracted elements.
a.reverse()
print("Reversed extracted elements:",a)




