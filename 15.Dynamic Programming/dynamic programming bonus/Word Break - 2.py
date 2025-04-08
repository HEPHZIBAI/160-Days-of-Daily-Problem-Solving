'''
Given a string s and a dictionary dict[] of valid words, you need to return all possible ways to break the string s into sentence such that each word in the sentence is a valid dictionary word.
You are allowed to use a valid word multiple times in the sentence.

Examples:

Input: s = "likegfg", dict[] = ["lik", "like", "egfg", "gfg"]
Output: 
"lik egfg"
"like gfg"
Explanation: All the words in the given sentences are present in the dictionary.
Input: s = "geeksforgeeks", dict[] = ["for", "geeks"]
Output: "geeks for geeks"
Explanation: The string "geeksforgeeks" can be broken into valid words from the dictionary in one way.
Constraints:
1 ≤ dict.size() ≤ 20
1 ≤ dict[i] ≤ 15
1 ≤ s.size() ≤ 500

'''


class Solution:
    def wordBreak(self, dict, s):
        st=set(dict)
        n=len(s)
        dp=[[] for _ in range(n+1)]
        
        dp[n].append("")
        
        for i in range(n-1,-1,-1):
            for j in range(i+1,n+1):
                word=s[i:j]
                
                if word in st:
                    for sub in dp[j]:
                        if sub:
                            dp[i].append(word+" "+sub)
                        else:
                            dp[i].append(word)
                            
        return dp[0]