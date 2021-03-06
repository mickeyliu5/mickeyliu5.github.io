---
layout: post
title: Find the difference between two set
date: 2016-01-21 11:30:59.000000000 -05:00
tags:
- OA
categories:
- Array
author: Jason
---
**找出两个数组的差，比如A = [1,1,1,2,2,2], B = [2,2,3]，在A出现在B不出现的集合是[1,1,1,2]**


``` java
public class Solution {
    public static void main(String[] args) {
        List<Integer> A = new ArrayList<>(Arrays.asList(1,1,1,2,2,2));
        List<Integer> B = new ArrayList<>(Arrays.asList(2,2,3));
        System.out.println(findSubset(B, A));
        System.out.println(findSubset(A, B));
    }
    public static List<Integer> findSubset(List<Integer> A, List<Integer> B) {
        List<Integer> result = new ArrayList<>();
        if (A.size() == 0) return result;
        if (B.size() == 0) {
            result.addAll(A);
            return result;
        }
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int num : A) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        for (int num : B) {
            if (map.containsKey(num)) {
                map.put(num, map.get(num) - 1);
            }
        }
        for (int num : map.keySet()) {
            for (int i = 0; i < map.get(num); i++) {
                result.add(num);
            }
        }
        return result;
    }
}
```

``` python
class Solution(object):
    def findSubset(self, A, B):
        if not A:
            return []
        elif not B:
            return A

        counter = collections.Counter(A)
        for num in B:
            if num in counter:
                counter[num] -= 1
        ret = []
        for k, v in counter.iteritems():
            ret.extend([k] * v)
        return ret
```
