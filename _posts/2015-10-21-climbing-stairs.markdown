---
layout: post
title: 70 - Climbing Stairs
date: 2015-10-21 12:26:49.000000000 -04:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
**You are climbing a stair case. It takes n steps to reach to the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?**


``` java
public class Solution {
    /**
     * @param n: An integer
     * @return: An integer
     */
    public int climbStairs(int n) {
        //state: dp[i]
        //function: dp[i] = dp[i-1][i-2]
        //initialization dp[0] = 1, dp[1] = 1
        //answer: dp[n]
        int[] dp = new int[n+1];
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }
}
```

``` python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n in (1, 2):
            return n

        dp = [0, 1, 2]
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])

        return dp[-1]
```
