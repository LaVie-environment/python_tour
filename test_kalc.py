import unittest
import kalc

class TestKalc(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = kalc.kalc_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = kalc.kalc_text(text)
        self.assertEqual(result, 'Monty python')

if __name__== '__main__':
    unittest.main()