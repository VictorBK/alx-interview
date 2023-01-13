#!/usr/bin/python3
"""
Minimum Operations Task
"""

def minOperations(n):
    pasted_chars = 1 #No of characters in the file
    clipboard = 0 #No of Hs coped
    counter = 0 #Operations Counter

    while pasted_chars < n:
        if clipboard == 0:
            clipboard = pasted_chars
            counter += 1

        if pasted_chars == 1:
            pasted_chars += clipboard
            counter += 1
            continue
        
        remaining = n - pasted_chars
        if remaining < clipboard:
            return 0

        if remaining % pasted_chars != 0:
            pasted_chars += clipboard
            counter += 1
        else:
            clipboard = pasted_chars
            pasted_chars += clipboard
            counter += 2

    if pasted_chars == n:
        return counter
    else:
        return 0
