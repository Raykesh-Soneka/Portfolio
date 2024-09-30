
def caesar_cipher(text, shift, charset):
    result = ""
    Complexity=3
    Roue=3
    Roue2=5
    n=100

    for char in text:
        if char in charset:  # Check if character is in the custom charset
            idx = charset.index(char)
            new_idx = (idx + shift) % len(charset)
            if Complexity>=1:
                if shift>=0:
                    shift +=Roue  #Add Complexity 1
                    if Complexity>=2 and shift%2==0:shift +=Roue2  #Add Complexity 2
                else:
                    shift -=Roue
                    if Complexity>=2 and shift%2==0:shift -=Roue2  #Add Complexity 2
            if Complexity>=3 and shift%3==0: #Add Complexity 3
                shift=-shift
                if shift>=0:shift -=n
                else:shift +=n
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
text = "Hello, World! 123Aza)"+custom_charset
shift = 3
charset_Choisi=utf8_charset
encrypted_text = caesar_cipher(text, shift, charset_Choisi)
print(f"\033[36mOriginal  text: {text}\033[0m")
print(f"Encrypted text: {encrypted_text}")

decrypted_text = caesar_cipher(encrypted_text, -shift, charset_Choisi)
print(f"\033[32mDecrypted text: {decrypted_text}\033[0m")

# print(custom_charset)
# print(ascii_extended)
# print(utf8_charset)
# print(len(custom_charset))  #72
# print(len(ascii_extended))  #256
# print(len(utf8_charset))    #1114112   > 1 million

f = open("utf8_charset.txt", "w")
f.write('[')
for i in utf8_charset:
    f.write("'");f.write(i);f.write("' ,");
f.write(']')
f.close()
print("écrit")
