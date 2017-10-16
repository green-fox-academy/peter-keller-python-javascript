import unittest
from peter_keller_work import Tasks

test_method = Tasks()

#class AppleTest(unittest.TestCase):
#    def test_get_apple(self):
#        self.assertEqual(test_method.get_apple(), "apple")

#class SumElements(unittest.TestCase):
    def test_sum_of_elements(self):
        self.assertEqual(test_method.sum_of_elements([12, 1]), 13)

class AnagramTest(unittest.TestCase):
    def test_anagram(self):
        self.assertTrue(test_method.anagram("hitlerwoman", "motherinlaw"))

#class CountLetterTest(unittest.TestCase):
    def test_count_letters(self):
        self.assertEqual(test_method.count_letters("aaacc"),{"a" : 3, "c" : 2})

#class FibonacciTest(unittest.TestCase):
#    def test_fibonacci(self):
#        self.assertEqual(test_method.fibonacci(10),55)


if __name__ == "__main__":
    unittest.main(exit=True)
