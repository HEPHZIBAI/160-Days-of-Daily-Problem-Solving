'''
Given an array arr[] and an integer target, you need to find and return the count of quadruplets such that the index of each element of the quadruplet is unique and the sum of the elements is equal to target.

Examples:

Input: arr[] = [1, 5, 3, 1, 2, 10], target = 20
Output: 1
Explanation: Only quadruplet satisfying the condition is arr[1] + arr[2] + arr[4] + arr[5] = 5 + 3 + 2 + 10 = 20. Hence, the answer is 1.
Input: arr[] = [1, 1, 1, 1, 1], target = 4
Output: 5
Explanation: Three quadruplets with sum 4 are:
arr[0] + arr[1] + arr[2] + arr[3] = 1 + 1 + 1 + 1 = 4
arr[1] + arr[2] + arr[3] + arr[4] = 1 + 1 + 1 + 1 = 4
arr[0] + arr[2] + arr[3] + arr[4] = 1 + 1 + 1 + 1 = 4
arr[0] + arr[1] + arr[3] + arr[4] = 1 + 1 + 1 + 1 = 4
arr[0] + arr[1] + arr[2] + arr[4] = 1 + 1 + 1 + 1 = 4
Input: arr = [4, 3, -13, 3], target = -3
Output: 1
Explanation: There is only 1 quadruplet with sum = -3, that is [4, 3, -13, 3].
Constraints:
1 <= arr.length <= 103
-105 <=arr[i]<= 105
-105 <=target<= 105


'''

class Solution:
    def countSum(self, arr, target):
        n=len(arr)
        count=0
        m=defaultdict(int)
        
        
        for i in range(n-1):
            for j in range(i+1,n):
                t=arr[i]+arr[j]
                count+=m[target-t]
                
                    
            for j in range(i):
                t=arr[i]+arr[j]
                m[t]+=1
            
        return count