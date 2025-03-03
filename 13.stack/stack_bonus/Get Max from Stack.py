'''
Given q queries, You task is to implement the following three functions for a stack:

push(x) – Insert an integer x onto the stack.
pop() – Remove the top element from the stack.
peek() - Return the top element from the stack. If the stack is empty, return -1.
getMax() – Retrieve the maximum element from the stack in O(1) time. If the stack is empty, return -1.
Each query can be one of the following:

1 x : Push x onto the stack.
2 : Pop the top element from the stack.
3: Return the top element from the stack. If the stack is empty, return -1.
4: Return the maximum element from the stack.
Examples:

Input: q = 7, queries = [[1, 2], [1, 3], [3], [2], [4], [1, 1], [4]]
Output: [3, 2, 2]
Explanation: 
push(2): Stack is [2]
push(3): Stack is [2, 3]
peek(): Top element is 3
pop(): Removes 3, stack is [2]
getMax(): Maximum element is 2
push(1): Stack is [2, 1]
getMax(): Maximum element is 2
Input: q = 4, queries = [[1, 4], [1, 2], [4], [3]]
Output: [4, 2]
Explanation: 
push(4): Stack is [4]
push(2): Stack is [4, 2]
getMax(): Maximum element is 4
peek(): Top element is 2
Input: q = 5, queries = [[1, 10], [4], [1, 5], [4], [2]]
Output: [10, 5]
Explanation: 
push(10): Stack is [10]
getMax(): Maximum element is 10
push(5): Stack is [10, 5]
getMax(): Maximum element is 10
pop(): Removes 5, stack is [10]
Constraints:

1 <= q <= 105
0 <= values on the stack <= 109

'''

class Solution:

    def __init__(self):
        self.s=[]
        self.maxele=-1
        
    # Add an element to the top of Stack
    def push(self, x):
        if not self.s:
            self.maxele=x
            self.s.append(x)
        elif x>self.maxele:
            self.s.append(2*x-self.maxele)
            self.maxele=x
        else:
            self.s.append(x)

    # Remove the top element from the Stack
    def pop(self):
        if not self.s:
            return
        top=self.s.pop()
        
        if top>self.maxele:
            self.maxele=2*self.maxele-top

    # Returns top element of Stack
    def peek(self):
        if not self.s:
            return -1
            
        top=self.s[-1]
        return self.maxele if self.maxele<top else top

    # Finds minimum element of Stack
    def getMax(self):
        if not self.s:
            return -1
            
        return self.maxele