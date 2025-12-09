import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from square import area, perimeter

class TestSquare(unittest.TestCase):
    """Тесты для модуля square.py"""
    
    # Тесты для функции area()
    def test_area_side_positive(self):
        """Тест площади с положительной стороной"""
        self.assertEqual(area(5), 25)
    
    def test_area_side_zero(self):
        """Тест площади с нулевой стороной"""
        self.assertEqual(area(0), 0)
    
    def test_area_side_fraction(self):
        """Тест площади с дробной стороной"""
        self.assertAlmostEqual(area(2.5), 6.25, places=2)
    
    def test_area_side_large(self):
        """Тест площади с большой стороной"""
        self.assertEqual(area(100), 10000)
    
    # Тесты для функции perimeter()
    def test_perimeter_side_positive(self):
        """Тест периметра с положительной стороной"""
        self.assertEqual(perimeter(5), 20)
    
    def test_perimeter_side_zero(self):
        """Тест периметра с нулевой стороной"""
        self.assertEqual(perimeter(0), 0)
    
    def test_perimeter_side_fraction(self):
        """Тест периметра с дробной стороной"""
        self.assertAlmostEqual(perimeter(3.5), 14.0, places=2)
    
    def test_perimeter_side_large(self):
        """Тест периметра с большой стороной"""
        self.assertEqual(perimeter(75), 300)

if __name__ == '__main__':
    unittest.main()