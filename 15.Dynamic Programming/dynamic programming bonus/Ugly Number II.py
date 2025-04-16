'''
Given an integer n,  return the nth ugly number.

An ugly number is a positive integer whose prime factors are limited to 2, 3 and 5.

Examples:

Input: n = 5
Output: 5
Explanation: Ugly Numbers - 1, 2, 3, 4, 5, 6, 8, 9, 10, 12. So, 5th Ugly Number is 5
Input: n = 10
Output: 12
Explanation: 10th Ugly Number is 12
Constraints:
1 ≤ n ≤ 1500

'''

class Solution:
    def uglyNumber(self, n):
        arr=[0]*n
        
        i2=0
        i3=0
        i5=0
        
        m2=2
        m3=3
        m5=5
        
        nn=1
        arr[0]=1
        
        for i in range(1,n):
            nn=min(m2,m3,m5)
            arr[i]=nn
            
            if nn==m2:
                i2+=1
                m2=arr[i2]*2
                
            if nn==m3:
                i3+=1
                m3=arr[i3]*3
                
            if nn==m5:
                i5+=1
                m5=arr[i5]*5
                
        return nn
            