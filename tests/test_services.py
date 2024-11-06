import unittest
from services.mutant_service import MutantService
from unittest.mock import patch

class TestMutantService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.service = MutantService()

    def test_detect_mutant_sequence(self):
        dna_mutant = [
            "ATGCGA",
            "CAGTGC",
            "TTATGT",
            "AGAAGG",
            "CCCCTA",
            "TCACTG"
        ]
        self.assertTrue(self.service.mutant_status(dna_mutant))

    
    @patch.object(MutantService, 'store_sequence', return_value=True)
    def test_store_dna_sequence(self, mock_store_sequence):
        sequence = ["ATGCGA", "CAGTGA", "TTATGA", "AGAAGG", "CCCCTT", "TCACTG"]
        self.assertTrue(self.service.store_sequence(sequence, mutant_status=True))
        mock_store_sequence.assert_called_once_with(sequence, mutant_status=True)

    @patch.object(MutantService, 'store_sequence', return_value=False)
    def test_store_duplicate_sequence(self, mock_store_sequence):
        sequence = ["ATGCGA", "CAGTGA", "TTATGA", "AGAAGG", "CCCCTT", "TCACTG"]
        self.assertFalse(self.service.store_sequence(sequence, mutant_status=True))
        mock_store_sequence.assert_called_once_with(sequence, mutant_status=True)

if __name__ == "__main__":
    unittest.main()
