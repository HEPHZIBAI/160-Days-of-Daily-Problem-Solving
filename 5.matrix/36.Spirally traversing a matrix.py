'''
You are given a rectangular matrix mat[][] of size n x m, and your task is to return an array while traversing the matrix in spiral form.

Examples:

Input: mat[][] = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
Explanation: 

Input: mat[][] = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]
Output: [1, 2, 3, 4, 5, 6, 12, 18, 17, 16, 15, 14, 13, 7, 8, 9, 10, 11]
Explanation: Applying same technique as shown above.
Input: mat[][] = [[32, 44, 27, 23], [54, 28, 50, 62]]
Output: [32, 44, 27, 23, 62, 50, 28, 54]
Explanation: Applying same technique as shown above, output will be [32, 44, 27, 23, 62, 50, 28, 54].
Constraints:
1 <= n, m <= 1000
0 <= mat[i][j]<= 100
'''


class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        if not mat or not mat[0]:
            return []
    
        result = []
        top, bottom = 0, len(mat) - 1
        left, right = 0, len(mat[0]) - 1
        
        while top <= bottom and left <= right:
            # Traverse from left to right along the top row
            for col in range(left, right + 1):
                result.append(mat[top][col])
            top += 1

            # Traverse from top to bottom along the right column
            for row in range(top, bottom + 1):
                result.append(mat[row][right])
            right -= 1
    
            # Traverse from right to left along the bottom row, if it exists
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(mat[bottom][col])
                bottom -= 1
    
            # Traverse from bottom to top along the left column, if it exists
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(mat[row][left])
                left += 1

        return result