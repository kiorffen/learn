#! /usr/bin/env python
# -*- coding:utf8 -*-

"""
   leetcode 2: Add Two Numbers
"""

import os
import sys

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        min_len = 0
        lt = []
        if len(l1) >= len(l2):
            min_len = len(l2)
        else:
            min_len = len(l1)
        incre_flag = 0
        for i in range(0, min_len):
            tmp_sum = l1[i].val + l2[i].val + incre_flag
            incre_flag = 0
            if tmp_sum < 10:
                x = ListNode(tmp_sum)
                lt.append(x)
            else:
                incre_flag = 1
                x = ListNode(tmp_sum % 10)
                lt.append(x)
        if min_len < len(l1):
            for i in range(min_len, len(l1)):
                tmp_sum = l1[i].val + incre_flag
                incre_flag = 0
                if tmp_sum < 10:
                    x = ListNode(tmp_sum)
                    lt.append(x)
                else:
                    incre_flag = 1
                    x = ListNode(tmp_sum % 10)
                    lt.append(x)
        else:
            for i in range(min_len, len(l2)):
                tmp_sum = l2[i].val + incre_flag
                incre_flag = 0
                if tmp_sum < 10:
                    x = ListNode(tmp_sum)
                    lt.append(x)
                else:
                    incre_flag = 1
                    x = ListNode(tmp_sum % 10)
                    lt.append(x)
        if incre_flag == 1:
            x = ListNode(incre_flag)
            lt.append(x)
        return lt


if __name__ == "__main__":
    n1 = ListNode(2)
    n2 = ListNode(4)
    n3 = ListNode(3)
    n4 = ListNode(5)
    n5 = ListNode(6)
    n6 = ListNode(6)
    n7 = ListNode(9)
    l1 = [n1, n2, n3, n4, n7]
    l2 = [n4, n5, n6, n7]

    s = Solution()
    l3 = s.addTwoNumbers(l1, l2)
    if len(l3) >= 2:
        for i in range(0, len(l3) - 1):
            sys.stdout.write("%s->" % (l3[i].val))
    sys.stdout.write("%s\n" % (l3[len(l3) - 1].val))
