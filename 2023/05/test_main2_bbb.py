import unittest
from main2 import Segment

class TestMyClass(unittest.TestCase):
    def setUp(self):
        """Set up resources before each test."""
        self.obj = Segment(start=10, end=20)

    def test_increment(self):
        """Test the increment method."""
        self.obj.increment()
        self.assertEqual(self.obj.value, 6)

    def test_multiply(self):
        """Test the multiply method."""
        result = self.obj.multiply(3)
        self.assertEqual(result, 15)

    def test_initial_value(self):
        """Test the initial value."""
        self.assertEqual(self.obj.value, 5)

if __name__ == "__main__":
    unittest.main()
