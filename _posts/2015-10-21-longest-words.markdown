---
layout: post
title: Longest Words
date: 2015-10-21 12:59:11.000000000 -04:00
tags:
- Leetcode
categories:
- Brain Teaser
author: Jason
---
<p><strong><em>Given a dictionary, find all of the longest words in the dictionary.</em></strong></p>


``` java
class Solution {
    public ArrayList<String> longestWords(String[] dictionary) {
        ArrayList<String> result = new ArrayList<String>();
        if (dictionary == null) return result;
        
        int maxLen = 0;
        for (String str : dictionary) {
            if (str.length() > maxLen) {
                result.clear();
                result.add(str);
                maxLen = str.length();
            } else if (str.length() == maxLen) {
                result.add(str);
            }
        }
        return result;
    }
};
```
