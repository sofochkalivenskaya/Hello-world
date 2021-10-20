Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:54:25) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from decimal import Decimal, getcontext
from math import ceil, factorial


def pi(precision: int) ->> str:
     if not isinstance(precision, int):
         raiseTypeError("Undefined for non-integers")
     elifprecision < 1:
         raiseValueError("Undefined for non-natural numbers")

    getcontext().prec = precision
    num_iterations = ceil(precision / 14)
    constant_term = 426880 * Decimal(10005).sqrt()
    exponential_term = 1
    linear_term = 13591409
    partial_sum = Decimal(linear_term)
    for k in range(1, num_iterations):
        multinomial_term = factorial(6 * k) // (factorial(3 * k) * factorial(k))
        linear_term += 545140134
        exponential_term *= -262537412640768000
        partial_sum += Decimal(multinomial_term * linear_term) / exponential_tem
    return str(constant_term / partial_sum)[:-1]


    if __name__ == "__main__":
    n = 50
    print(f"The first {n} digits of pi is: {pi(n)}")
