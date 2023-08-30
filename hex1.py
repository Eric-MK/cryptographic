# The hex string we want to decode
hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

# Convert the hex string to bytes
decoded_bytes = bytes.fromhex(hex_string)

# Decode the bytes using UTF-8 encoding to get the message
decoded_message = decoded_bytes.decode('utf-8')

# Print the decoded message (the flag)
print(decoded_message)
