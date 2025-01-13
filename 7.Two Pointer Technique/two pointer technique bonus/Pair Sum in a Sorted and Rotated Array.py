'''
Given an array of positive elements arr[] that is sorted and then rotated around an unknown point, the task is to check if the array has a pair with sum equals to a given target.

Examples:

Input: arr[] = [7, 9, 1, 3, 5], target = 6
Output: true
Explanation: arr[2] and arr[4] has sum equals to 6 which is equal to the target.
Input: arr[] = [2, 3, 4, 1], target = 3
Output: true
Explanation: arr[0] and arr[3] has sum equals to 3 which is equal to the target.
Input: arr[] = [10, 7, 4, 1], target = 9
Output: false
Explanation: There is no such pair exists in arr[] which sums to target.
Constraints:
2 <= arr.size() <=106
1 <= arr[i] <= 106
1 <= target <= 106
'''


class Solution:
    def pairInSortedRotated(self,arr, target):
        n=len(arr)
        p=0
        
        for i in range(1,n):
            if arr[i]<arr[i-1]:
                p=i
                break
            
        l=p
        r=(p-1+n)%n
        
        while l!=r:
            cs=arr[l]+arr[r]
            
            if cs==target:
                return True
            elif cs<target:
                l=(l+1)%n
            else:
                r=(r-1+n)%n
        
        return False