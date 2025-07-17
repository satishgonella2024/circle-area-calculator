from src.area_calculator import calculate_area

print(calculate_area("circle", 5))  # Output: 78.53981633974483
print(calculate_area("rectangle", 4, 6))  # Output: 24.0
print(calculate_area("triangle", 3, 4))  # Output: 6.0
print(calculate_area("square", 5, 5))  # Raises ValueError: Unsupported shape: square