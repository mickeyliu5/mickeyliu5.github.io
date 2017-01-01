---
layout: post
title: Construct Binary Tree from Preorder and Inorder Traversal
date: 2015-10-21 02:55:10.000000000 -04:00
type: post
published: true
status: publish
categories:
- Binary Search Tree
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1464880773;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:274;}i:1;a:1:{s:2:"id";i:47;}i:2;a:1:{s:2:"id";i:1234;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p>[expand title="code"]</p>
<pre>
//basic idea: the first element in preorder is the root
//the root int inorder divides the inorder into left subtree and right subtree, which are also subtrees in preorder
//we find the index of root in inorder and get the length of left subtree, recursively get root.left
public class Solution {
    /**
     *@param preorder : A list of integers that preorder traversal of a tree
     *@param inorder : A list of integers that inorder traversal of a tree
     *@return : Root of a tree
     */
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder == null || inorder == null || preorder.length == 0 || inorder.length == 0 || preorder.length != inorder.length) return null;
        
        return buildTreeUtil(preorder, 0, preorder.length - 1, inorder, 0, inorder.length - 1);
    }
    public int findIndex(int[] nums, int start, int end, int target) {
        for (int i = start; i <= end; i ++) {
            if (nums[i] == target) {
                return i;
            } 
        }
        return -1;
    }
    public TreeNode buildTreeUtil(int[] preorder, int pre_start, int pre_end, int[] inorder, int in_start, int in_end) {
        if (pre_start > pre_end || in_start > in_end) return null;
        int root_val = preorder[pre_start];//not preorder[0] !!!
        TreeNode root = new TreeNode(root_val);
        int index = findIndex(inorder, in_start, in_end, root_val);
        root.left = buildTreeUtil(preorder, pre_start + 1, pre_start + index - in_start, inorder, in_start, index - 1);
        root.right = buildTreeUtil(preorder, pre_start + index - in_start + 1, pre_end, inorder, index + 1, in_end);
        return root;
    }
}
</pre>
<p>[/expand]</p>