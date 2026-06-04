"""
5. Label the program written in problem 4 with comments. 
"""

import os # Import statement to import required module.

path = "C:/Users/CodeWithShahzaib/Play Ground/PYTHON" # File Path to list Directories of.

list_of_file = os.listdir(path) # This line takes the path and return the list of it's items.
print(list_of_file)