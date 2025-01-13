'''

You are given two positive integers n and m, and an integer array arr[] containing total (n*m) elements. Return a 2D matrix of dimensions n x m by filling it in a clockwise spiral order using the elements from the given array.

Examples:

Input: n = 4, m = 4, arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
Output: [[1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]]
Input: n = 3, m = 4, arr[] =[1, 8, 6, 3, 8, 6, 1, 6, 3, 2, 5, 3]
Output: [[1, 8, 6, 3],
        [2, 5, 3, 8],
        [3, 6, 1, 6]]
Input: n = 2, m = 2, arr[] =[1, 8, 6, 3]
Output: [[1, 8],
        [3, 6]]
Constraints:
1 ≤ n, m ≤ 103
arr.size() = n x m
1 ≤ arr[i] ≤ 103

'''

class Solution:
    def spiralFill(self, n, m, arr):
        res=[[0 for _ in range(m)] for _ in range(n)]
        t,b,l,r=0,n-1,0,m-1
        i=0
        
        while i<len(arr):
            for j in range(l,r+1):
                res[t][j]=arr[i]
                i+=1
            t+=1
            
            for k in range(t,b+1):
                res[k][r]=arr[i]
                i+=1
            r-=1
            
            if t<=b:
                for j in range(r,l-1,-1):
                    res[b][j]=arr[i]
                    i+=1
                b-=1
            
            if l<=r:
                for k in range(b,t-1,-1):
                    res[k][l]=arr[i]
                    i+=1
                l+=1
                
        return res