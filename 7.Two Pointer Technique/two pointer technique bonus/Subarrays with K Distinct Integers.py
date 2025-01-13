'''
You are given an array arr[] of positive integers and an integer k, find the number of subarrays in arr[] where the count of distinct integers is exactly k.

Note: A subarray is a contiguous part of an array.

Examples:

Input: arr[] = [1, 2, 2, 3], k = 2
Output: 4
Explanation: Subarrays formed with exactly 2 different integers are: arr[0..1], arr[0..2], arr[1..3] and arr[2..3].
Input: arr[] = [3, 1, 2, 2, 3], k = 3
Output: 4
Explanation: Subarrays formed with exactly 3 distinct integers are: arr[0..2], arr[0..3], arr[0..4], arr[1..4].
Input: arr[] = [1, 1, 1, 1], k = 2
Output: 0
Explanation: There is no subarray having exactly 2 distinct integers.
Constraints:
1 ≤ arr.size() ≤ 104
1 ≤ k ≤ arr.size()
1≤ arri  ≤ arr.size()


'''


class Solution:
    def at_most_k(self,arr,k):
        s=0
        f={}
        c=0
        
        for e in range(len(arr)):
            f[arr[e]]=f.get(arr[e],0)+1
            while len(f)>k:
                f[arr[s]]-=1
                
                if f[arr[s]]==0:
                    del f[arr[s]]
                s+=1
                
            c+=e-s+1
        return c
        
    def exactlyK(self, arr, k):
        return self.at_most_k(arr,k)-self.at_most_k(arr,k-1)