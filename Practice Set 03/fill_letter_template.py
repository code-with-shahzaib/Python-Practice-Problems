"""2. Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
"""

name = input("Enter Your Name: ")
date = input("Enter Date: ")


# This Version is the uses print function and f-string
print(f'''
Dear <|{name.capitalize()}|>,
You are selected!
<|{date}|>
''')


# This Version is uses Escape Sequence Characters and f-strings
letter = f'''Dear <|{name}|>,\nYou are selected!\n<|{date}|>'''
print(letter)