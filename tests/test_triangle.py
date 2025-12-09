import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from triangle import area, perimeter

class TestTriangle(unittest.TestCase):
    """Тесты для модуля triangle.py"""
    
    # Тесты для функции area()
    def test_area_base_height_positive(self):
        """Тест площади с положительными основанием и высотой"""
        self.assertEqual(area(10, 5), 25)
    
    def test_area_base_height_zero(self):
        """Тест площади с нулевыми значениями"""
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(area(0, 0), 0)
    
    def test_area_base_height_fraction(self):
        """Тест площади с дробными значениями"""
        self.assertAlmostEqual(area(5.5, 4.4), 12.1, places=2)
    
    def test_area_base_height_large(self):
        """Тест площади с большими значениями"""
        self.assertEqual(area(100, 50), 2500)
    
    def test_area_base_height_one(self):
        """Тест площади со значением 1"""
        self.assertEqual(area(1, 1), 0.5)
    
    def test_area_base_height_equal(self):
        """Тест площади с равными значениями"""
        self.assertEqual(area(6, 6), 18)
    
    # Тесты для функции perimeter()
    def test_perimeter_sides_positive(self):
        """Тест периметра с положительными сторонами"""
        self.assertEqual(perimeter(3, 4, 5), 12)
    
    def test_perimeter_sides_zero(self):
        """Тест периметра с нулевыми сторонами"""
        self.assertEqual(perimeter(0, 0, 0), 0)
        self.assertEqual(perimeter(0, 4, 5), 9)
        self.assertEqual(perimeter(3, 0, 5), 8)
        self.assertEqual(perimeter(3, 4, 0), 7)
    
    def test_perimeter_sides_fraction(self):
        """Тест периметра с дробными сторонами"""
        self.assertAlmostEqual(perimeter(2.5, 3.5, 4.5), 10.5, places=2)
    
    def test_perimeter_sides_large(self):
        """Тест периметра с большими сторонами"""
        self.assertEqual(perimeter(100, 150, 200), 450)
    
    def test_perimeter_sides_equal(self):
        """Тест периметра равностороннего треугольника"""
        self.assertEqual(perimeter(5, 5, 5), 15)
    
    def test_perimeter_sides_one(self):
        """Тест периметра со сторонами 1"""
        self.assertEqual(perimeter(1, 1, 1), 3)

if __name__ == '__main__':
    unittest.main()