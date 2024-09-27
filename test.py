import unittest
from tire_classification import Type, classify_tire

# Equivalent class 
# traction_index : above 110, below 110 and above 90, below 90 and above 40 or below 40
# circonference : below 26 and above 26 
# pressure : below 36 or above 36
# Satisfy the critieria for WRECT 

class TestFunction(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(Type.INVALID, classify_tire(110, 9, 36))

    def test_case_2(self):
        self.assertEqual(Type.INVALID, classify_tire(100, 37, 25))

    def test_case_3(self):
        self.assertEqual(Type.SUMMER, classify_tire(89, 37, 36))

    def test_case_4(self):
        self.assertEqual(Type.INVALID, classify_tire(37, 37, 36))