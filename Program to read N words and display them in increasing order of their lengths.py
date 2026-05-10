
# Program to read N words and display them in increasing order of their lengths
# Input number of words
n = int(input('Enter number of words:'))
# Read words
words = []
for i in range(n):
    word = input('Enter word ')
    words.append(word)
# Sort words by their length
    words.sort(key=len)
# Display words with lenghths
print("\n Words in increasing order of length:")
for word in words:
        print(f"{word} (Length: {len(word)})")
