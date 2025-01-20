/*

Given the head of a linked list, the task is to reverse this list and return the reversed head.

Examples:

Input: head: 1 -> 2 -> 3 -> 4 -> NULL
Output: head: 4 -> 3 -> 2 -> 1 -> NULL
Explanation:

Input: head: 2 -> 7 -> 10 -> 9 -> 8 -> NULL
Output: head: 8 -> 9 -> 10 -> 7 -> 2 -> NULL
Explanation:

Input: head: 10 -> NULL
Output: 10 -> NULL
Explanation:

Constraints:
1 <= number of nodes, data of nodes <= 105

*/

class Solution 
{
    Node reverseList(Node head) 
    {
        Node p=null;
        Node c=head;
        
        while(c!=null)
        {
            Node nn=c.next;
            c.next=p;
            p=c;
            c=nn;
        }
        return p;
        
    }
}
