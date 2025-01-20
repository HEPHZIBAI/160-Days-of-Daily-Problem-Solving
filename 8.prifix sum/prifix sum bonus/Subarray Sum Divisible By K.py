'''
You are given an integer array arr[] and a value k. The task is to find the count of all sub-arrays whose sum is divisible by k.

Examples:

Input: arr[] = [4, 5, 0, -2, -3, 1], k = 5
Output: 7
Explanation: There are 7 sub-arrays whose sum is divisible by k: [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3] and [-2, -3]
Input: arr[] = [2, 2, 2, 2, 2, 2], k = 2
Output: 21
Explanation: All subarray sums are divisible by 2
Input: arr[] = [-1, -3, 2], k = 5
Output: 0
Explanation: There is no such sub-array whose sum is divisible by k.
Constraints:
1 ≤ arr.size() ≤ 104
-106 ≤ arr[i]≤ 106
1 ≤ k ≤ 104


'''
class Solution:
    def subCount(self, arr, k):
        rm={0:1}
        ps=0
        c=0
        
        for i in arr:
            ps+=i
            r=ps%k
            
            if r<0:
                r+=k
            
            if r in rm:
                c+=rm[r]
                
            rm[r]=rm.get(r,0)+1
            
        return c
