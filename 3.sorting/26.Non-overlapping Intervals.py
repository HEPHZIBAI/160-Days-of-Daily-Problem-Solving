'''
Given a 2D array intervals[][] of representing intervals where intervals [i] = [starti, endi ]. Return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Examples:

Input: intervals[][] = [[1, 2], [2, 3], [3, 4], [1, 3]]
Output: 1
Explanation: [1, 3] can be removed and the rest of the intervals are non-overlapping.
Input: intervals[][] = [[1, 3], [1, 3], [1, 3]]
Output: 2
Explanation: You need to remove two [1, 3] to make the rest of the intervals non-overlapping.
Input: intervals[][] = [[1, 2], [5, 10], [18, 35], [40, 45]]
Output: 0
Explanation: All ranges are already non overlapping.
Constraints:
1 ≤ intervals.size() ≤  105
|intervalsi| == 2
0 ≤ starti < endi <=5*104

'''


class Solution:
    def minRemoval(self, intervals):
        intervals.sort(key=lambda x: x[1])
        removed_intervals = 0
        last_end = float('-inf') 
        
        for start, end in intervals:
            if start >= last_end:
                last_end = end
            else:
                removed_intervals += 1
        
        return removed_intervals

