---
layout: post
title: 3Sum Smaller
date: 2015-10-31 10:24:04.000000000 -04:00
type: post
published: true
status: publish
categories:
- Subarray
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1464270101;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:125;}i:1;a:1:{s:2:"id";i:127;}i:2;a:1:{s:2:"id";i:123;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 &lt;= i &lt; j &lt; k &lt; n that satisfy the condition nums[i] + nums[j] + nums[k] &lt; target.<br />
For example, given nums = [-2, 0, 1, 3], and target = 2.<br />
Return 2. Because there are two triplets which sums are less than 2:</em></strong></p>
<p>[expand title = "O(n^2)"]</p>
<pre>
public class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        if (nums == null || nums.length == 0) return 0;
        
        Arrays.sort(nums);
        int result = 0;
        for (int i = 0; i + 2 < num.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int lo = i + 1, hi = nums.length - 1;
            while (lo < hi) {
                if (lo > i + 1 && nums[lo] == nums[lo - 1]) {
                    lo++;
                    continue;
                }
                if (hi < nums.length - 1 && nums[hi] == nums[hi + 1]) {
                    hi--;
                    continue;
                }
                int sum = nums[i] + nums[lo] + nums[hi];
                if (sum < target) {
                    result += hi - lo;
                    lo ++;
                } else {
                    hi --;
                }
            }
        }
        return result;
    }
}
</pre>
<p>[/expand]<br />
[expand title="O(n^3)"]</p>
<pre>
public class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        if (nums == null || nums.length == 0) return 0;
        
        int count = 0;
        for (int i = 0; i < nums.length - 2; i++) {
            for (int j = i + 1; j < nums.length - 1; j++) {
                for (int k = j + 1; k < nums.length; k++) {
                    if (nums[i] + nums[j] + nums[k] < target) {
                        count ++;
                    }
                }
            }
        }
        return count;
    }
}
</pre>
<p>[/expand]</p>