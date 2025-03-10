'''
Given a string s, count all palindromic sub-strings present in the string. The length of the palindromic sub-string must be greater than or equal to 2. 

Examples

Input: s = "abaab"
Output: 3
Explanation: All palindromic substrings are : "aba" , "aa" , "baab".
Input: s = "aaa"
Output: 3
Explanation: All palindromic substrings are : "aa", "aa", "aaa".
Input: s = "abbaeae"
Output: 4
Explanation: All palindromic substrings are : "bb" , "abba" , "aea", "eae".
Constraints:
2 ≤ s.size() ≤ 103
string contains only lowercase english characters



'''
class Solution:

    def countPS(self, s):
        n=len(s)
        count=0
        
        def eac(left,right):
            nonlocal count
            while left>=0 and right<n and s[left]==s[right]:
                if right-left+1>=2:
                    count+=1
                left-=1
                right+=1
                
        for i in range(n):
            eac(i,i)
            if i+1<n:
                eac(i,i+1)
                
        return count

