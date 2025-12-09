import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from rectangle import area, perimeter

class TestRectangle(unittest.TestCase):
    """Тесты для модуля rectangle.py"""
    
    # Тесты для функции area()
    def test_area_sides_positive(self):
        """Тест площади с положительными сторонами"""
        self.assertEqual(area(5, 4), 20)
    
    def test_area_sides_zero(self):
        """Тест площади с нулевыми сторонами"""
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(5, 0), 0)
        self.assertEqual(area(0, 0), 0)
    
    def test_area_sides_fraction(self):
        """Тест площади с дробными сторонами"""
        self.assertAlmostEqual(area(2.5, 3.5), 8.75, places=2)
    
    def test_area_sides_large(self):
        """Тест площади с большими сторонами"""
        self.assertEqual(area(100, 50), 5000)
    
    # Тесты для функции perimeter()
    def test_perimeter_sides_positive(self):
        """Тест периметра с положительными сторонами"""
        self.assertEqual(perimeter(5, 4), 18)
    
    def test_perimeter_sides_zero(self):
        """Тест периметра с нулевыми сторонами"""
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(5, 0), 10)
        self.assertEqual(perimeter(0, 0), 0)
    
    def test_perimeter_sides_fraction(self):
        """Тест периметра с дробными сторонами"""
        self.assertAlmostEqual(perimeter(2.5, 3.5), 12.0, places=2)
    
    def test_perimeter_sides_large(self):
        """Тест периметра с большими сторонами"""
        self.assertEqual(perimeter(100, 200), 600)

if __name__ == '__main__':
    unittest.main()