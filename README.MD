# FILEPATH: 
# .

    """
    Returns the sum of all even numbers in the given list of integers.

    Args:
    numbers (list): A list of integers.

    Returns:
    int: The sum of all even numbers in the list.
    """
    return sum(num for num in numbers if num % 2 == 0)
