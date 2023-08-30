# Given encrypted hexadecimal value
encrypted_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

# Convert the encrypted hexadecimal value to bytes
encrypted_bytes = bytes.fromhex(encrypted_hex)

# Loop through all possible single-byte keys and XOR them with the encrypted bytes
for key in range(256):
    decrypted_bytes = bytes([byte ^ key for byte in encrypted_bytes])
    
    # Convert the decrypted bytes to a string and check if it contains "crypto{"
    decrypted_text = decrypted_bytes.decode('utf-8', errors='ignore')
    if "crypto{" in decrypted_text:
        print(f"Key: {key:02X} - Decrypted Flag: {decrypted_text}")
        break
