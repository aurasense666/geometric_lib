import unittest
import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from circle import area, perimeter

class TestCircle(unittest.TestCase):
    """Тесты для модуля circle.py"""
    
    # Тесты для функции area()
    def test_area_radius_positive(self):
        """Тест площади с положительным радиусом"""
        self.assertAlmostEqual(area(5), math.pi * 25, places=5)
    
    def test_area_radius_zero(self):
        """Тест площади с нулевым радиусом"""
        self.assertEqual(area(0), 0)
    
    def test_area_radius_fraction(self):
        """Тест площади с дробным радиусом"""
        self.assertAlmostEqual(area(2.5), math.pi * 6.25, places=5)
    
    def test_area_radius_large(self):
        """Тест площади с большим радиусом"""
        self.assertAlmostEqual(area(100), math.pi * 10000, places=5)
    
    # Тесты для функции perimeter()
    def test_perimeter_radius_positive(self):
        """Тест периметра с положительным радиусом"""
        self.assertAlmostEqual(perimeter(5), 10 * math.pi, places=5)
    
    def test_perimeter_radius_zero(self):
        """Тест периметра с нулевым радиусом"""
        self.assertEqual(perimeter(0), 0)
    
    def test_perimeter_radius_fraction(self):
        """Тест периметра с дробным радиусом"""
        self.assertAlmostEqual(perimeter(3.5), 7 * math.pi, places=5)
    
    def test_perimeter_radius_large(self):
        """Тест периметра с большим радиусом"""
        self.assertAlmostEqual(perimeter(50), 100 * math.pi, places=5)

if __name__ == '__main__':
    unittest.main()