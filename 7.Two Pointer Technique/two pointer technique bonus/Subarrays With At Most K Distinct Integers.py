'''
You are given an array arr[] of positive integers and an integer k, find the number of subarrays in arr[] where the count of distinct integers is at most k.

Note: A subarray is a contiguous part of an array.

Examples:

Input: arr[] = [1, 2, 2, 3], k = 2
Output: 9
Explanation: Subarrays with at most 2 distinct elements are: [1], [2], [2], [3], [1, 2], [2, 2], [2, 3], [1, 2, 2] and [2, 2, 3].
Input: arr[] = [1, 1, 1], k = 1
Output: 6
Explanation: Subarrays with at most 1 distinct element are: [1], [1], [1], [1, 1], [1, 1] and [1, 1, 1].
Input: arr[] = [1, 2, 1, 1, 3, 3, 4, 2, 1], k = 2
Output: 24
Explanation: There are 24 subarrays with at most 2 distinct elements.
Constraints:
1 ≤ arr.size() ≤ 104
1 ≤ k ≤ arr.size()
1≤ arri  ≤ arr.size()


'''

class Solution:
    def atMostK(self, arr, k):
        s=0
        f={}
        count=0
        
        for e in range(len(arr)):
            f[arr[e]]=f.get(arr[e],0)+1
            while len(f)>k:
                f[arr[s]]-=1
                if f[arr[s]]==0:
                    del f[arr[s]]
                s+=1
                
            count+=e-s+1
        return count