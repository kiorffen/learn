#! /usr/bin/env python
# -*- coding:utf8 -*-

class Solution(object):

    def findKth(self, nums1, nums2, k):
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findKth(nums2, nums1, k)
        if m == 0:
            return nums2[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        p1 = min(k/2, m)
        p2 = k - p1
        if nums1[p1 - 1] < nums2[p2 - 1]:
            return self.findKth(nums1[p1:m], nums2, k - p1)
        elif nums2[p2 - 1] < nums1[p1 - 1]:
            return self.findKth(nums1, nums2[p2:n], k - p2)
        else:
            return nums1[p1 - 1]

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        count = len(nums1) + len(nums2)
        if count & 0x1:
            return self.findKth(nums1, nums2, count/2 + 1)
        else:
            return (self.findKth(nums1, nums2, count/2) + self.findKth(nums1, nums2, count/2 + 1))*1.0/2

if __name__ == "__main__":
    s = Solution()
    print s.findMedianSortedArrays([2], [])
    print s.findMedianSortedArrays([], [2])
    print s.findMedianSortedArrays([1, 3, 5, 7], [2, 4, 6, 8, 10])
    print s.findMedianSortedArrays([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
