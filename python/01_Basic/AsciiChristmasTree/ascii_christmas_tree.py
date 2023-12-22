#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Define the colors using ANSI escape sequences
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BROWN = '\033[0;33m'
    RESET = '\033[0m'


# Define the parameters for the tree
stars = 1
width = 15
tree = 3

# Generate the tree with colors
for i in range(width):
    if i == 0:
        print((' ' * (width - i)) + (Colors.YELLOW + '^' * stars + Colors.RESET))
    elif i % 3 == 0:
        print((' ' * (width - i)) + (
                    Colors.YELLOW + '$' + Colors.GREEN + ('*' * (stars - 2)) + Colors.YELLOW + '$' + Colors.RESET))
    else:
        print((' ' * (width - i)) + (Colors.GREEN + '*' * stars + Colors.RESET))
    stars += 2

# Add the tree trunk with dark brown color
for i in range(tree):
    print((' ' * (width - 2)) + (Colors.BROWN + '|' * 5 + Colors.RESET))

# Add the Christmas greeting in red
greeting = "Merry Christmas!"
centered_greeting = Colors.RED + greeting.center(width * 2 + 1) + Colors.RESET
print(centered_greeting)
