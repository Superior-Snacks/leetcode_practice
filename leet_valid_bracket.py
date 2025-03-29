def isValid(s):
    r = ["(", "[", "{"]
    l = {")":"(", "]":"[", "}":"{"}
    # find first right side
    #go back, remove checked
    while True:
        print(s)
        if s:
            for i in range(len(s)):
                if s[i] in l: #find right
                    k = l[s[i]]
                    j = r[i-1]
                    print("#find right")
                    if k == j: # check if close
                        s = s[:j,k:] #remove valid and conitnue
                        print("#remove valid and conitnue")
                        print(f"string is {s}")
                        break
                    else: # if not valid string bad
                        False
                        print("if not valid string bad")
                else:
                    print("na not it")
        else: #if no left means valid string
            print("#if no left means valid string")
            True
print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([])"))


"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true"""