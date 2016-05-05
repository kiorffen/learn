#! /usr/bin/env python
# -*- coding:utf8 -*-

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        j = 0
        sub_str = ""
        max_len = 1
        sub_begin = 0
        for i in range(0, len(s)):
            index = sub_str.find(s[i])
            print "index: ", index
            print "sub_str: ", sub_str
            if index == -1:
                sub_str = s[j:i+1]
                tmp_len = i - j + 1
                if (max_len < tmp_len):
                    max_len = tmp_len
                    print "max_len: ", max_len
            else:
                j = j + index + 1
                sub_str = s[j:i+1]

        return max_len

if __name__ == "__main__":
    s = Solution()
    s1 = "bbtablud"
    sub_len = s.lengthOfLongestSubstring(s1)
    print sub_len
