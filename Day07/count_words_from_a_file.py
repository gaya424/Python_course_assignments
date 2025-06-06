import os

def read_words_from_file(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    return text.split()

def count_words(words):
    word_counts = {}
    for word in words:
        word_lower = word.lower()
        word_counts[word_lower] = word_counts.get(word_lower, 0) + 1
    return word_counts

def construct_output_path(input_path):
    dir_name, base_name = os.path.split(input_path)
    name, ext = os.path.splitext(base_name)
    new_name = f"{name}_counted{ext}"
    return os.path.join(dir_name, new_name)

def write_word_counts(word_counts, output_path):
    with open(output_path, 'w') as f:
        for word in sorted(word_counts):
            f.write(f"{word.ljust(14)}{word_counts[word]}\n")

def main():
    input_path = input("Enter the path to the input file: ").strip()
    
    try:
        words = read_words_from_file(input_path)
        word_counts = count_words(words)
        output_path = construct_output_path(input_path)
        write_word_counts(word_counts, output_path)
        print(f"Word counts saved to: {output_path}")
    except FileNotFoundError:
        print("Error: File not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
