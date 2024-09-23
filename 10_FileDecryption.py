# Predefined encryption dictionary
encryption_dict = {
    'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '!', 'c': '$',
    'D': '&', 'd': '*', 'E': '(', 'e': ')', 'F': '-', 'f': '+',
    'G': '=', 'g': '>', 'H': '<', 'h': '[', 'I': ']', 'i': '{',
    'J': '}', 'j': '^', 'K': '~', 'k': '/', 'L': '|', 'l': '?',
    'M': ';', 'm': ':', 'N': '_', 'n': ',', 'O': '.', 'o': '"',
    'P': "'", 'p': '`', 'Q': '1', 'q': '2', 'R': '3', 'r': '4',
    'S': '5', 's': '6', 'T': '7', 't': '8', 'U': '0', 'u': 'z',
    'V': 'x', 'v': 'y', 'W': 'w', 'w': 'v', 'X': 'u', 'x': 't',
    'Y': 's', 'y': 'r', 'Z': 'q', 'z': 'p', ' ': '_'
}

# Invert the dictionary to create the decryption dictionary
decryption_dict = {v: k for k, v in encryption_dict.items()}

# Open the encrypted file and read its contents
with open('e:/AdvancedPython/AdvPython/mydictionaries/encrypted.txt', 'r') as infile:
    encrypted_content = infile.read()

# Decrypt the content using the decryption dictionary
# Leave characters that are not in the dictionary (punctuation) unchanged
decrypted_content = ''.join([decryption_dict.get(char, char) for char in encrypted_content])

# Display the decrypted content
print("Decrypted content:\n")
print(decrypted_content)

# Compare to the original file to verify decryption
with open('e:/AdvancedPython/AdvPython/mydictionaries/info_security.txt', 'r') as original_file:
    original_content = original_file.read()


