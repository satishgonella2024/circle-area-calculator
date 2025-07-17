Here is the Python code to validate the area calculation function:

import math

def calculate_area(shape, *args):
    """
    Calculates the area of a given shape.

    Args:
        shape (str): The shape to calculate the area for.
        *args: Variable length argument list containing the necessary parameters for the shape.

    Returns:
        float: The calculated area.
    """
    if shape == "circle":
        radius, = args
        return math.pi * radius ** 2
    elif shape == "rectangle":
        length, width = args
        return length * width
    elif shape == "triangle":
        base, height = args
        return 0.5 * base * height
    else:
        raise ValueError(f"Unsupported shape: {shape}")

# Test the function with different inputs
print(calculate_area("circle", 5))  # Output: 78.53981633974483
print(calculate_area("rectangle", 4, 6))  # Output: 24.0
print(calculate_area("triangle", 3, 4))  # Output: 6.0
print(calculate_area("square", 5, 5))  # Raises ValueError: Unsupported shape: square