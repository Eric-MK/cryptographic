# Given encrypted hexadecimal value
encrypted_msg = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

# Convert the encrypted hexadecimal value to bytes
encrypted_msg = bytes.fromhex(encrypted_msg)

# Flag format to check against (in bytes)
flag_format = b"crypto{"

# Calculate the XOR key based on the difference between the encrypted message and the flag format
key = [o1 ^ o2 for (o1, o2) in zip(encrypted_msg, flag_format)] + [ord("y")]

# Initialize an empty list to store the decrypted flag bytes
flag = []

# Get the length of the key
key_len = len(key)

# Loop through each byte in the encrypted message
for i in range(len(encrypted_msg)):
    # XOR the byte from the encrypted message with the corresponding key byte
    flag.append(encrypted_msg[i] ^ key[i % key_len])

# Convert the decrypted integer values back to a string
flag = "".join(chr(o) for o in flag)

# Print the decrypted flag
print("Flag:")
print(flag)
