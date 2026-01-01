#calculate_area

def calculate_area(length, width):
    """Calculate the area of a rectangle.

    Args:
        length (float or itn): The length of the rectangle.
        width (float or int): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * width

area1 = calculate_area(5, 10)
area2 = calculate_area(7.5, 3.2)    
print("Area 1:", area1)
print("Area 2:", area2)
