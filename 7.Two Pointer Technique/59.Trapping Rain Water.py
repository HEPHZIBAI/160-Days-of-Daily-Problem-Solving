'''
Given an array arr[] with non-negative integers representing the height of blocks. If the width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 

Examples:

Input: arr[] = [3, 0, 1, 0, 4, 0 2]
Output: 10
Explanation: Total water trapped = 0 + 3 + 2 + 3 + 0 + 2 + 0 = 10 units.

Input: arr[] = [3, 0, 2, 0, 4]
Output: 7
Explanation: Total water trapped = 0 + 3 + 1 + 3 + 0 = 7 units.
Input: arr[] = [1, 2, 3, 4]
Output: 0
Explanation: We cannot trap water as there is no height bound on both sides.
Input: arr[] = [2, 1, 5, 3, 1, 0, 4]
Output: 9
Explanation: Total water trapped = 0 + 1 + 0 + 1 + 3 + 4 + 0 = 9 units.
Constraints:
1 < arr.size() < 105
0 < arr[i] < 103
'''


class Solution:
    def maxWater(self, arr):
        n=len(arr)
        if n<3:
            return 0
            
        l,r=0,n-1
        lm,rm=0,0
        wt=0
        
        while l<=r:
            if arr[l]<=arr[r]:
                if arr[l]>=lm:
                    lm=arr[l]
                else:
                    wt+=lm-arr[l]
                l+=1
            else:
                if arr[r]>=rm:
                    rm=arr[r]
                else:
                    wt+=rm-arr[r]
                r-=1
                
        return wt
