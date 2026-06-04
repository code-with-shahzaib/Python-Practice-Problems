"""
Write a python program to print the contents of a directory using the os module.
Search online for the function which does that.
"""

import os 

path = "C:/Users/Mujadad Computer/OneDrive/Desktop/PYTHON"

list_of_file = os.listdir(path)
print(list_of_file)
