#! /usr/bin/env python
# -*- coding:gbk -*-

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        s_list = []
        if numRows == 1 or len(s) == 0:
            return s
        for i in range(0, numRows):
            for index in range(i, len(s), 2*(numRows - 1)):
                s_list.append(s[index])
                if i != 0 and i != numRows - 1:
                    if index + 2*(numRows - i - 1) < len(s):
                        s_list.append(s[index + 2*(numRows - i - 1)])

        ret_str = ''.join(s_list)

        return ret_str

if __name__ == "__main__":
    s = Solution()
    print s.convert("PAYPALISHIRING", 3)
    #print s.convert("", 3)
    #print s.convert("PAYPALISHIRING", 1)
