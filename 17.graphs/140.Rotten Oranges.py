'''
Given a matrix mat[][] of dimension n * m where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cell have fresh oranges
2 : Cell have rotten oranges

We have to determine what is the earliest time after which all the oranges are rotten. A rotten orange at index (i, j) can rot other fresh orange at indexes (i-1, j), (i+1, j), (i, j-1), (i, j+1) (up, down, left and right) in a unit time.

Note: Your task is to return the minimum time to rot all the fresh oranges. If not possible returns -1.

Examples:

Input: mat[][] = [[0, 1, 2], [0, 1, 2], [2, 1, 1]]
Output: 1
Explanation: Oranges at positions (0,2), (1,2), (2,0) will rot oranges at (0,1), (1,1), (2,2) and (2,1) in unit time.
Input: mat[][] = [[2, 2, 0, 1]]
Output: -1
Explanation: Oranges at (0,0) and (0,1) can't rot orange at (0,3).
Input: mat[][] = [[2, 2, 2], [0, 2, 0]]
Output: 0
Explanation: There is no fresh orange. 
Constraints:
1 ≤ mat.size() ≤ 500
1 ≤ mat[0].size() ≤ 500
mat[i][j] = {0, 1, 2} 



'''


from collections import deque

class Solution:
	def orangesRotting(self, mat):
        if not mat or not mat[0]:
            return -1
            
        r,c=len(mat),len(mat[0])
        queue=deque()
        fc=0
        
        for i in range(r):
            for j in range(c):
                if mat[i][j]==2:
                    queue.append((i,j,0))
                elif mat[i][j]==1:
                    fc+=1
        
        if fc==0:
            return 0
            
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        tt=0
        
        while queue:
            x,y,time=queue.popleft()
            tt=max(tt,time)
            
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                
                if 0<=nx<r and 0<=ny<c and mat[nx][ny]==1:
                    mat[nx][ny]=2
                    fc-=1
                    queue.append((nx,ny,time+1))
                    
        return tt if fc==0 else -1