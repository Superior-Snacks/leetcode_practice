class Solution(object):
    def reverseBits(self, n):
        result = 0
        bit = n & 1
        print(bit)
        for i in range(32):
            bit = n & 1
            result = (result << 1) | bit 
            n >>= 1
            print(result)
        return f"old: {n} new: {result}"     

sol = Solution()
print(sol.reverseBits(43261596), "expected 964176192")
print(sol.reverseBits(2147483644), "expected 1073741822")
print(sol.reverseBits(0), "expected 0")
print(sol.reverseBits(1), "expected 2147483648")   # lowest bit becomes highest
print(sol.reverseBits(2), "expected 1073741824")   # second lowest bit to second highest
print(sol.reverseBits(4294967295), "expected 4294967295") # all 1s stay same
"""
Reverse bits of a given 32 bits signed integer.

Example 1:
Input: n = 43261596
Output: 964176192
Explanation:
Integer	Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000

Example 2:
Input: n = 2147483644
Output: 1073741822
Explanation:
Integer	Binary
2147483644	01111111111111111111111111111100
1073741822	00111111111111111111111111111110
 
Constraints:
0 <= n <= 231 - 2
n is even.

Follow up: If this function is called many times, how would you optimize it?
"""