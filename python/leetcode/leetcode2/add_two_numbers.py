#! /usr/bin/env python
# -*- coding:utf8 -*-

"""
   leetcode 2: Add Two Numbers
"""

import os
import sys
import time

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
        ll1 = []
        ll2 = []
        while (l1.next != None):
            ll1.append(l1.val)
            l1 = l1.next
        ll1.append(l1.val)
        while (l2.next != None):
            ll2.append(l2.val)
            l2 = l2.next
        ll2.append(l2.val)
        min_len = 0
        lt = []
        if len(ll1) >= len(ll2):
            min_len = len(ll2)
        else:
            min_len = len(ll1)
        incre_flag = 0
        for i in range(0, min_len):
            tmp_sum = ll1[i] + ll2[i] + incre_flag
            incre_flag = 0
            if tmp_sum < 10:
                lt.append(tmp_sum)
            else:
                incre_flag = 1
                lt.append(tmp_sum % 10)
        if min_len < len(ll1):
            for i in range(min_len, len(ll1)):
                tmp_sum = ll1[i] + incre_flag
                incre_flag = 0
                if tmp_sum < 10:
                    lt.append(tmp_sum)
                else:
                    incre_flag = 1
                    lt.append(tmp_sum % 10)
        else:
            for i in range(min_len, len(ll2)):
                tmp_sum = ll2[i] + incre_flag
                incre_flag = 0
                if tmp_sum < 10:
                    lt.append(tmp_sum)
                else:
                    incre_flag = 1
                    lt.append(tmp_sum % 10)
        if incre_flag == 1:
            lt.append(incre_flag)
        n = None
        for i in range(len(lt) - 1, -1, -1):
            ret_l = ListNode(0)
            ret_l.val = lt[i]
            if n != None:
                ret_l.next = n
            else:
                ret_l.next = None
            n = ret_l
        return ret_l


if __name__ == "__main__":
    n1 = ListNode(4)
    n2 = ListNode(5)
    n3 = ListNode(5)
    n4 = ListNode(5)
    n2.next = n1
    n3.next = n2
    n4.next = n3
    l1 = n2
    l2 = n4

    s = Solution()
    l3 = s.addTwoNumbers(l1, l2)
    while l3.next != None:
        sys.stdout.write("%s->" % (l3.val))
        l3 = l3.next
    sys.stdout.write("%s\n" % (l3.val))
