---
layout: post
title: Valid parentheses
date: 2015-10-21 03:35:31.000000000 -04:00
categories:
- Brain teaser
- Data Structure
author: Jason
---
<p><strong><em>Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.</em></strong></p>


``` java
public class Solution {
    /**
     * @param s A string
     * @return whether the string is a valid parentheses
     */
    public boolean isValidParentheses(String s) {
        if (s == null || s.length() == 0) return true;
        
        Stack<character> stack = new Stack<character>();
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else if (c == ')' || c == '}' || c == ']') {
                if (stack.isEmpty()) {
                    return false;//for the case s = "]", stack is empty
                } else {
                    char curr = stack.pop();
                    if ((curr == '(' && c != ')') || (curr == '{' && c != '}') || (curr == '[' && c != ']')) {
                        return false;
                    }
                }
            }
        }
        return stack.isEmpty();
    }
}
```