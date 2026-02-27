import unittest
from dna_transcriber import transcribe_dna

class TestDNATranscriber(unittest.TestCase):
    def test_uppercase_transcription(self):
        self.assertEqual(transcribe_dna("GATTACA"), "GAUUACA")

    def test_no_t(self):
        self.assertEqual(transcribe_dna("CGCA"), "CGCA")

    def test_lowercase_input(self):
        self.assertEqual(transcribe_dna("gattaca"), "GAUUACA")

if __name__ == '__main__':
    unittest.main()
