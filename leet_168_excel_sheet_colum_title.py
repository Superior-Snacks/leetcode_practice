class Solution(object):
    def convertToTitle(self, columnNumber):
        num = columnNumber
        result = ""
        while num != 0:
            print(num)
            num = ((num - 1) / 26)
            rem = num % 26
            result += chr(ord("A") + rem)
            print(result)
            print(num)
        return result
        

sol = Solution()
print(sol.convertToTitle(1), "expected: A")
print(sol.convertToTitle(26), "expected: Z")
print(sol.convertToTitle(27), "expected: AA")
print(sol.convertToTitle(28), "expected: AB")
print(sol.convertToTitle(52), "expected: AZ")
print(sol.convertToTitle(701), "expected: ZY")
print(sol.convertToTitle(702), "expected: ZZ")
print(sol.convertToTitle(703), "expected: AAA")
"""
Given an integer columnNumber, 
return its corresponding column title as it appears in an Excel sheet.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Example 1:
Input: columnNumber = 1
Output: "A"

Example 2:
Input: columnNumber = 28
Output: "AB"

Example 3:
Input: columnNumber = 701
Output: "ZY"
 
Constraints:
1 <= columnNumber <= 231 - 1
"""