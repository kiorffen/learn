#! /usr/bin/env python
# -*- coding:gbk -*-

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        digital_dict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        if str == "":
            return 0
        while str.startswith(' '):
            str = str[1:]
        if str == "":
            return 0
        is_negtive = 0
        if str[0] == '-':
            is_negtive = 1
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]
        if str == "":
            return 0
        while str.startswith('0'):
            str = str[1:]
        if str == "":
            return 0
        ret = 0
        for i in range(len(str)):
            if not digital_dict.has_key(str[i]):
                break
            ret = ret*10 + digital_dict[str[i]]
            if not is_negtive and ret >= (1<<31):
                return (1<<31) - 1
            elif is_negtive and ret > (1<<31):
                return -(1<<31)
        if not is_negtive:
            return ret
        else:
            return -ret

if __name__ == "__main__":
    s = Solution()
    print s.myAtoi('12345')
    print s.myAtoi('-12345')
    print s.myAtoi('   -12345')
    print s.myAtoi('   -')
    print s.myAtoi('   +')
    #print s.myAtoi('   12345')
    #print s.myAtoi('   1234 5')
    print s.myAtoi('   1234a5')
    #print s.myAtoi('1234599999999999999')
    #print s.myAtoi('-1234599999999999999')
