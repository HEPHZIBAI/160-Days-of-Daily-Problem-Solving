'''
You are given an array arr[], in which arr[i] is the price of a given stock on the ith day and an integer k represents a transaction fee. Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Examples:

Input: arr[] = [6, 1, 7, 2, 8, 4], k = 2
Output: 8
Explanation:
Buy the stock on day 2 and sell it on day 3 => 7 – 1 -2 = 4
Buy the stock on day 4 and sell it on day 5 => 8 – 2 - 2 = 4
Maximum Profit  = 4 + 4 = 8
Input: arr[] = [7, 1, 5, 3, 6, 4], k = 1
Output: 5
Explanation: 
Buy the stock on day 2 and sell it on day 3 => 5 – 1 - 1 = 3
Buy the stock on day 4 and sell it on day 5 => 6 – 3 - 1 = 2
Maximum Profit  = 3 + 2 = 5
Constraint:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 106
0 ≤ k ≤ 106
'''
class Solution:
    def maxProfit(self,arr,k):
        n=len(arr)
        ns=0
        ih=0
        
        if n==0:
            return 0
            
        for i in range(n-1,-1,-1):
            nns=max(ns,ih-arr[i])
            nih=max(ih,arr[i]-k+ns)
            ns=nns
            ih=nih
            
        return ns

