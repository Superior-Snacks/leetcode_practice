class Solution(object):
    def generate(self, numRows):
        prev = [1]
        curr = []
        if numRows == 1:
            return [1]
        elif numRows == 2:
            return [1,1]
        for i in range(3,numRows):
            #rows
            #for j in len(prev):
            print(i)


sol=Solution()
print(sol.generate(1))  
# Expected: [[1]]

print(sol.generate(2))  
# Expected: [[1], [1,1]]

print(sol.generate(5))  
# Expected: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

print(sol.generate(6))  
# Expected: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1]]

print(sol.generate(10))  
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