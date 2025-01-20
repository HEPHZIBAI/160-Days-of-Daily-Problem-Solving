'''
Given an array, arr[] construct a product array, res[] where each element in res[i] is the product of all elements in arr[] except arr[i]. Return this resultant array, res[].
Note: Each element is res[] lies inside the 32-bit integer range.

Examples:

Input: arr[] = [10, 3, 5, 6, 2]
Output: [180, 600, 360, 300, 900]
Explanation: For i=0, res[i] = 3 * 5 * 6 * 2 is 180.
For i = 1, res[i] = 10 * 5 * 6 * 2 is 600.
For i = 2, res[i] = 10 * 3 * 6 * 2 is 360.
For i = 3, res[i] = 10 * 3 * 5 * 2 is 300.
For i = 4, res[i] = 10 * 3 * 5 * 6 is 900.
Input: arr[] = [12, 0]
Output: [0, 12]
Explanation: For i = 0, res[i] is 0.
For i = 1, res[i] is 12.
Constraints:
2 <= arr.size() <= 105
-100 <= arr[i] <= 100



'''

class Solution:
    def productExceptSelf(self, arr):
        n=len(arr)
        p=[1]*n
        s=[1]*n
        r=[0]*n
        
        for i in range(1,n):
            p[i]=p[i-1]*arr[i-1]
            
        for i in range(n-2,-1,-1):
            s[i]=s[i+1]*arr[i+1]
            
        for i in range(n):
            r[i]=p[i]*s[i]
            
        return r