import math

def area(r):
    """
    Вычисляет площадь круга.
    
    Args:
        r (float): Радиус круга
        
    Returns:
        float: Площадь круга
    """
    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет длину окружности.
    
    Args:
        r (float): Радиус круга
        
    Returns:
        float: Длина окружности
    """
    return 2 * math.pi * r