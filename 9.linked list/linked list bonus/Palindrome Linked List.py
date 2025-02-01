/*
Given a head singly linked list of positive integers. The task is to check if the given linked list is palindrome or not.

Examples:

Input: head: 1 -> 2 -> 1 -> 1 -> 2 -> 1
Output: true
Explanation: The given linked list is 1 -> 2 -> 1 -> 1 -> 2 -> 1 , which is a palindrome and Hence, the output is true.

Input: head: 1 -> 2 -> 3 -> 4
Output: false
Explanation: The given linked list is 1 -> 2 -> 3 -> 4, which is not a palindrome and Hence, the output is false.

Constraints:
1 <= number of nodes <= 105
1 ≤ node->data ≤ 103
*/

class Solution 
{
    static boolean isPalindrome(Node head) 
    {
        if(head==null || head.next==null)
            return true;
            
        Node slow=head,fast=head;
        
        while(fast!=null && fast.next!=null)
        {
            slow=slow.next;
            fast=fast.next.next;
        }
        
        Node secondhalf=reverselist(slow);
        Node secondhalfcopy=secondhalf;
        Node firsthalf=head;
        boolean ispalindrome=true;
        
        while(secondhalf!=null)
        {
            if(firsthalf.data!=secondhalf.data)
            {
                ispalindrome=false;
                break;
            }
            firsthalf=firsthalf.next;
            secondhalf=secondhalf.next;
        }
        reverselist(secondhalfcopy);
        return ispalindrome;
        
    }
    private static Node reverselist(Node head)
    {
        Node prev=null,next=null,current=head;
        while(current!=null)
        {
            next=current.next;
            current.next=prev;
            prev=current;
            current=next;
        }
        return prev;
    }
}

