---
layout: post
title: 153 - Find Minimum in Rotated Sorted Array
date: 2015-10-21 02:30:03.000000000 -04:00
tags:
- Leetcode
categories:
- Binary Search Tree
author: Jason
---
**Suppose a sorted array is rotated at some pivot unknown to you beforehand. (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2). Find the minimum element.**


``` java
public class Solution {
    public int findMin(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int lo = 0, hi = nums.length - 1;
        while (lo < hi) {//not <=
            int mid = (lo + hi) / 2;
            if (nums[mid] < nums[hi]) {//右边有序,且右边的值都大于nums[mid]
                hi = mid;
            } else {//左边有序,且左边的值都大于nums[mid]
                lo = mid + 1;
            }
        }
        return nums[lo];
    }
}
```

``` python
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) / 2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        return nums[lo]
```
