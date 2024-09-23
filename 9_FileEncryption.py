import string

# Predefined encryption dictionary without affecting punctuation
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

# Open the original file (info_security.txt) and read its contents
with open('e:/AdvancedPython/AdvPython/mydictionaries/info_security.txt', 'r') as infile:
    content = infile.read()

# Encrypt the content using the predefined dictionary
# Only encrypt letters and spaces, leave punctuation unchanged
encrypted_content = ''.join([encryption_dict.get(char, char) for char in content])

# Write the encrypted content to a new file (encrypted.txt)
with open('e:/AdvancedPython/AdvPython/mydictionaries/encrypted.txt', 'w') as outfile:
    outfile.write(encrypted_content)

print("Encryption complete. Encrypted content written to 'encrypted.txt'.")
