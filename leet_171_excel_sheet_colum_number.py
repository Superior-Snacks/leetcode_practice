class Solution(object):
    def titleToNumber(self, columnTitle):
        title = columnTitle
        count = 0
        while title:
            m = len(title) - 1
            print(m)
            print(26^m)
            char = title[0]
            print(f"number {char} is ascci {ord(char) - ord("A") + 1}")
            count += (ord(char) - ord("A") + 1) * (26 ** m)
            title = title[1:]
        return count
"""
        num = columnNumber
        result = ""
        while num != 0:
            num -= 1
            rem = (num % 26)
            result = chr(ord("A") + rem) + result
            num = num // 26
        return result
"""

sol = Solution()
print(sol.titleToNumber("A"), "expected:", 1)
print(sol.titleToNumber("AB"), "expected:", 28)
print(sol.titleToNumber("ZY"), "expected:", 701)
print(sol.titleToNumber("Z"), "expected:", 26)
print(sol.titleToNumber("AA"), "expected:", 27)
print(sol.titleToNumber("AZ"), "expected:", 52)
print(sol.titleToNumber("BA"), "expected:", 53)
print(sol.titleToNumber("FXSHRXW"), "expected:", 2147483647)  # upper bound
"""
Given a string columnTitle that represents the column title as appears in an Excel sheet, 
return its corresponding column number.

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
Input: columnTitle = "A"
Output: 1

Example 2:
Input: columnTitle = "AB"
Output: 28

Example 3:
Input: columnTitle = "ZY"
Output: 701
 
Constraints:
1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"]
"""