class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        longest_substring = 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            longest_substring = max(longest_substring, r-l+1)

        return longest_substring
