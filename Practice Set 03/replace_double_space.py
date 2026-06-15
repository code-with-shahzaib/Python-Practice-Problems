"""
4. Replace the double space from problem 3 with single spaces.
"""

sentence = input("Enter a Sentence: ")

index_of_double_space = sentence.find("  ")
replaced_str = sentence.replace("  ", " ")

print(f"The Replaced String is following:\n{replaced_str}")