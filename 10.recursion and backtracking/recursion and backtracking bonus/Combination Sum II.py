'''
Given an array arr[] and a target, your task is to find all unique combinations in the array where the sum is equal to target. Each number in arr[] may only be used once in the combination.

You can return your answer in any order.

Examples:

Input: arr[] = [1, 2, 3, 3, 5], target =7
Output: [[1, 3, 3], [2, 5]]
Explanation: Total number of possible combinations are 2.
Input: arr[] = [5, 10, 15, 20, 25, 30], target = 30
Output: [[5, 10, 15], [5, 25], [10, 20], [30]]
Explanation: Total number of possible combinations are 4.
Input: arr[] = [6, 5, 7], target = 8
Output: []
Explanation: There are no possible combinantions such that target sum is 8.
Constraints:
1 <= arr.size() <= 100
1 <= arr[i] <= 50
1 <= target <= 30

'''

class Solution:
    def uniqueCombinations(self, arr, target):
        def bt(s,p,t):
            if t==target:
                result.append(list(p))
                return
            
            if t>target:
                return
            
            for i in range(s,len(arr)):
                if i>s and arr[i]==arr[i-1]:
                    continue
                
                p.append(arr[i])
                bt(i+1,p,t+arr[i])
                p.pop()
                
        arr.sort()
        result=[]
        bt(0,[],0)
        return result