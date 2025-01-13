'''
Given an integer array arr[] and a number k. Find the count of distinct elements in every window of size k in the array.

Examples:

Input: arr[] = [1, 2, 1, 3, 4, 2, 3], k = 4
Output:  [3, 4, 4, 3]
Explanation: Window 1 of size k = 4 is 1 2 1 3. Number of distinct elements in this window are 3. 
Window 2 of size k = 4 is 2 1 3 4. Number of distinct elements in this window are 4.
Window 3 of size k = 4 is 1 3 4 2. Number of distinct elements in this window are 4.
Window 4 of size k = 4 is 3 4 2 3. Number of distinct elements in this window are 3.
Input: arr[] = [4, 1, 1], k = 2
Output: [2, 1]
Explanation: Window 1 of size k = 2 is 4 1. Number of distinct elements in this window are 2. 
Window 2 of size k = 2 is 1 1. Number of distinct elements in this window is 1. 
Input: arr[] = [1, 1, 1, 1, 1], k = 3
Output: [1, 1, 1]
Constraints:
1 <= k <= arr.size() <= 105
1 <= arr[i] <= 105
'''


class Solution:
    def countDistinct(self, arr, k):
        n=len(arr)
        
        if k>n:
            return []
            
        r=[]
        fm={}
        
        for i in range(k):
            fm[arr[i]]=fm.get(arr[i],0)+1
            
        r.append(len(fm))
        
        for i in range(k,n):
            fm[arr[i]]=fm.get(arr[i],0)+1
            fm[arr[i-k]]-=1
            
            if fm[arr[i-k]]==0:
                del fm[arr[i-k]]
                
            r.append(len(fm))
        return r