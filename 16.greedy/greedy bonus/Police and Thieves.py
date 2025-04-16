'''
Given an array arr[], where each element contains either a 'P' for policeman or a 'T' for thief. Find the maximum number of thieves that can be caught by the police. 
Keep in mind the following conditions :

Each policeman can catch only one thief.
A policeman cannot catch a thief who is more than k units away from him.
Examples:

Input: arr[] = [P, T, T, P, T], k = 1
Output: 2
Explanation: Maximum 2 thieves can be caught. First policeman catches first thief and second police man can catch either second or third thief.
Input: arr[] = [T, T, P, P, T, P], k = 2
Output: 3
Explanation: Maximum 3 thieves can be caught.
Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ k ≤ 1000
arr[i] = 'P' or 'T'

'''

def catchThieves(arr, k):
    n=len(arr)
    i,j=0,0
    c=0
    
    while i<n and j<n:
        while i<n and arr[i]!='P':
            i+=1
            
        while j<n and arr[j]!='T':
            j+=1
            
        if i<n and j<n and abs(i-j)<=k:
            c+=1
            i+=1
            j+=1
        elif j<n and j<i:
            j+=1
        elif i<n and i<j:
            i+=1
            
    return c