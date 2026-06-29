
def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    """
    Compute the derivative of the product of two polynomials.
    
    Args:
        f_coeffs: Coefficients of polynomial f, where f_coeffs[i] is the coefficient of x^i
        g_coeffs: Coefficients of polynomial g, where g_coeffs[i] is the coefficient of x^i
    
    Returns:
        Coefficients of (f*g)' as a list of floats rounded to 4 decimal places
    """
    # Your code here
    output=[float()]*(len(g_coeffs)-1)*len(f_coeffs)
    if len(f_coeffs)==1 or len(g_coeffs)==1:
        output=[0.0]
    for a in range(len(f_coeffs)):
        for b in range(len(g_coeffs)):
            if a+b>=1:
                output[a+b-1]+=f_coeffs[a]*g_coeffs[b]*(a+b)
    return output