from amino_acid_counter import count_amino_acids

def test_simple_sequence():
    """
    Test simple codon translation.

    >>> dict(count_amino_acids("ATGCTT"))
    {'Met': 1, 'Leu': 1}
    """
    assert count_amino_acids("ATGCTT") == {'Met': 1, 'Leu': 1}

def test_mixed_case_sequence():
    """
    Test that lowercase input is handled correctly.

    >>> dict(count_amino_acids("atgctt"))
    {'Met': 1, 'Leu': 1}
    """
    assert count_amino_acids("atgctt") == {'Met': 1, 'Leu': 1}

def test_stop_codons():
    """
    Test that STOP codons are excluded.

    >>> dict(count_amino_acids("TAA"))
    {}
    """
    assert count_amino_acids("TAA") == {}  # STOP codon only

def test_incomplete_codon():
    """
    Test that an incomplete codon is ignored.

    >>> dict(count_amino_acids("ATGA"))
    {'Met': 1}
    """
    assert count_amino_acids("ATGA") == {'Met': 1}  # Ignore trailing A

def test_multiple_codons():
    """
    Test multiple codons translation.

    >>> dict(count_amino_acids("ATGCTGCGT"))
    {'Met': 1, 'Leu': 1, 'Arg': 1}
    """
    assert count_amino_acids("ATGCTGCGT") == {'Met': 1, 'Leu': 1, 'Arg': 1}

def test_unknown_codon():
    """
    Test that unknown codons (not in table) are ignored.

    >>> dict(count_amino_acids("NNN"))
    {}
    """
    assert count_amino_acids("NNN") == {}
