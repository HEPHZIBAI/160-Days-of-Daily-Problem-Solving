'''
Given an array arr[], return the sum of the XOR of all elements for every possible subset of the array. Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

Note: The answer is guaranteed to fit within a 32-bit integer.

Examples:

Input: arr[] = [7, 2]
Output: 14
Explanation: Subsets are: [[], [7], [2], [7, 2]]
Sum of all XOR's = 7 + 2 + (7 ^ 2) = 14.
Input: arr[] = [1, 2, 3]
Output: 12
Explanation: Subsets are: [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
Sum of all XOR's = 1 + 2 + 3 + (1 ^ 2)  + (1 ^ 3) + (2 ^ 3) + (1 ^ 2 ^ 3) = 12.
Constraints:
1 ≤ arr.size() ≤ 30
1 ≤ arr[i] ≤ 103
'''

#User function Template for python3
class Solution:
    def subsetXORSum(self, arr):
        n=len(arr)
        b=0
        
        for i in range(n):
            b|=arr[i]
            
        ans=b*(2**(n-1))
        
        return ans