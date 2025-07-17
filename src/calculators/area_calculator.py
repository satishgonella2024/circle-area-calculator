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