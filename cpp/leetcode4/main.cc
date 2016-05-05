#include <cstdio>
#include <vector>
#include <algorithm>

using std::vector;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size();
        int n2 = nums2.size();
        int count = n1 + n2;
        if (count & 0x01) {
            return findKth(nums1, 0, n1, nums2, 0, n2, count/2 + 1);
        } else {
            return (findKth(nums1, 0, n1, nums2, 0, n2, count/2)
                + findKth(nums1, 0, n1, nums2, 0, n2, count/2 + 1)) / 2.0;
        }
    }
private:
    double findKth(vector<int>& nums1, int s1, int e1,
            vector<int>& nums2, int s2, int e2, int k) {
        int m = e1 - s1;
        int n = e2 - s2;
        if (m > n) {
            return findKth(nums2, s2, e2, nums1, s1, e1, k);
        }
        if (m == 0) {
            return nums2[s2 + k - 1];
        }
        if (k == 1) {
            return std::min(nums1[s1], nums2[s2]);
        }
        int pa = std::min(k/2, m);
        int pb = k - pa;
        if (nums1[s1 + pa - 1] < nums2[s2 + pb - 1]) {
            return findKth(nums1, s1 + pa, e1, nums2, s2, e2, k - pa);
        } else if (nums1[s1 + pa -1] > nums2[s2 + pb - 1]) {
            return findKth(nums1, s1, e1, nums2, s2 + pb, e2, k - pb);
        } else {
            return nums1[s1 + pa - 1];
        }
    }
};

int main()
{
    Solution s;
    vector<int> v1, v2;
    v1.clear();
    v2.clear();

    v1.push_back(2);
    // v1.push_back(3);
    // v1.push_back(5);
    // v1.push_back(7);
    // v1.push_back(9);
    
    // v2.push_back(2);
    // v2.push_back(4);
    // v2.push_back(6);
    // v2.push_back(8);
    // v2.push_back(10);

    double median = s.findMedianSortedArrays(v1, v2);

    printf("median:%.2f\n", median);

    return 0;
}
