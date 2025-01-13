'''
You are given an integer target and an array arr[]. You have to find number of pairs in arr[] which sums up to target. It is given that the elements of the arr[] are in sorted order.
Note: pairs should have elements of distinct indexes. 

Examples :

Input: arr[] = [-1, 1, 5, 5, 7], target = 6
Output: 3
Explanation: There are 3 pairs which sum up to 6 : {1, 5}, {1, 5} and {-1, 7}.
Input: arr[] = [1, 1, 1, 1], target = 2
Output: 6
Explanation: There are 6 pairs which sum up to 2 : {1, 1}, {1, 1}, {1, 1}, {1, 1}, {1, 1} and {1, 1}.
Input: arr[] = [-1, 10, 10, 12, 15], target = 125
Output: 0
Explanation: There is no such pair which sums up to 4.
Constraints:
-105 <= target <=105
 2 <= arr.size() <= 105
-105 <= arr[i] <= 105
'''

class Solution:
    def countPairs (self, arr, target) : 
        l=0
        r=len(arr)-1
        count=0
        
        while l<r:
            cs=arr[l]+arr[r]
            
            if(cs<target):
                l+=1
            elif cs>target:
                r-=1
            else:
                cnt1=0
                cnt2=0
                e1=arr[l]
                e2=arr[r]
                
                while l<=r and e1==arr[l]:
                    l+=1
                    cnt1+=1
                    
                while l<=r and e2==arr[r]:
                    r-=1
                    cnt2+=1
                    
                if e1==e2:
                    count+=cnt1*(cnt1-1)//2
                    
                else:
                    count+=cnt1*cnt2
    
        
        return count