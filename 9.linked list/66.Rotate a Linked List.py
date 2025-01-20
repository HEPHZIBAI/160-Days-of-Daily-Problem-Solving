'''
Given the head of a singly linked list, your task is to left rotate the linked list k times.

Examples:

Input: head = 10 -> 20 -> 30 -> 40 -> 50, k = 4
Output: 50 -> 10 -> 20 -> 30 -> 40
Explanation:
Rotate 1: 20 -> 30 -> 40 -> 50 -> 10
Rotate 2: 30 -> 40 -> 50 -> 10 -> 20
Rotate 3: 40 -> 50 -> 10 -> 20 -> 30
Rotate 4: 50 -> 10 -> 20 -> 30 -> 40

Input: head = 10 -> 20 -> 30 -> 40 , k = 6
Output: 30 -> 40 -> 10 -> 20 
 
Constraints:

1 <= number of nodes <= 105
0 <= k <= 109
0 <= data of node <= 109

'''

class Solution {
    public Node rotate(Node head, int k) {
        if(head==null || head.next==null || k==0)
            return head;
            
        Node tail=head;
        int l=1;
        
        while(tail.next!=null)
        {
            tail=tail.next;
            l+=1;
        }
        
        k%=l;
        
        if(k==0)
            return head;
            
        Node nt=head;
        
        for(int i=1;i<k;i++)
            nt=nt.next;
            
        Node nh=nt.next;
        
        nt.next=null;
        tail.next=head;
        
        return nh;
    }
}