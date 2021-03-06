---
layout: post
title: 417 - Pacific Atlantic Water Flow
date: 2018-02-28
tags:
- Leetcode
categories:
- Matrix
author: Jason
---
**Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges. Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower. Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.**


```python
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        if not matrix:
            return []

        ret, p_queue, a_queue = [], [], []
        m, n = len(matrix), len(matrix[0])
        p_visited = [[False] * n for _ in xrange(m)]
        a_visited = [[False] * n for _ in xrange(m)]
        for i in xrange(m):
            p_queue.append([i, 0])
            a_queue.append([i, n - 1])
            p_visited[i][0] = a_visited[i][n - 1] = True
        for j in xrange(n):
            p_queue.append([0, j])
            a_queue.append([m - 1, j])
            p_visited[0][j] = a_visited[m - 1][j] = True

        self.bfs(matrix, p_queue, p_visited)
        self.bfs(matrix, a_queue, a_visited)
        for i in xrange(m):
            for j in xrange(n):
                if p_visited[i][j] and a_visited[i][j]:
                    ret.append([i, j])
        return ret

    def bfs(self, matrix, queue, visited):
        idx = [-1, 1, 0, 0]
        idy = [0, 0, 1, -1]
        while queue:
            i, j = queue.pop(0)
            for k in xrange(4):
                new_i, new_j = i + idx[k], j + idy[k]
                if new_i >= 0 and new_i < len(matrix) and new_j >= 0 and new_j < len(matrix[0]) and not visited[new_i][new_j] and matrix[i][j] <= matrix[new_i][new_j]:
                    visited[new_i][new_j] = True
                    queue.append([new_i, new_j])
```
