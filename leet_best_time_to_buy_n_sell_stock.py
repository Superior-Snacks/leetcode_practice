class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        

sol = Solution()
print(sol.maxProfit([1]), "expected:", 0)
print(sol.maxProfit([1,2]), "expected:", 1)
print(sol.maxProfit([2,1]), "expected:", 0)
print(sol.maxProfit([2,2,2]), "expected:", 0)
print(sol.maxProfit([3,1,4]), "expected:", 3)
print(sol.maxProfit([5,2,7,1,4]), "expected:", 5)
print(sol.maxProfit([9,8,7,3,10]), "expected:", 7)
print(sol.maxProfit([1,10,2,9,3,8]), "expected:", 9)
print(sol.maxProfit([10,1,10]), "expected:", 9)
print(sol.maxProfit([2,4,1,7]), "expected:", 6)
print(sol.maxProfit([8,1,2,4,6,3]), "expected:", 5)
print(sol.maxProfit([0,0,0,0]), "expected:", 0)
print(sol.maxProfit([0,2,0,2]), "expected:", 2)
print(sol.maxProfit([2,1,2,1,0,1,2]), "expected:", 2)
print(sol.maxProfit([10000,0,9999]), "expected:", 9999)
print(sol.maxProfit([3,3,5,0,0,3,1,4]), "expected:", 4)
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""