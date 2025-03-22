import unittest
import math
from circle import Circle

class TestCircle(unittest.TestCase):
    def test_calculate_perimeter(self):
        # Test with positive radius
        circle = Circle(5)
        expected_perimeter = 2 * math.pi * 5
        self.assertAlmostEqual(circle.calculate_perimeter(), expected_perimeter)
        
        # Test with zero radius
        circle = Circle(0)
        self.assertAlmostEqual(circle.calculate_perimeter(), 0)
    
    def test_calculate_area(self):
        # Test with positive radius
        circle = Circle(5)
        expected_area = math.pi * 5**2
        self.assertAlmostEqual(circle.calculate_area(), expected_area)
        
        # Test with zero radius
        circle = Circle(0)
        self.assertAlmostEqual(circle.calculate_area(), 0)

if __name__ == '__main__':
    unittest.main()