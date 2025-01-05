'''
Given a sorted array arr[] and a target value, the task is to count triplets (i, j, k) of valid indices, such that arr[i] + arr[j] + arr[k] = target and i < j < k.

Examples:

Input: arr[] = [-3, -1, -1, 0, 1, 2], target = -2
Output: 4
Explanation: Two triplets that add up to -2 are:
arr[0] + arr[3] + arr[4] = (-3) + 0 + (1) = -2
arr[0] + arr[1] + arr[5] = (-3) + (-1) + (2) = -2
arr[0] + arr[2] + arr[5] = (-3) + (-1) + (2) = -2
arr[1] + arr[2] + arr[3] = (-1) + (-1) + (0) = -2
Input: arr[] = [-2, 0, 1, 1, 5], target = 1
Output: 0
Explanation: There is no triplet whose sum is equal to 1. 
Constraints:
3 ≤ arr.size() ≤ 104
-105 ≤ arr[i], target ≤ 105


'''

class Solution:
    def countTriplets(self, arr, target):
        arr.sort()
        n=len(arr)
        count=0
        
        for i in range(n-2):
            l=i+1
            r=n-1
            
            while l<r:
                s=arr[i]+arr[l]+arr[r]
                
                if s==target:
                    if arr[l]==arr[r]:
                        nu=r-l+1
                        count+=nu*(nu-1)//2
                        break
                    else:
                        cl=1
                        cr=1
                        while(l+1<r and arr[l]==arr[l+1]):
                            l+=1
                            cl+=1
                        while r-1>l and arr[r]==arr[r-1]:
                            r-=1
                            cr+=1
                        count+=cl*cr
                        l+=1
                        r-=1
                elif s<target:
                    l+=1
                else:
                    r-=1
    
        return count
