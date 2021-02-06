import unittest 
import _cap

class TestCap(unittest.TestCase):

	def test_one_word(self):
		text = 'java'
		result = _cap.cap_text(text)
		self.assertEqual(result,'Java')

	def test_multiple_words(self):
		text = 'java kotlin'
		result = _cap.cap_text(text)
		self.assertEqual(result,'Java Kotlin')

if __name__ == '__main__':
	unittest.main()