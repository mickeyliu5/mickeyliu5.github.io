---
layout: post
title: Insert Node in a Binary Search Tree
date: 2015-10-21 02:08:49.000000000 -04:00
type: post
published: true
status: publish
categories:
- Binary Search Tree
tags: []
meta:
  _edit_last: '1'
  _wpcom_is_markdown: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1455615897;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:282;}i:1;a:1:{s:2:"id";i:260;}i:2;a:1:{s:2:"id";i:296;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Given a binary search tree and a new tree node, insert the node into the tree. You should keep the tree still be a valid binary search tree.</em></strong><br />
[expand title="code"]</p>
<pre>
public class Solution {
    /*** @param root: The root of the binary search tree.
     * @param node: insert this node into the binary search tree*/
    public TreeNode insertNode(TreeNode root, TreeNode node) {
        if (root == null) return node;//base case!!!
        if (node == null) return root;
        if (node.val <= root.val){
            if (root.left != null) { 
                root.left = insertNode(root.left, node);
            } else { 
                root.left = node;
            }
        } else {
            if (root.right != null) {
                root.right = insertNode(root.right, node);
            } else { 
                root.right = node;
            }
        }
        return root;
    }   
    //iterative approach
    public TreeNode insertNode(TreeNode root, TreeNode node) {    
        if (root == null) return node;
        if (node == null) return root;
        TreeNode curr = root;
        while (curr != null) {
            if (node.val <= curr.val && curr.left == null) {
                curr.left = node;
                break; //first check null, then move
            } else if (node.val > curr.val && curr.right == null) {
                curr.right = node;
                break;// don't forget to break!!!
            } else if (node.val <= curr.val) { 
                curr = curr.left;
            } else { 
                curr = curr.right;
            }
        }
        return root;
    }
}
</pre>
<p>[/expand]</p>