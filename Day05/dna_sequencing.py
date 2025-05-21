import sys
import re

def extract_valid_dna_segments(sequence):
    return sorted(re.findall(r'[ACTG]+', sequence), key=len, reverse=True)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python dna_sequencing.py <SEQUENCE>")
        sys.exit(1)

    sequence = sys.argv[1].upper()
    valid_segments = extract_valid_dna_segments(sequence)
    print(valid_segments)
