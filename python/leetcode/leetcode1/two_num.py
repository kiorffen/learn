#! /usr/bin/env python

import os
import sys

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: list[int]
        :type target: int
        :rtype: list[int]
        """

        ret = []
        dict = {}
        for i in range(0, len(nums)):
            dict[nums[i]] = i
        for i in range(0, len(nums)):
            other = target - nums[i]
            if dict.has_key(other) and dict[other] != i:
                ret.append(i)
                ret.append(dict[other])
                return ret

        return []

if __name__ == "__main__":
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 22
    ret = s.twoSum(nums, target)
    for i in range(0, len(ret)):
        print ret[i]

