'''
Given an array of integers arr[] that is first strictly increasing and then maybe strictly decreasing, find the bitonic point, that is the maximum element in the array.
Bitonic Point is a point before which elements are strictly increasing and after which elements are strictly decreasing.

Examples:

Input: arr[] = [1, 2, 4, 5, 7, 8, 3]
Output: 8
Explanation: Elements before 8 are strictly increasing [1, 2, 4, 5, 7] and elements after 8 are strictly decreasing [3].
Input: arr[] = [10, 20, 30, 40, 50]
Output: 50
Explanation: Elements before 50 are strictly increasing [10, 20, 30 40] and there are no elements after 50.
Input: arr[] = [120, 100, 80, 20, 0]
Output: 120
Explanation: There are no elements before 120 and elements after 120 are strictly decreasing [100, 80, 20, 0].
Constraints:
3 ≤ arr.size() ≤ 105
1 ≤ arr[i]≤ 106


'''

#User function Template for python3
class Solution:
    def findMaximum(self, arr):
        low, high = 0, len(arr) - 1
        
        # Binary search
        while low <= high:
            mid = (low + high) // 2
     
            if (mid == 0 or arr[mid - 1] < arr[mid]) and (mid == len(arr) - 1 or arr[mid + 1] < arr[mid]):
                return arr[mid]
           
            elif mid < len(arr) - 1 and arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1
