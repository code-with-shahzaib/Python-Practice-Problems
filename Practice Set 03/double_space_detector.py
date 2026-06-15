"""
3. Write a program to detect double space in a string.
"""

sentence = input("Enter a Sentence: ")

index_of_double_space = sentence.find("  ")
print(f"Double Space Found in Sentence at {index_of_double_space}th Index.")

