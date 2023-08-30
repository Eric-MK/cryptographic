# The given string
label = "label"

# XOR each character with the integer 13 and convert to a new string
new_string = ''.join(chr(ord(c) ^ 13) for c in label)

# Format the flag
flag = f"crypto{{{new_string}}}"

# Print the flag
print(flag)
