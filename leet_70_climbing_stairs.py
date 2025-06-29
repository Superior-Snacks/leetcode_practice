def climbStairs(n):
    count = 0
    f0 = 0
    f1 = 1
    fnow = None
    while count < n:
        count += 1
        fnow = f1 + f0
        f0 = f1
        f1 = fnow
    if fnow:
        return fnow
    else:
        return "ERROR INVALID NUMBER"


print("n = 0:", climbStairs(0), "expected ERROR")
print("n = 1:", climbStairs(1), "expected 1")
print("n = 2:", climbStairs(2), "expected 2")
print("n = 3:", climbStairs(3), "expected 3")
print("n = 4:", climbStairs(4), "expected 5")
print("n = 5:", climbStairs(5), "expected 8")
print("n = 10:", climbStairs(10), "expected 89")
print("n = 20:", climbStairs(20), "expected 10946")
print("n = 30:", climbStairs(30), "expected 1346269")
print("n = 45:", climbStairs(45), "expected 1836311903")
"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 
Constraints:
1 <= n <= 45
"""