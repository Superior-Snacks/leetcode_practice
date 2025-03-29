def isValid(s):
    r = ["(", "[", "{"]
    l = {")":"(", "]":"[", "}":"{"}
    # find first right side
    #go back, remove checked
    while True:
        if s:
            for i in range(len(s)):
                if s[i] == l: #find right
                    k = l[s[i]]
                    j = r[i-1]
                    if k == j: # check if close
                        s = s[:j,k:] #remove valid and conitnue
                        break
                    else: # if not valid string bad
                        False
        else: #if no left means valid string
            True
print(isValid())
print(isValid())
print(isValid())
print(isValid())