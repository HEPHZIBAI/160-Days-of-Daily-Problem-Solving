'''
Given an array arr[] such that each element is in the range [0, 9] find the minimum possible sum of two numbers formed using the elements of the array. All digits in the given array must be used to form the two numbers. Return a string without leading zeroes.

Examples :

Input: arr[] = [6, 8, 4, 5, 2, 3]
Output: "604"
Explanation: The minimum sum is formed by numbers 358 and 246.
Input: arr[] = [5, 3, 0, 7, 4]
Output: "82"
Explanation: The minimum sum is formed by numbers 35 and 047.
Input: arr[] = [9, 4]
Output: "13"
Explanation: The minimum sum is formed by numbers 9 and 4.
Constraints:
1 ≤ arr.size() ≤ 106
0 ≤ arr[i] ≤ 9


'''

class Solution:
    def an(self,l1,l2):
        i=len(l1)-1
        j=len(l2)-1
        c=0
        res=[]
        
        while i>=0 or j>=0 or c>0:
            total=c
            if i>=0:
                total+=l1[i]
            if j>=0:
                total+=l2[j]
                
            res.append(str(total%10))
            c=total//10
            i-=1
            j-=1
            
        while len(res)>0 and res[-1]=='0':
            res.pop()
            
        res=res[::-1]
        return ''.join(res)
        
    def minSum(self, arr):
        arr.sort()
        l1=[]
        l2=[]
        
        for i in range(len(arr)):
            if i%2==0:
                l1.append(arr[i])
            else:
                l2.append(arr[i])
        return self.an(l1,l2)
