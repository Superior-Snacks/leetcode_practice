def strStr(haystack, needle):
    if not needle:
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i] == needle[0]:
            if haystack[i:i+len(needle)] == needle:
                return i
    return -1



print("no.1", strStr("sadbutsad", "sad"))          # Expected: 0 (first "sad" starts at index 0)
print("no.2", strStr("leetcode", "leeto"))         # Expected: -1 ("leeto" not in "leetcode")
print("no.3", strStr("hello", "ll"))               # Expected: 2 ("ll" starts at index 2)
print("no.4", strStr("aaaaa", "bba"))              # Expected: -1 ("bba" not in "aaaaa")
print("no.5", strStr("aaaaa", "a"))                # Expected: 0 (first "a" starts at index 0)
print("no.6", strStr("mississippi", "issip"))      # Expected: 4 ("issip" starts at index 4)
print("no.7", strStr("a", "a"))                    # Expected: 0 (same character)
print("no.8", strStr("abc", ""))                   # Optional: could be 0 depending on constraints
print("no.9", strStr("", "a"))                     # Expected: -1 (cannot find anything in empty haystack)
print("no.10", strStr("abcabcabc", "cab"))         # Expected: 2 (first "cab" starts at index 2)
print("edge.2", strStr("exactmatch", "exactmatch"))  # Expected: "first", 0
print("edge.1", strStr("short", "longerneedle"))  # Expected: "failed", -1
print("edge.3", strStr("", ""))  # Expected: "first", 0