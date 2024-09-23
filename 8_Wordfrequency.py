# Open the file and read the contents
with open('sometext.txt', 'r') as infile:
    text = infile.read()

# Create an empty dictionary for word frequencies
word_freq = {}

# Split the text into words and count frequencies
for k in text.split():
    k = k.lower().strip('.,!?;:')
    word_freq[k] = word_freq.get(k, 0) + 1

# Display the word frequencies
for k, v in word_freq.items():
    print(f"{k}: {v}")
