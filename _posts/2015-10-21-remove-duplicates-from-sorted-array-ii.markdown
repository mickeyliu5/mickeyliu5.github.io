---
layout: post
title: 80 - Remove Duplicates from Sorted Array II
date: 2015-10-21 02:24:13.000000000 -04:00
tags:
- Leetcode
categories:
- Integer
author: Jason
---
**Follow up for "Remove Duplicates": What if duplicates are allowed at most twice?**


``` java
public class Solution {
    /**
     * @param A: a array of integers
     * @return : return an integer
     */
    public int removeDuplicates(int[] nums) {
        // write your code here
        if (nums == null || nums.length == 0) return 0;

        int flag = 0, index = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i-1] && flag == 0) {
                index ++;
                flag = 1;
            } else if (nums[i] != nums[i-1]) {
                flag = 0;
                index ++;
            }
            nums[index] = nums[i];
        }
        return index + 1;
    }
}
```

``` java
public class Solution {
    //hash map solution
    public int removeDuplicates(int[] nums) {
        int j = 0;
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for ( int i = 0; i < nums.length; i++ ) {
            if(map.containsKey(nums[i])) {
                map.put(nums[i], map.get(nums[i]) + 1);
                if ( map.get(nums[i]) > 2 ) { continue; }
            }else{
                map.put(nums[i], 1);
            }
            nums[j++] = nums[i];
        }
        return j;
    }
```

``` python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        seen = False
        index = 0
        for i in xrange(1, len(nums)):
            if nums[i] == nums[i - 1]:
                if not seen:
                    index += 1
                    seen = True
            else:
                seen = False
                index += 1
            nums[index] = nums[i]
        return index + 1
```
