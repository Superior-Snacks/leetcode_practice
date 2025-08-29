class Solution(object):
    def generate(self, numRows):
        curr = []
        res = [[1]]
        if numRows == 1:
            return res
        for i in range(1, numRows):
            curr = [1]
            for j in range(1,len(res[-1])):
                curr.append(res[-1][j-1] + res[-1][j])
            curr.append(1)
            res.append(curr)
        return res

sol=Solution()
print(sol.generate(1), "done")  
# Expected: [[1]]

print(sol.generate(2), "done")  
# Expected: [[1], [1,1]]

print(sol.generate(5), "done")  
# Expected: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

print(sol.generate(6), "done")  
# Expected: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1]]

print(sol.generate(10), "done")  
# Expected last row = [1,9,36,84,126,126,84,36,9,1]
"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
"""