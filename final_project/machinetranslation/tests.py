
import unittest
from translator import english_to_french, french_to_english

class testTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(french_to_english("None"), '')


    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(english_to_french("None"), '')

if __name__ == "__main__":
    unittest.main()
