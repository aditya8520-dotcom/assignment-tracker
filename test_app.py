
import unittest
from app import add_assignment

class TestApp(unittest.TestCase):

    def test_add(self):
        result = add_assignment("Python Lab")
        self.assertIn("Python Lab", result)

if __name__ == "__main__":
    unittest.main()
