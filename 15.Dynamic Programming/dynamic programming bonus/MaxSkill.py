'''
You are given a queue of n people indexed from 0 to n-1. Each person has a rating represented by an array arr[]. You are asked to remove all the persons from the queue. If you remove the i-th person from the queue, you gain a skill value of arr[i - 1] * arr[i] * arr[i + 1]. Return the maximum total skill you can obtain by removing the people optimally.

Note: If i - 1 or i + 1 is out of bounds, assume there is an implicit person with a rating of 1 at that position.

Examples:

Input: arr[] = [5, 10] 
Output: 60
Explanation:
Remove person with rating 5 → Skill gained = 1 * 5 * 10 = 50, remaining queue: [10].
Remove person with rating 10 → Skill gained = 1 * 10 * 1 = 10, total skill = 50 + 10 = 60.
Input: arr[] = [3, 2, 5, 8]
Output: 182
Explanation:
Remove person with rating 2 → Skill gained = 3 * 2 * 5 = 30, remaining queue: [3, 5, 8].
Remove person with rating 5 → Skill gained = 3 * 5 * 8 = 120, remaining queue: [3, 8].
Remove person with rating 3 → Skill gained = 1 * 3 * 8 = 24, remaining queue: [8].
Remove person with rating 8 → Skill gained = 1 * 8 * 1 = 8, total skill = 30 + 120 + 24 + 8 = 182
Constraints:
1 ≤ n ≤ 300
0 ≤ arr[i] ≤ 100


'''
class Solution:
    def maxSkill(self, arr):
        n=len(arr)
        arr=[1]+arr+[1]
        dp=[[0]*(n+2) for _ in range(n+2)]
        
        for i in range(1,n+1):
            for j in range(1,n-i+2):
                r=j+i-1
                
                for k in range(j,r+1):
                    skill=arr[j-1]*arr[k]*arr[r+1]
                    ts=skill+dp[j][k-1]+dp[k+1][r]
                    dp[j][r]=max(dp[j][r],ts)
                    
        return dp[1][n]

