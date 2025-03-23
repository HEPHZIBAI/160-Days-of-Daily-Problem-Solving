'''
Given an array arr[], determine if it can be partitioned into two subsets such that the sum of elements in both parts is the same.

Note: Each element must be in exactly one subset.

Examples:

Input: arr = [1, 5, 11, 5]
Output: true
Explanation: The two parts are [1, 5, 5] and [11].
Input: arr = [1, 3, 5]
Output: false
Explanation: This array can never be partitioned into two such parts.
Constraints:
1 ≤ arr.size ≤ 100
1 ≤ arr[i] ≤ 200

'''

class Solution:
    def equalPartition(self, arr):
        ts=sum(arr)
        
        if ts%2!=0:
            return False
            
        t=ts//2
        n=len(arr)
        dp=[False]*(t+1)
        dp[0]=True
        
        for i in arr:
            for j in range(t,i-1,-1):
                dp[j]=dp[j] or dp[j-i]
                
        return dp[t]