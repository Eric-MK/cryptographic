import base64

# The hex string to decode and then encode to Base64
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Decode the hex string into bytes
decoded_bytes = bytes.fromhex(hex_string)

# Encode the decoded bytes to Base64
base64_encoded = base64.b64encode(decoded_bytes)

# Convert the Base64 encoded bytes to a string
base64_encoded_string = base64_encoded.decode('utf-8')

# Print the Base64 encoded string
print(base64_encoded_string)
