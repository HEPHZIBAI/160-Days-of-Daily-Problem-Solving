'''
Given a string s consisting of opening and closing parenthesis '(' and ')'. Find the length of the longest valid parenthesis substring.

A parenthesis string is valid if:

For every opening parenthesis, there is a closing parenthesis.
The closing parenthesis must be after its opening parenthesis.
Examples :

Input: s = "((()"
Output: 2
Explanation: The longest valid parenthesis substring is "()".
Input: s = ")()())"
Output: 4
Explanation: The longest valid parenthesis substring is "()()".
Input: s = "())()"
Output: 2
Explanation: The longest valid parenthesis substring is "()".
Constraints:
1 ≤ s.size() ≤ 106  
s consists of '(' and ')' only



'''


class Solution:
    def maxLength(self, s):
        max_length, open_count, close_count = 0, 0, 0

        for ch in s:
            if ch == '(':
                open_count += 1
            else:
                close_count += 1
            if open_count == close_count:
                max_length = max(max_length, 2 * close_count)
            elif close_count > open_count:
                open_count, close_count = 0, 0

        open_count, close_count = 0, 0
        for ch in reversed(s):
            if ch == ')':
                close_count += 1
            else:
                open_count += 1
            if open_count == close_count:
                max_length = max(max_length, 2 * open_count)
            elif open_count > close_count:
                open_count, close_count = 0, 0

        return max_length
