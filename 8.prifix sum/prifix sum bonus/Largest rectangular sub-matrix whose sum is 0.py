'''

Given a matrix mat[][]. Find the size of the largest sub-matrix whose sum is equal to zero. The size of a matrix is the product of rows and columns. A sub-matrix is a matrix obtained from the given matrix by deletion of several (possibly, zero or all) rows/columns from the beginning and several (possibly, zero or all) rows/columns from the end.

Examples:

Input: mat[][] = [[9, 7, 16, 5], [1, -6, -7, 3], [1, 8, 7, 9], [7, -2, 0, 10]] 
Output: 6
Explanation: 

Input: mat[][] =  [[1, 2, 3], [-3, -2, -1], [1, 7, 5]]
Output:  6
Explanation:

Input: mat[][] = [[1, -1], [-1, 1]]
Output: 4
Explanation: The largest sub-matrix with sum 0 is [[1, -1], [-1, 1]].
Constraints:
1 <= mat.size(), mat[0].size() <= 100
-1000 <= mat[][] <= 1000

'''

from typing import List

class Solution:
    def zeroSumSubmat(self, mat):
        r,c=len(mat),len(mat[0])
        ms=0
        
        for i in range(r):
            cs=[0]*c
            
            for j in range(i,r):
                for k in range(c):
                    cs[k]+=mat[j][k]
                     
                ps=0
                pm={0:-1}
                
                for k in range(c):
                    ps+=cs[k]
                    
                    if ps in pm:
                        w=k-pm[ps]
                        h=j-i+1
                        ms=max(ms,w*h)
                    else:
                        pm[ps]=k
                
        return ms