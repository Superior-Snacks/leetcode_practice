def addBinary(a, b):
    count = 0
    i = len(a) - 1
    j = len(b) - 1
    



"""
how to calc binary, start from back if 1 + 1 leave 0 carry over 1 elif 1 + 0 leave 1 carry over none
a	b	in	sum	out
0	0	0	0	0
0	1	0	1	0
1	0	0	1	0
1	1	0	0	1
1	1	1	1	1
1	0	1	0	1
0	1	1	0	1
0	0	1	1	0
"""
print(addBinary("0", "0"), "=> 0")
print(addBinary("1", "0"), "=> 1")
print(addBinary("1", "1"), "=> 10")
print(addBinary("101", "1"), "=> 110")
print(addBinary("11", "1"), "=> 100")
print(addBinary("1", "111"), "=> 1000")
print(addBinary("1111", "1"), "=> 10000")
print(addBinary("111", "111"), "=> 1110")
a = "1" * 10  # 10 ones
b = "1"
# 1111111111 + 1 = 10000000000 (a 1 followed by ten 0s)
print(addBinary(a, b), "=> 10000000000")
print(addBinary("000", "000"), "=> 0")
print(addBinary("0001", "0010"), "=> 11")
"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
 
Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""