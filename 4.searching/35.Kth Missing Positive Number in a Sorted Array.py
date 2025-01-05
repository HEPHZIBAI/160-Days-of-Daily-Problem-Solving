'''

Given a sorted array of distinct positive integers arr[], we need to find the kth positive number that is missing from arr[].  

Examples :

Input: arr[] = [2, 3, 4, 7, 11], k = 5
Output: 9
Explanation: Missing are 1, 5, 6, 8, 9, 10… and 5th missing number is 9.
Input: arr[] = [1, 2, 3], k = 2
Output: 5
Explanation: Missing are 4, 5, 6… and 2nd missing number is 5.
Input: arr[] = [3, 5, 9, 10, 11, 12], k = 2
Output: 2
Explanation: Missing are 1, 2, 4, 6… and 2nd missing number is 2.
Constraints:
1 <= arr.size() <= 105
1 <= k <= 105
1 <= arr[i]<= 106

'''


#User function Template for python3
class Solution:
    def kthMissing(self, arr, k):
        # We start with the first missing number being 1.
        missing_count = 0
        prev = 0  # Previous number before the first element in the array
        
        for num in arr:
           
            missing_in_range = num - prev - 1
            if missing_count + missing_in_range >= k:
            
                return prev + (k - missing_count)
            missing_count += missing_in_range
            prev = num
        
        
        return prev + (k - missing_count)
