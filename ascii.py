# Define the list of numbers representing ASCII codes
integer_array = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

# Create an empty string to store the flag
flag = ''

# Loop through each number in the list
for i in integer_array:
    # Convert the number to its corresponding ASCII character and add it to the flag
    flag += chr(i)

# Print the decoded flag
print(flag)
