import unittest

from website import extract_title

class TestDelimiter(unittest.TestCase):
    def test_extr_title_correct(self):
        md = """
# Hello there
This is a test text
Hello again
        """
        title = extract_title(md)
        self.assertEqual(title, 'Hello there')
    
    def test_extr_title_correct_middle(self):
        md = """
My title is underneath
# Hello there
This is a test text
Hello again
        """
        title = extract_title(md)
        self.assertEqual(title, 'Hello there')
    
    def test_extr_title_fail(self):
        md = """
Hello there
There is no title
This is a test text
Hello again
        """
        with self.assertRaises(Exception):
            extract_title(md)

if __name__ == "__main__":
    unittest.main()