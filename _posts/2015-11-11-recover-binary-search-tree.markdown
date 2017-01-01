---
layout: post
title: Recover Binary Search Tree
date: 2015-11-11 17:51:55.000000000 -05:00
type: post
published: true
status: publish
categories:
- Binary Search Tree
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466044830;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:596;}i:1;a:1:{s:2:"id";i:268;}i:2;a:1:{s:2:"id";i:1161;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Two elements of a binary search tree (BST) are swapped by mistake.<br />
Recover the tree without changing its structure.</em></strong></p>
<p>[expand title = "O(1) space"]</p>
<pre>
public class Solution {
    private TreeNode n1 = null, n2 = null, prev = null;
    public void recoverTree(TreeNode root) {
        if (root == null) return;
        recover(root);
        int temp = n1.val;
        n1.val = n2.val;
        n2.val = temp;
    }
    public void recover(TreeNode root) {
        if (root == null) return;
        recover(root.left);
        if (prev != null && prev.val > root.val) {
            if (n1 == null) {
                n1 = prev;
            }
            n2 = root;
        }
        prev = root;
        recover(root.right);
    }
}
</pre>
<p>[/expand]</p>
<p>[expand title="O(n) space"]</p>
<pre>
public class Solution {
    public void recoverTree(TreeNode root) {
        if (null == root) return;
        
        Stack<treenode> stack = new Stack<treenode>();
        TreeNode node1 = null, node2 = null, prev = null;
        while (root != null || !stack.isEmpty()) {
            if (root != null) {
                stack.push(root);
                root = root.left;
            } else {
                root = stack.pop();
                if (prev != null && root.val < prev.val) {
                    if (node1 == null) {
                        node1 = prev;
                    } 
                    node2 = root;//we need to update both node1 and node2 here, otherwise for the case of two nodes only, node2 will be null
                }
                prev = root;
                root = root.right;
            }
        }
        int temp = node1.val;
        node1.val = node2.val;
        node2.val = temp;
    }
}
</treenode></treenode></pre>
<p>[/expand]</p>