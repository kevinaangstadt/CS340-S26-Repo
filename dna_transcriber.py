def transcribe_dna(dna_string):
    """
    Transcribes a DNA string to RNA.

    The transcription process replaces Thymine ('T') with Uracil ('U').

    Args:
        dna_string (str): The DNA sequence.

    Returns:
        str: The corresponding RNA sequence.
    """
    return dna_string.upper().replace('T', 'U')