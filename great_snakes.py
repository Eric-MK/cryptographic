#!/usr/bin/env python3

import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

print("Here is your flag:")
print("".join(chr(o ^ 0x32) for o in ords))

""" Here's the fun part! This line takes each of those numbers in the ords list and does a special operation on them. It's like translating the secret code into regular words.

The for o in ords part means "for each number in the list called ords."
The o ^ 0x32 part takes each number and does something called a "bitwise XOR" with another number (0x32, which is 50 in regular numbers). It's like doing a secret math operation.
The chr() part changes the number you got from the XOR into a letter. It's like converting a number back into its letter.
The "".join() part is like putting all those letters together to form words.

So, when you run the script, it takes those numbers, does the secret math, and reveals the hidden message, just like deciphering a code. The message is your "flag," a special reward for figuring out the code! """