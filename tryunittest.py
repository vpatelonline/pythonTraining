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
        self.assertEqual(result,'Python Ninja')   #This case will fail due to Ninja so fix this use ninja

    def test_word(self):
        text = 'python ninja'
        result = cap.title_text(text)
        self.assertEqual(result,'Python Ninja')

    
if __name__=='__main__':
    unittest.main()

