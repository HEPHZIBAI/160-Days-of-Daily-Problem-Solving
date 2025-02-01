'''

The n-queens puzzle is the problem of placing n queens on a (n × n) chessboard such that no two queens can attack each other. Note that two queens attack each other if they are placed on the same row, the same column, or the same diagonal.

Given an integer n, find all distinct solutions to the n-queens puzzle.
You can return your answer in any order but each solution should represent a distinct board configuration of the queen placements, where the solutions are represented as permutations of [1, 2, 3, ..., n]. In this representation, the number in the ith position denotes the row in which the queen is placed in the ith column.
For eg. below figure represents a chessboard [3 1 4 2].



Examples:

Input: n = 1
Output: [1]
Explaination: Only one queen can be placed in the single cell available.
Input: n = 4
Output: [[2 4 1 3 ] [3 1 4 2 ]]
Explaination: There are 2 possible solutions for n = 4.
Input: n = 2
Output: []
Explaination: There are no possible solutions for n = 2.
Constraints:
1 ≤ n ≤ 10



'''


class Solution:
    def nQueen(self, n):
        def is_safe(q,r,c):
            for i in range(c):
                if q[i]==r or abs(q[i]-r)==abs(i-c):
                    return False
            return True
            
        def backtrack(c,q):
            if c==n:
                results.append(q[:])
                return
            
            for i in range(1,n+1):
                if is_safe(q,i,c):
                    q[c]=i
                    backtrack(c+1,q)
                    q[c]=0
                    
        results=[]
        backtrack(0,[0]*n)
        return results