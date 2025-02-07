#!/usr/bin/env python3
"""
This script creates an indexable, mutable iterable named colours with at least four items. 
It also defines a function called firsts that returns the first letter of each item in a list. 
The function is then called with the colours list to verify its functionality.
Additionally, various list operations are performed.
"""

# Creating an indexable, mutable iterable named colours
colours = ["red", "blue", "green", "yellow"]

def firsts(lst):
    """
    This function takes a list as a parameter and returns a list of the first letters of each item in the list.
    
    :param lst: List of strings
    :return: List of first letters of each string in the input list
    """
    return [item[0] for item in lst]

# Call the function with colours and verify its functionality
print("First letters of each colour:", firsts(colours))

# Print the entire list
print("Colours list:", colours)

# Check the data type of colours
print("Type of colours:", type(colours))

# Check the data type of the output from firsts(colours)
print("Type of firsts(colours):", type(firsts(colours)))

# Check if "blue" is in the colours list
print("Is 'blue' in colours?:", "blue" in colours)

# Print the first element of colours
print("First colour:", colours[0])

# Print the last element of colours
print("Last colour:", colours[-1])

# Add a new colour to the list
colours.append("purple")
print("Colours after appending 'purple':", colours)

# Remove "green" from the list
colours.remove("green")
print("Colours after removing 'green':", colours)

# Sort colours alphabetically
colours.sort()
print("Colours after sorting:", colours)
