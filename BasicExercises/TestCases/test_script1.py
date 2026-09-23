import unittest
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from Scripts import script1

class TestScript(unittest.TestCase):
    def test_square(self):
        self.assertEqual(script1.square(3), 9)
        self.assertEqual(script1.square(-4), 16)

    def test_cube(self):
        self.assertEqual(script1.cube(3), 27)
        self.assertEqual(script1.cube(-2), -8)

    def test_devide(self):
        self.assertEqual(script1.devide(10, 2), 5)
        self.assertEqual(script1.devide(9, 3), 3)
        with self.assertRaises(ZeroDivisionError):
            script1.devide(10, 0)

if __name__ == "__main__":
    unittest.main()