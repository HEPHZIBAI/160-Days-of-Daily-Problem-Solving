'''
You are given a histogram represented by an array arr, where each element of the array denotes the height of the bars in the histogram. All bars have the same width of 1 unit.

Your task is to find the largest rectangular area possible in the given histogram, where the rectangle can be formed using a number of contiguous bars.

Examples:

Input: arr[] = [60, 20, 50, 40, 10, 50, 60]
 Largest-Rectangular-Area-in-a-Histogram
Output: 100
Explanation: We get the maximum by picking bars highlighted above in green (50, and 60). The area is computed (smallest height) * (no. of the picked bars) = 50 * 2 = 100.
Input: arr[] = [3, 5, 1, 7, 5, 9]
Output: 15
Explanation:  We get the maximum by picking bars 7, 5 and 9. The area is computed (smallest height) * (no. of the picked bars) = 5 * 3 = 15.
Input: arr[] = [3]
Output: 3
Explanation: In this example the largest area would be 3 of height 3 and width 1.
Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 104

'''


class Solution:
    def getMaxArea(self,arr):
        stack=[]
        ma=0
        n=len(arr)
        
        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                height=arr[stack.pop()]
                width=i if not stack else i-stack[-1]-1
                ma=max(ma,height*width)
            stack.append(i)
            
        while stack:
            height=arr[stack.pop()]
            width=n if not stack else n-stack[-1]-1
            ma=max(ma,height*width)
            
        return ma