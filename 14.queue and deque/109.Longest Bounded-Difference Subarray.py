'''
Given an array of positive integers arr[] and a non-negative integer x, the task is to find the longest sub-array where the absolute difference between any two elements is not greater than x.
If multiple such subarrays exist, return the one that starts at the smallest index.

Examples: 

Input: arr[] = [8, 4, 2, 6, 7], x = 4 
Output: [4, 2, 6] 
Explanation: The sub-array described by index [1..3], i.e. [4, 2, 6] contains no such difference of two elements which is greater than 4.
Input: arr[] = [15, 10, 1, 2, 4, 7, 2], x = 5 
Output: [2, 4, 7, 2] 
Explanation: The sub-array described by indexes [3..6], i.e. [2, 4, 7, 2] contains no such difference of two elements which is greater than 5. 
Constraints:
1 <= arr.size() <= 105
1 <= arr[i] <= 109
0 <= x<= 109



'''


from collections import deque

class Solution:
    def longestSubarray(self, arr, x):
        left=0
        maxd=deque()
        mind=deque()
        ml=0
        si=0
        
        for right in range(len(arr)):
            while maxd and arr[maxd[-1]]<arr[right]:
                maxd.pop()
            maxd.append(right)
            
            while mind and arr[mind[-1]]>arr[right]:
                mind.pop()
            mind.append(right)
            
            while arr[maxd[0]]-arr[mind[0]]>x:
                left+=1
                if maxd[0]<left:
                    maxd.popleft()
                if mind[0]<left:
                    mind.popleft()
                    
            if right-left+1>ml:
                ml=right-left+1
                si=left
                
        return arr[si:si+ml]