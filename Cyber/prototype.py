
def caesar_cipher(text, shift, charset):
    result = ""

    for char in text:
        if char in charset:  # Check if character is in the custom charset
            idx = charset.index(char)  # Get the index of the character in the charset
            new_idx = (idx + shift) % len(charset)  # Calculate the new index with the shift
            result += charset[new_idx]  # Get the character at the new index
        else:
            result += char  # Characters not in the charset remain unchanged

    return result

# Charset
custom_charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
ascii_extended = [chr(i) for i in range(256)]  # Generate the extended ASCII character set
import sys
utf8_charset = [chr(i) for i in range(sys.maxunicode + 1)]  # Generate the UTF-8 character set


# Example usage:
text = "Hello, World! 123Aza)"
shift = 3
charset_Choisi=utf8_charset
encrypted_text = caesar_cipher(text, shift, charset_Choisi)
print(f"Encrypted text: {encrypted_text}")

decrypted_text = caesar_cipher(encrypted_text, -shift, charset_Choisi)
print(f"Decrypted text: {decrypted_text}")

# print(custom_charset)
# print(ascii_extended)
# print(utf8_charset)

