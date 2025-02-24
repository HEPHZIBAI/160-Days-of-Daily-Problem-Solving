'''
Given two arrays start[] and end[] such that start[i] is the starting time of ith meeting and end[i] is the ending time of ith meeting. Return the minimum number of rooms required to attend all meetings.

Examples:

Input: start[] = [1, 10, 7], end[] = [4, 15, 10]
Output: 1
Explanation: Since all the meetings are held at different times, it is possible to attend all the meetings in a single room.
Input: start[] = [2, 9, 6], end[] = [4, 12, 10]
Output: 2
Explanation: 1st and 2nd meetings at one room but for 3rd meeting one another room required.
Constraints:
1 ≤ start.size() ≤ 105
0 ≤ start[i] < end[i] ≤ 106



'''


import heapq

class Solution:
    def minMeetingRooms(self, start, end):
        start.sort()
        end.sort()
        mr=0
        heap=[]
        ei=0
        
        for s in start:
            while heap and heap[0]<=s:
                heapq.heappop(heap)
            
            heapq.heappush(heap,end[ei])
            ei+=1
            mr=max(mr,len(heap))
            
        return mr