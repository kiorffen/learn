#! /usr/bin/env python
# -*- coding: gbk -*-

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negtive = 1 if x < 0 else 0
        new_x = str(abs(x))[::-1]
        while new_x.startswith('0'):
            new_x = new_x[1:]
        if new_x == "":
            return 0
        new_x = int(new_x)
        return new_x if not is_negtive and new_x < 1<<31 \
        else -new_x if  is_negtive and new_x <= 1<<31 \
        else 0

if __name__ == "__main__":
    s = Solution()
    print s.reverse(-123)
                                         
