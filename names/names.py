import time
from binary_search_tree import BinarySearchTree

# Reads duplicates names
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

binary = BinarySearchTree('names')
#  It adds all of the names from name 1 to binary tree
for names in names_1:
    binary.insert(names)
# It checks names in names 2 to see if it exists in the tree
for name in names_2:
    # if it does it appends it to the dulicates array 
    if binary.contains(name):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
