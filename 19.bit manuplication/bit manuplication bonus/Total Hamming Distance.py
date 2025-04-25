'''
Given an integer array arr[], return the sum of Hamming distances between all the pairs of the integers in arr.

Note: The answer is guaranteed to fit within a 32-bit integer.

Examples:

Input: arr[] = [1, 14]
Output: 4
Explanation: Binary representations of 1 is 0001, 14 is 1110. The answer will be:
HammingDistance(1, 14) = 4.
Input: arr[] = [4, 14, 4, 14]
Output: 8
Explanation: Binary representations of 4 is 0100, 14 is 1110. The answer will be:
HammingDistance(4, 14) + HammingDistance(4, 4) + HammingDistance(4, 14) + HammingDistance(14, 4) + HammingDistance(14, 14) + HammingDistance(4, 14) = 2 + 0 + 2 + 2 + 0 + 2 = 8.
Constraints:
2 ≤ arr.size() ≤ 104
1 ≤ arr[i] ≤ 109



'''


#User function Template for python3
class Solution:
    def totHammingDist(self, arr):
        n=len(arr)
        c=0
        co=[0]*32
        
        for i in arr:
            for j in range(32):
                if i & (1<<j):
                    co[j]+=1
                    
        for i in range(32):
            c+=co[i]*(n-co[i])
            
        return c