'''
Given an array arr[] of distinct positive integers, your task is to find all its subsets. The subsets should be returned in lexicographical order.

Examples:

Input: arr = [1, 2, 3]
Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
Explanation: 
The subsets of [1, 2, 3] in lexicographical order are:
[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]
Input: arr = [1, 2]
Output: [[], [1], [1, 2], [2]]
Explanation:
The subsets of [1, 2] in lexicographical order are:
[], [1], [1, 2], [2]
Input: arr = [10]
Output: [[], [10]]
Explanation: For the array with a single element [10], the subsets are [ ] and [10].
Constraints :
1 ≤ arr.size() ≤ 10
1 ≤ arr[i] ≤ 10

'''

class Solution:
    def subsets(self, arr):
        n=len(arr)
        arr.sort()
        res=[]
        
        for i in range(1<<n):
            s=[]
            for j in range(n):
                if (i&(1<<j))!=0:
                    s.append(arr[j])
                
            res.append(s)
            
        res.sort()
        return res