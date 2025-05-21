import re

def extract_valid_dna_segments(sequence):
    return sorted(re.findall(r'[ACTG]+', sequence.upper()), key=len, reverse=True)

if __name__ == '__main__':
    sequence = input("Please type in a sequence: ")
    valid_segments = extract_valid_dna_segments(sequence)
    print(valid_segments)
