import os
from collections import defaultdict
from typing import Dict

codon_table_raw = {
    'Phe': ['TTT', 'TTC'],
    'Leu': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'Ile': ['ATT', 'ATC', 'ATA'],
    'Met': ['ATG'],
    'Val': ['GTT', 'GTC', 'GTA', 'GTG'],
    'Ser': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Pro': ['CCT', 'CCC', 'CCA', 'CCG'],
    'Thr': ['ACT', 'ACC', 'ACA', 'ACG'],
    'Ala': ['GCT', 'GCC', 'GCA', 'GCG'],
    'Tyr': ['TAT', 'TAC'],
    'His': ['CAT', 'CAC'],
    'Gln': ['CAA', 'CAG'],
    'Asn': ['AAT', 'AAC'],
    'Lys': ['AAA', 'AAG'],
    'Asp': ['GAT', 'GAC'],
    'Glu': ['GAA', 'GAG'],
    'Cys': ['TGT', 'TGC'],
    'Trp': ['TGG'],
    'Arg': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Gly': ['GGT', 'GGC', 'GGA', 'GGG'],
    'STOP': ['TAA', 'TAG', 'TGA']
}

# Reverse mapping: codon -> amino acid
codon_to_aa = {}
for aa, codons in codon_table_raw.items():
    for codon in codons:
        codon_to_aa[codon] = aa

def read_sequence_from_file(filepath):
    """
    Reads a DNA sequence from a .txt or .fasta file, removing headers and non-DNA characters.

    Args:
        filepath: Path to the DNA sequence file.

    Returns:
        A cleaned DNA sequence string.
    """
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    # Remove FASTA headers (lines starting with ">")
    sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))
    sequence = ''.join(filter(lambda x: x in 'ACGTacgt', sequence.upper()))
    return sequence


def count_amino_acids(sequence):
    """
    Counts occurrences of amino acids in a DNA sequence (ignoring STOP codons).

    Args:
        sequence: DNA sequence string.

    Returns:
        Dictionary mapping amino acid names to their counts.

    Example:
        >>> count_amino_acids('ATGCTT')
        {'Met': 1, 'Leu': 1}
    """ 
    aa_counts = defaultdict(int)
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        if len(codon) != 3:
            continue
        aa = codon_to_aa.get(codon)
        if aa and aa != 'STOP':
            aa_counts[aa] += 1
    return aa_counts


def main():
    filepath = input("Enter the path to the DNA sequence file: ").strip()
    if not os.path.isfile(filepath):
        print("File not found.")
        return

    sequence = read_sequence_from_file(filepath)
    if not sequence:
        print("No valid DNA sequence found.")
        return

    aa_counts = count_amino_acids(sequence)
    
    print("\nAmino Acid Counts:")
    for aa in sorted(aa_counts):
        print(f"{aa.ljust(10)}{aa_counts[aa]}")

if __name__ == '__main__':
    main()