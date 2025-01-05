'''
Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in sorted order without using any extra space. Modify a[] so that it contains the first n elements and modify b[] so that it contains the last m elements.

Examples:

Input: a[] = [2, 4, 7, 10], b[] = [2, 3]
Output:
2 2 3 4
7 10
Explanation: After merging the two non-decreasing arrays, we get, 2 2 3 4 7 10
Input: a[] = [1, 5, 9, 10, 15, 20], b[] = [2, 3, 8, 13]
Output:
1 2 3 5 8 9
10 13 15 20
Explanation: After merging two sorted arrays we get 5 10 12 18 20.
Input: a[] = [0, 1], b[] = [2, 3]
Output:
0 1
2 3
Explanation: After merging two sorted arrays we get 0 1 2 3.
Constraints:
1 <= a.size(), b.size() <= 105
0 <= a[i], b[i] <= 107
'''

class Solution:
    def mergeArrays(self, a, b):
        import math
        n, m = len(a), len(b)
        gap = math.ceil((n + m) / 2)
        
        while gap > 0:
            i, j = 0, gap
            
            # Compare elements within `a`
            while j < n:
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]
                i += 1
                j += 1
            
            # Compare elements between `a` and `b`
            j = j - n  # Adjust j for the `b` array
            while i < n and j < m:
                if a[i] > b[j]:
                    a[i], b[j] = b[j], a[i]
                i += 1
                j += 1
            
            # Compare elements within `b`
            i = 0
            while j < m:
                if b[i] > b[j]:
                    b[i], b[j] = b[j], b[i]
                i += 1
                j += 1
            
            # Update gap
            if gap == 1:
                gap = 0
            else:
                gap = math.ceil(gap / 2)
        
        return a, b