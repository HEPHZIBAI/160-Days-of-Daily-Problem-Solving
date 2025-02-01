'''
You are given a two-dimensional mat[][] of size n*m containing English alphabets and a string word. Check if the word exists on the mat. The word can be constructed by using letters from adjacent cells, either horizontally or vertically. The same cell cannot be used more than once.

Examples :

Input: mat[][] = [['T', 'E', 'E'], ['S', 'G', 'K'], ['T', 'E', 'L']], word = "GEEK"
Output: true
Explanation:

The letter cells which are used to construct the "GEEK" are colored.
Input: mat[][] = [['T', 'E', 'U'], ['S', 'G', 'K'], ['T', 'E', 'L']], word = "GEEK"
Output: false
Explanation:

It is impossible to construct the string word from the mat using each cell only once.
Input: mat[][] = [['A', 'B', 'A'], ['B', 'A', 'B']], word = "AB"
Output: true
Explanation:

There are multiple ways to construct the word "AB".
Constraints:
1 ≤ n, m ≤ 100
1 ≤ L ≤ n*m
'''

class Solution:
	def isWordExist(self, mat, word):
		if not mat:
		    return False
		    
	    rr,cc=len(mat),len(mat[0])
	    
	    def dfs(r,c,i):
	        if i==len(word):
	            return True
	       
	        if r<0 or r>=rr or c<0 or c>=cc or mat[r][c]!=word[i]:
	            return False
	            
	        temp=mat[r][c]
	        mat[r][c]='#'
	        
	        found=(dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
	        mat[r][c]=temp
	        
	        return found
	   
	    for i in range(rr):
	        for j in range(cc):
	            if mat[i][j]==word[0] and dfs(i,j,0):
	                return True
	                
	    return False