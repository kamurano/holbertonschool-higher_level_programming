#!/usr/bin/python3
"""Module containing append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """Function adding string to a file"""

    # Reading the file and keeping it line-by-line
    with open(filename, 'r') as file:
        text = file.readlines()

    # Inserting new_string to each line after search_string
    new_text = []
    for line in range(len(text)):
        new_text.append(text[line])

        # Checking if search_string is in current line
        if search_string in text[line]:
            new_text.append(new_string)

    # Writing the new text to the file
    with open(filename, "w") as file:
        file.writelines(new_text)
