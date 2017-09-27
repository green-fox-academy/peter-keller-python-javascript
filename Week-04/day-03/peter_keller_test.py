import unittest
from peter_keller_work import Tasks

test_method = Tasks()

class AppleTest(unittest.TestCase):
    def test_get_apple(self):
        self.assertEqual(test_method.get_apple(), "apple")


class SumElements(unittest.TestCase):
    def test_sum_of_elements(self):
        self.assertEqual(test_method.sum_of_elements([12, 1]), 13)


if __name__ == "__main__":
    unittest.main()


#class AnagramTest(unittest.TestCase):
#    def test_anagram(self):
#        self.assertEqual()


#if __name__ == "__main__":
#    unittest.main()