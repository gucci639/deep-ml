import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    def derivative(coeffs):
        return [coeffs[i]*(len(coeffs)-i-1) for i in range(0, len(coeffs)-1)]
    def multiplication(coeffs1, coeffs2):
        result = [0.0] *(len(coeffs1)+(len(coeffs2)) - 1)
        for i in range(len(coeffs1)):
            for j in range(len(coeffs2)):
                result[i+j] += coeffs1[i]*coeffs2[j]
        return result
    def countx(coeffs, x):
        return sum([coeffs[i]*x**(len(coeffs)-i-1) for i in range(len(coeffs))])
    return (countx(derivative(g_coeffs), x)*countx(h_coeffs, x) - countx(g_coeffs, x )*countx(derivative(h_coeffs), x)) / countx(h_coeffs, x)**2
