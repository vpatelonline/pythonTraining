import unittest
import cap

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Python')

    def test_multi_word(self):
        text = 'python ninja'
        result = cap.cap_text(text)
        self.assertEqual(result,'Python ninja')

    def test_word(self):
        text = 'python ninja'
        result = cap.title_text(text)
        self.assertEqual(result,'Python Ninja')

    def test_word_in_single_line(self):
        self.assertEqual(cap.title_text('python ninja'),'Python Ninja')
    
if __name__=='__main__':
    unittest.main()

