#!/usr/bin/env python3

class Solution:
    remain = 1
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if self.remain <= 0:
                    return False
                else:
                    self.remain -= 1
                    return self.validPalindrome(s[left:right]) or self.validPalindrome(s[left+1:right+1])

        return True
