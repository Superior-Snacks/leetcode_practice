def mySqrt(x):
    if x < 2:
        return x
    l = 0
    r = x
    while l <= r:
        m = (l + r) // 2
        if (m * m >= x) and (m * m <= x + 1):
            return int(m) - 1
        elif m * m < x:
            l = m + 1
        else:
            r = m - 1
    return r

            

print("input 0:", mySqrt(0), "expected answer 0")               # edge: lowest input
print("input 1:", mySqrt(1), "expected answer 1")               # edge: small input
print("input 2:", mySqrt(2), "expected answer 1")               # non-perfect square
print("input 3:", mySqrt(3), "expected answer 1")               # non-perfect square
print("input 4:", mySqrt(4), "expected answer 2")               # perfect square
print("input 8:", mySqrt(8), "expected answer 2")               # in-between square
print("input 9:", mySqrt(9), "expected answer 3")               # perfect square
print("input 10:", mySqrt(10), "expected answer 3")             # non-perfect square
print("input 15:", mySqrt(15), "expected answer 3")             # edge between 3 and 4
print("input 16:", mySqrt(16), "expected answer 4")             # perfect square
print("input 2147395600:", mySqrt(2147395600), "expected answer 46340") # large perfect square
print("input 2147483647:", mySqrt(2147483647), "expected answer 46340") # max 32-bit int, not a perfect square
"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1
"""