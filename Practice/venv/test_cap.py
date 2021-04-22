import unittest
import cap


class TesCap(unittest.TestCase):

    def test_one_word(self):
        text = "pyhton"
        result = cap.cap_text(text)
        self.assertEqual(result,"Python")


    def test_multiple_words(self):
        text = "monty python"
        result = cap.cap_text(text)
        self.assertEqual(result,"Monty Python")