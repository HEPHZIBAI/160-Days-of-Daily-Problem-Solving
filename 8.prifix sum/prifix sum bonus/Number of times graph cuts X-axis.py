'''
Given an integer array arr[], where each arr[i] denotes the trajectory of the graph over the plane; i.e. arr[i]>0 means graph going above its current position by arr[i] value and arr[i]<0 means graph going down by arr[i] value. If initial position of the graph is at origin, determines the number of times graph crosses or touches the X-axis.

Example:

Input: arr[] = [2, 5, -9, 4]
Output: 2
Explanation: Graph touches the X-axis two times through index 1 to 2, and through index 2 to 3.
Input: arr[] = [4, -6, 2, 8, -2, 3, -12]
Output: 3
Explanation:

Graph touches the X-axis three times through index 0 to 1, through index 1 to 2, and through index 5 to 6.
Input: arr[] = [1, 3, 5]
Output: 0
Explanation: Graph has not touched the X-axis any time.
Constraints:
1 <= arr.size() <= 105
-104 <= arr[i] <= 104
arr[i] does not contains any zero.
'''
class Solution:
    def touchedXaxis(self, arr):
        cr=0
        cu=0
        ps=0
        
        for i in arr:
            cu+=i
            
            if cu==0 or(cu>0 and ps<0)or (cu<0 and ps>0):
                cr+=1
                
            ps=cu
            
        return cr
