def isValid(s):
    r = ["(", "[", "{"]
    m = {")":"(", "]":"[", "}":"{"}
    l = [")", "]", "}"]
    # find first right side
    #go back, remove checked
    while True:
        print(s)
        if s:
            for i in range(len(s)):
                if s[i] in l: #find right
                    k = s[i]
                    print(k)
                    j = r[i-1]
                    print(j)
                    print("#find right")
                    if m[k] == j: # check if close
                        s = s[:i-1] + s[i:] #remove valid and conitnue
                        print("#remove valid and conitnue")
                        print(f"string is {s}")
                        break
                    else: # if not valid string bad
                        print("if not valid string bad")
                        return False
                else:
                    print("na not it")
        else: #if no left means valid string
            print("#if no left means valid string")
            return True
print("result ", isValid("()"))
print("result ", isValid("()[]{}"))
print("result ", isValid("(]"))
print("result ", isValid("([])"))


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