"""
Given a list of digits, return the smallest number
that could be formed from these digits, using the
digits only once (ignore duplicates).

Only positive integers will be passed to the function (> 0 ),
no negatives or zeros.

"""

def min_value(digits):
    digits = list(set(digits))
    digits.sort()
    return int(''.join([str(i) for i in digits]))

min_value([4,5,6,7,7,6])