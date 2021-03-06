---
layout: post
title: Buy one get one free
date: 2015-10-23 21:00:16.000000000 -04:00
tags:
- Leetcode
categories:
- Dynamic Programming
author: Jason
---
<p><strong><em>一堆商品，买一个可以送一个，但送的那个的价格必须小于买的那个的价格（强调一下，不能等于）。给定商品总数n和每个商品的价格，求得到全部商品的最少开销。 例如：4个商品价格为[5, 4, 3, 3]，最优解为9，即买5和4，送3和3。 两个test case: [100, 99, 98, 1, 1, 1], [100, 99, 98, 98, 97, 97, 97, 97]</em></strong></p>


<p><a href="http://www.jiuzhang.com/qa/221/">Dynamic programming</a></p>

首先排序不用说了。从小到大。然后先给出DP的方程：</p>
<p>定义状态 f[i][j] 为 i 到 j 这一段的最优值（最少花多少钱全买下来）</p>
    f[i][j] = min(f[i + 1][j - 1]+A[j], f[i][k] + f[k+1][j]) 其中k为i到j-1。</p>
然后我们来证明为什么这个方程是对的。这个方程的假设前提是，不存在相交的搭配，也就是说不存在下面这种情况的匹配：</p>
<p>从小到大的4个数：a&lt;= b&lt;= c&lt;= d。 a与c一起买，b与d一起买。</p>
为毛呢？首先a和d肯定不相等，否则的话，abcd都相等了，这种情况是不会出现的（我们就是要证明这种情况不会出现），然后看b和c，如果他们相等，那么换成(a,b)和(c,d)，代价一样，并且不会产生相交的匹配（什么叫做相交？你在ac连一条曲线，和bd之间的曲线一定相交）。然后看b和c不等的情况，不等的话，换成(b,c) + (a,d)，也还是不影响结果=c+d， 然后又能使得连线不相交。</p>
<p>好了，上面我们证明了不相交理论。那么既然连线不想交的话，i-j这一段的匹配情况，只存在两种可能性：</p>
<p>第一种可能是i和j匹配，然后中间的自己配对。</p>
第二种可能是，一定存在一条分割线，使得这个i-j的区间被分为i-k和k+1-j，两个区间之间的自己匹配，没有互相的连边。</p>
好了，综上所述。问题已经解决并证明。我知道理解起来有点难，特别是证明，我也证明了好久……</p>
<p>顺便说一下时间复杂度 ： O(n^3)，可能可以用决策单调的优化优化到O(n^2)。</p>
[/expand]</p>
