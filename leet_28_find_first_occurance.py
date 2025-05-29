def strStr(haystack, needle):
    for i in haystack:
        print(i)
        thread += i
        if thread == needle[:len(thread)]:






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