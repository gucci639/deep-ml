def find_treasure(start_x: float) -> float:
    """
    Find the x-coordinate where f(x) = x^4 - 3x^3 + 2 is minimized.

  Returns:
        float: The x-coordinate of the minimum point.
    """
    # Your code here
    x=start_x
    deriv=4*x**3-9*x**2
    learning_rate=0.09
    for i in range(10000):
        deriv=4*x**3-9*x**2
        x = x - learning_rate * deriv
    return x