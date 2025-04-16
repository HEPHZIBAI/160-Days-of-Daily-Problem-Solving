'''
There are n children standing in a line. Each child is assigned a rating value given in the integer array arr[]. You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating than their neighbors get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute.

Note: The answer will always fit into a 32-bit integer.

Examples:

Input: arr[] = [1, 0, 2]
Output: 5
Explanation: Children at index 0 and 2 will get 2 candies each as their rating is higher than index 1, and index 1 will get 1 candy. Thus total candies = 2 + 1 + 2 = 5.
Input: arr[] = [1, 2, 2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively. The third child gets 1 candy because it satisfies the above two conditions.
Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 109

'''


class Solution:
    def minCandy(self, arr):
        n=len(arr)
        t=n
        i=1
        
        while i<n:
            if arr[i]==arr[i-1]:
                i+=1
                continue
            
            peak=0
            
            while i<n and arr[i]>arr[i-1]:
                peak+=1
                t+=peak
                i+=1
                
            if i==n:
                return t
                
            v=0
            
            while i<n and arr[i]<arr[i-1]:
                v+=1
                t+=v
                i+=1
                
            t-=min(peak,v)
            
        return t