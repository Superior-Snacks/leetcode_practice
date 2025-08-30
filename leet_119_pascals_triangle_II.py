class Solution(object):
    def getRow(self, rowIndex):
        curr = []
        prev = [1]
        for i in range(len(rowIndex)):
            if rowIndex == 0:
                return prev
            
        


sol = Solution()
print(sol.getRow(0))   # [1]
print(sol.getRow(1))   # [1, 1]
print(sol.getRow(2))   # [1, 2, 1]
print(sol.getRow(3))   # [1, 3, 3, 1]
print(sol.getRow(4))   # [1, 4, 6, 4, 1]
print(sol.getRow(5))   # [1, 5, 10, 10, 5, 1]
print(sol.getRow(10))  # [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]

"""Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
 

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?"""