class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_str = ""

        for c in s.lower():
            if c.isalnum():
                new_str += c

        left_ptr = 0
        right_ptr = len(new_str)-1

        while right_ptr > left_ptr:
            if new_str[left_ptr] != new_str[right_ptr]:
                return False
            left_ptr = left_ptr+1
            right_ptr = right_ptr-1

        return True
