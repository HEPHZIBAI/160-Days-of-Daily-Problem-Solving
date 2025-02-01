'''
Given an incomplete Sudoku configuration in terms of a 9x9  2-D interger square matrix, mat[][], the task is to solve the Sudoku. It is guaranteed that the input Sudoku will have exactly one solution.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Note: Zeros represent blanks to be filled with numbers 1-9, while non-zero cells are fixed and cannot be changed.

Examples:

Input: mat[][] = 

Output:

Explanation: Each row, column and 3 x 3 box of the output matrix contains unique numbers.
Input: mat[][] = 

Output:

Explanation: Each row, column and 3 x 3 box of the output matrix contains unique numbers.
Constraints:
mat.size() = 9
mat[i].size() = 9
0 ≤ mat[i][j] ≤ 9

'''

class Solution:
    def is_safe(self,mat,r,c,num,N):
        for i in range(N):
            if mat[r][i]==num or mat[i][c]==num:
                return False
                
        sr,sc=r-r%3,c-c%3
        
        for i in range(3):
            for j in range(3):
                if mat[sr+i][sc+j]==num:
                    return False
                    
        return True
        
    def fec(self,mat,N):
        for r in range(N):
            for c in range(N):
                if mat[r][c]==0:
                    return r,c
                    
        return None
    
    def solveSudoku(self, mat):
        N=len(mat)
        ec=self.fec(mat,N)
        
        if not ec:
            return True
            
        r,c=ec
        
        for i in range(1,10):
            if self.is_safe(mat,r,c,i,N):
                mat[r][c]=i
                
                if self.solveSudoku(mat):
                    return True
                
                mat[r][c]=0
        
        return False