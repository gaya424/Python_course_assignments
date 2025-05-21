input_str = input("Enter words separated by commas: ")

# Split and strip whitespace
words = [word.strip() for word in input_str.split(",")]

# Count word occurrences
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

for word, count in word_counts.items():
    print(f"{word:<12} {count}")
