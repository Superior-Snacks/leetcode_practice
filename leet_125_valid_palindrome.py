class Solution(object):
    def isPalindrome(self, s):
        s = s.replace(" ", "")
        print(s)
        count = 0
        r = 0
        l = -1
        while count != len(s):

        for i in range(len(s) // 2):
            print(f"front: {s[i]}")
            print(f"back: {s[-i]}")
            if s[i].isalpha():
                print(True)

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"), "expected:", True)
print(sol.isPalindrome("race a car"), "expected:", False)
print(sol.isPalindrome(" "), "expected:", True)
print(sol.isPalindrome("No lemon, no melon"), "expected:", True)
print(sol.isPalindrome("12321"), "expected:", True)
print(sol.isPalindrome("123ab321"), "expected:", False)
print(sol.isPalindrome("!!!"), "expected:", True)
print(sol.isPalindrome("a."), "expected:", True)

"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""