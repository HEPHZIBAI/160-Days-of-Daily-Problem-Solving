'''
You are given an array arr[], containing non-negative integers. Additionally, you have q queries represented as a 2D array queries[][], where each query is of the form [xi , mi].
For each query, your task is to find the maximum bitwise XOR value between xi and any element in arr[] that is less than or equal to mi. In other words, for each query [xi , mi], compute: max( arr[j] XOR xi ) for all j such that arr[j]  ≤  mi .

If there is no element in arr[] that satisfies the condition arr[j]  ≤  mi , then the answer for that query should be -1.
Return an array ans[], where ans[i] represents the result of the i-th query.

Examples:

Input: arr[] = [0, 1, 2, 3, 4], q = 3, queries[][] = [[3, 1], [1, 3], [5, 6]]
Output: [3, 3, 7]
Explanation: 
1. For the query [3, 1]:
   Only elements in arr that are ≤ 1 are 0 and 1.
   3 XOR 0 = 3 and 3 XOR 1 = 2.
   So, the maximum result is 3.
2. For the query [1, 3]:
   Elements ≤ 3 in arr are 0, 1, 2, 3
   1 XOR 2 = 3 gives the highest value.
   So, the maximum result is 3.
3. For the query [5, 6]:
   All elements of arr are ≤ 6.
   5 XOR 2 = 7 gives the highest value.
   So, the maximum result is 7.
Input: arr[] = [5, 2, 4, 6, 6, 3], q = 3, queries[][] = [[12, 4], [8, 1], [6, 3]]
Output: [15, -1, 5]
Explanation:
1. For the query [12, 4]:
    Elements in arr that are ≤ 4 are 2, 4, and 3.
    Maximum result is 12 XOR 3 = 15.
2. For the query [8, 1]:
    There is no element in arr that is ≤ 1.
    So, the result is -1.
3. For the query [6, 3]:
    Elements in arr that are ≤ 3 are 2 and 3.
    Maximum result is 6 XOR 3 = 5.
Constraints:
1 ≤ arr.size(), q ≤ 105
0 ≤ arr[i] , xi , mi ≤ 109
'''

class node:
    def __init__(self):
        self.left=None
        self.right=None
        
class trie:
    def __init__(self):
        self.root=node()
        
    def insert(self,n):
        t=self.root
        
        for i in range(31,-1,-1):
            b=(n>>i)&1
            if b==0:
                if t.left is None:
                    t.left=node()
                t=t.left
                
            else:
                if t.right is None:
                    t.right=node()
                    
                t=t.right
                
    def xorHelper(self,value):
        curr=0
        temp=self.root
        
        for j in range(31,-1,-1):
            bit=(value>>j)&1
            
            if bit==0:
                if temp.right is not None:
                    temp=temp.right
                    curr+=(1<<j)
                else:
                    temp=temp.left
                    
            else:
                if temp.left is not None:
                    temp=temp.left
                    curr+=(1<<j)
                else:
                    temp=temp.right
                    
        return curr

class Solution:
    def maxXor(self, arr, queries):
        n=len(arr)
        q=len(queries)
        ans=[-1]*q
        qry=[]
        arr.sort()
        
        for i in range(q):
            qry.append([queries[i][1],queries[i][0],i])
            
        qry.sort()
        
        j=0
        tree=trie()
        
        for i in range(q):
            
            while j<len(arr) and arr[j]<=qry[i][0]:
                tree.insert(arr[j])
                j+=1
                
            if j==0:
                ans[qry[i][2]]=-1
            else:
                ans[qry[i][2]]=tree.xorHelper(qry[i][1])
                
        return ans