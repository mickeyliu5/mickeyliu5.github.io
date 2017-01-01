---
layout: post
title: Burst Balloons
date: 2015-11-29 20:36:44.000000000 -05:00
type: post
published: true
status: publish
categories:
- Brain teaser
- Dynamic Programming
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468764528;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:542;}i:1;a:1:{s:2:"id";i:2059;}i:2;a:1:{s:2:"id";i:443;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.<br />
Find the maximum coins you can collect by bursting the balloons wisely.</em></strong></p>
<p><a href="https://leetcode.com/discuss/72216/share-some-analysis-and-explanations">read more</a></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    public int maxCoins(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        
        int[] ballons = new int[nums.length + 2];
        int len = 1;
        for (int num : nums) {
            if (num > 0) {
                ballons[len++] = num;
            }
        }
        ballons[0] = ballons[len++] = 1;
        int[][] coins = new int[len][len];        
        for (int k = 3; k <= len; k++) {//there are at least three balloons
            for (int left = 0; left + k - 1 < len; left ++) {
                int right = left + k - 1;
                for (int i = left + 1; i < right; i ++) {
                    coins[left][right] = Math.max(coins[left][right], ballons[left] * ballons[i] * ballons[right] + coins[left][i] + coins[i][right]);
                }
            }
        }
        return coins[0][len - 1];
    }
}
</pre>
<p>[/expand]</p>