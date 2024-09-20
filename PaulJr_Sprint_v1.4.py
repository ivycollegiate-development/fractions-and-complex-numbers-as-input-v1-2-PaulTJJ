from fractions import Fraction

a = Fraction(input('Enter a fraction (e.g., 3/4): '))
print(a)
try:
    a = Fraction(input('Enter a fraction: '))
    print(a)
except ZeroDivisionError:
    print('Invalid fraction: denominator cannot be zero')
