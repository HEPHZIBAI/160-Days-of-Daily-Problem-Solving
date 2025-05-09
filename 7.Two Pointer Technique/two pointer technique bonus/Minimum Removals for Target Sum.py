'''
You are given an array of positive integers arr[] and an integer k. In one operation, you can remove either the leftmost or the rightmost element from the array. After each operation, the size of arr[] will be reduced by one.

Your task is to determine the minimum number of operations required to make the total sum of removed elements exactly equal to k. If it is not possible to achieve this, return -1.

Examples:

Input: arr[] = [3, 4, 1, 3, 2], k = 5
Output: 2
Explanation: Removing 3 from left and 2 from right gives a sum of 5 in 2 operations.
Input: arr[] = [5, 3, 4, 6, 2], k = 6
Output: -1
Explanation: It is impossible to achieve the sum of removed elements as 6.
Input: arr[] = [1, 1, 3, 1, 2], k = 4
Output: 3
Explanation: Removing 1, 1 from left and 2 from right gives a sum of 4 in 3 operation.
Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 104
1 ≤ k ≤ arr.size()



'''


class Solution:
    def minRemovals(self, arr, k):
        total=sum(arr)
        
        if k>total:
            return -1
            
        t=total-k
        n=len(arr)
        cs=0
        ml=-1
        s=0
        
        for e in range(n):
            cs+=arr[e]
            
            while cs>t:
                cs-=arr[s]
                s+=1
                
            if cs==t:
                ml=max(ml,e-s+1)
                
        if ml==-1:
            return -1
        return n-ml
