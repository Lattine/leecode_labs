# -------------------------------------------------------------------------------------------------------------
# 4. Median of Two Sorted Arrays
# -------------------------------------------------------------------------------------------------------------
# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]


# The median is (2 + 3)/2 = 2.5
# ------------------------------------------------------------------------------------------------------------
from typing import List

class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = sorted((nums1, nums2), key=len)
        m, n = len(a), len(b)
        after = (m + n - 1) // 2
        lo, hi = 0, m
        while lo < hi:
            i = (lo + hi) // 2
            if after - i - 1 < 0 or a[i] >= b[after - i - 1]:
                hi = i
            else:
                lo = i + 1
        i = lo
        nextfew = sorted(a[i:i + 2] + b[after - i:after - i + 2])
        return (nextfew[0] + nextfew[1 - (m + n) % 2]) / 2


if __name__ == "__main__":
    A = [1, 3]
    B = [2]
    s = Solution()
    print(s.findMedianSortedArrays(A, B))