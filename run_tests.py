#!/usr/bin/env python3
"""
Скрипт для запуска всех тестов geometric_lib
"""

import unittest
import sys
import os

def run_all_tests():
    """Запускает все тесты"""
    # Находим все тестовые файлы
    test_dir = os.path.join(os.path.dirname(__file__), 'tests')
    loader = unittest.TestLoader()
    
    # Загружаем тесты
    suite = loader.discover(test_dir, pattern='test_*.py')
    
    # Запускаем тесты
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Выводим статистику
    print("\n" + "="*50)
    print("СТАТИСТИКА ТЕСТИРОВАНИЯ")
    print("="*50)
    print(f"Всего тестов: {result.testsRun}")
    print(f"Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Провалено: {len(result.failures)}")
    print(f"Ошибок: {len(result.errors)}")
    
    # Возвращаем код завершения
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    print("Запуск тестов geometric_lib...")
    print("="*50)
    sys.exit(run_all_tests())