'''
Given an array arr[] of integers and another integer target. Find all unique quadruples from the given array that sums up to target.

Note: All the quadruples should be internally sorted, ie for any quadruple [q1, q2, q3, q4] it should be : q1 <= q2 <= q3 <= q4.

Examples :

Input: arr[] = [0, 0, 2, 1, 1], target = 3
Output: [0, 0, 1, 2] 
Explanation: Sum of 0, 0, 1, 2 is equal to 3.
Input: arr[] = [10, 2, 3, 4, 5, 7, 8], target = 23
Output: [[2, 3, 8, 10], [2, 4, 7, 10], [3, 5, 7, 8]] 
Explanation: Sum of 2, 3, 8, 10 is 23, sum of 2, 4, 7, 10 is 23 and sum of 3, 5, 7, 8 is also 23.
Input: arr[] = [0, 0, 2, 1, 1], target = 2
Output: [0, 0, 1, 1] 
Explanation: Sum of 0, 0, 1, 2 is equal to 2.
Constraints:
1 <= arr.size() <= 200
-106 <= target <= 106
-106 <= arr[i] <= 106
'''

class Solution:
    def fourSum(self, arr, target):
        arr.sort()
        n=len(arr)
        rr=[]
        
        for i in range(n-3):
            if i>0 and arr[i]==arr[i-1]:
                continue
            
            for j in range(i+1,n-2):
                if j>i+1 and arr[j]==arr[j-1] :
                    continue
                
                l,r=j+1,n-1
                while l<r:
                    cs=arr[i]+arr[j]+arr[l]+arr[r]
                    
                    if cs==target:
                        rr.append([arr[i],arr[j],arr[l],arr[r]])

                        while l<r and arr[l]==arr[l+1]:
                            l+=1
                        while l<r and arr[r]==arr[r-1]:
                            r-=1
                            
                        l+=1
                        r-=1
                        
                    elif cs<target:
                        l+=1
                    else:
                        r-=1
        return rr