def lengthOfLastWord(s):
    count = 0
    for i in range(len(s) - 1, -1, -1):
        if allowed(s[i]):
            count += 1
        elif not allowed(s[i]) and count == 0:
            continue
        elif not allowed(s[i]):
            return count
    return count


def allowed(x):
    
    if x.lower() in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
        return True
    else:
        return False


print(lengthOfLastWord("Hello World"))  # Expected: 5
print(lengthOfLastWord("   fly me   to   the moon  "))  # Expected: 4
print(lengthOfLastWord("Hello"))  # Expected: 5
print(lengthOfLastWord("world        "))  # Expected: 5
print(lengthOfLastWord("a   b    c   d   e   "))  # Expected: 1
print(lengthOfLastWord("solo     "))  # Expected: 4
print(lengthOfLastWord("yes"))  # Expected: 3
print(lengthOfLastWord("word before    final"))  # Expected: 5
print(lengthOfLastWord("           word"))  # Expected: 4
s = "a " * 9999 + "end"
print(lengthOfLastWord(s))  # Expected: 3
print(lengthOfLastWord("     "))  # Behavior undefined per constraints, should never occur.
print(lengthOfLastWord("MiXeDCaSe"))  # Expected: 9