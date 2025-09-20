class Solution(object):
    def hammingWeight(self, n):
        return (bin(n).count('1'))
        
sol = Solution()
print(sol.hammingWeight(11), "expected 3")          # 1011 → 3 ones
print(sol.hammingWeight(128), "expected 1")         # 10000000 → 1 one
print(sol.hammingWeight(2147483645), "expected 30") # large number with 30 ones
print(sol.hammingWeight(1), "expected 1")           # edge case: smallest input
print(sol.hammingWeight(2**31 - 1), "expected 31")  # all bits set except sign
"""
Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).
Example 1:
Input: n = 11
Output: 3
Explanation:
The input binary string 1011 has a total of three set bits.

Example 2:
Input: n = 128
Output: 1
Explanation:
The input binary string 10000000 has a total of one set bit.

Example 3:
Input: n = 2147483645
Output: 30
Explanation:
The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

Constraints:
1 <= n <= 231 - 1

Follow up: If this function is called many times, how would you optimize it?
"""