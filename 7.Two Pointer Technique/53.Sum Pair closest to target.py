'''
Given an array arr[] and a number target, find a pair of elements (a, b) in arr[], where a<=b whose sum is closest to target.
Note: Return the pair in sorted order and if there are multiple such pairs return the pair with maximum absolute difference. If no such pair exists return an empty array.

Examples:

Input: arr[] = [10, 30, 20, 5], target = 25
Output: [5, 20]
Explanation: As 5 + 20 = 25 is closest to 25.
Input: arr[] = [5, 2, 7, 1, 4], target = 10
Output: [2, 7]
Explanation: As (4, 7) and (2, 7) both are closest to 10, but absolute difference of (2, 7) is 5 and (4, 7) is 3. Hence, [2, 7] has maximum absolute difference and closest to target. 
Input: arr[] = [10], target = 10
Output: []
Explanation: As the input array has only 1 element, return an empty array.
Constraints:
1 <= arr.size() <= 2*105
0 <= target<= 2*105
0 <= arr[i] <= 105

'''

class Solution:
    def sumClosest(self, arr, target):
        arr.sort()
        l=0
        r=len(arr)-1
        cs=float('inf')
        md=-1
        result=[]
        
        while l<r:
            s=arr[l]+arr[r]
            d=abs(s-target)
            
            if d<abs(cs-target) or (d==abs(cs-target) and abs(arr[r]-arr[l]>md)):
                cs=s
                md=abs(arr[r]-arr[l])
                result=[arr[l],arr[r]]
                
            if s<target:
                l+=1
            else:
                r-=1
        
        return result