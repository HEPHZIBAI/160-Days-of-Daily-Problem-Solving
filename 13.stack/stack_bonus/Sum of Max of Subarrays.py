'''
Given an array arr[], the task is to find the sum of the maximum elements of every possible non-empty sub-arrays of the given array arr[].

Note: The answer will always fit into 32 bit integer.

Examples:

Input: arr[] = [1, 3, 2]
Output: 15
Explanation: All possible non-empty subarrays of [1, 3, 2] are [1], [3], [2], [1, 3], [3, 2] and [1, 3, 2]. The maximum elements of the subarrays are 1, 3, 2, 3, 3, 3 respectively. The sum will be 15.
Input: arr[] = [3, 1]
Output: 7
Explanation: All possible non-empty subarrays of [3, 1] are [3], [1] and [3, 1]. The maximum elements of the subarrays are 3, 1, 3 respectively. The sum will be 7.
Input: arr[] = [8, 0, 1]
Output: 26
Explanation: All possible non-empty subarrays of [8, 0, 1] are [8], [0], [1], [8, 0], [0, 1] and [8, 0, 1]. The maximum elements of the subarrays are 8, 0, 1, 8, 1, 8 respectively. The sum will be 26.
Constraints:
1 <= arr.size() <= 104
0 <= arr[i] <= 109

'''

class Solution:
    def sumOfMax(self, arr):
        n=len(arr)
        res=0
        stk=[]
        left=[0]*n
        right=[0]*n
        
        for i in range(n):
            while stk and arr[stk[-1]]<arr[i]:
                stk.pop()
                
            left[i]=(i+1) if not stk else (i-stk[-1])
            stk.append(i)
        stk.clear()
        for i in range(n-1,-1,-1):
            while stk and arr[stk[-1]]<=arr[i]:
                stk.pop()
                
            right[i]=(n-i) if not stk else (stk[-1]-i)
            stk.append(i)
            
        for i in range(n):
            res+=arr[i]*left[i]*right[i]
            
        return res
