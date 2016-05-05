#! /usr/bin/env python
# -*- coding -*-

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        max_len = 0
        index = 0
        if length == 0 or length == 1:
            return s
        for i in range(0, length):
            begin = i
            end = i
            while end < length - 1 and s[end] == s[end+1]:
                end = end + 1
            while end < length - 1 and begin > 0 and s[begin - 1] == s[end + 1]:
                begin = begin - 1
                end = end + 1
            if max_len < end - begin + 1:
                max_len = end - begin + 1
                index = begin

        return s[index:index + max_len]

if __name__ == "__main__":
    s = Solution();
    #print s.longestPalindrome('aabcbcbaacbeeeeeeeeebc')
    print s.longestPalindrome('eabcb')

                                         
