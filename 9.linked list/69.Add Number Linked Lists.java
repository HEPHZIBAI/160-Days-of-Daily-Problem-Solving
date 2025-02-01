/*
Given the head of two singly linked lists num1 and num2 representing two non-negative integers. The task is to return the head of the linked list representing the sum of these two numbers.

For example, num1 represented by the linked list : 1 -> 9 -> 0, similarly num2 represented by the linked list: 2 -> 5. Sum of these two numbers is represented by 2 -> 1 -> 5.

Note: There can be leading zeros in the input lists, but there should not be any leading zeros in the output list.

Examples:

Input: num1 = 4 - > 5, num2 = 3 -> 4 -> 5
Output:  3 -> 9 -> 0
 
Explanation: Given numbers are 45 and 345. There sum is 390.
Input: num1 = 0 -> 0 -> 6 -> 3, num2 = 0 -> 7 
Output: 7 -> 0 
 
Explanation: Given numbers are 63 and 7. There sum is 70.
Constraints:
1 <= size of both linked lists <= 106
0 <= elements of both linked lists <= 9


*/


class Solution 
{
    static Node addTwoLists(Node num1, Node num2) 
    {
        num1=rev(num1);
        num2=rev(num2);
        Node dummy =new Node(0);
        Node current=dummy;
        int carry=0;
        
        while(num1!=null || num2!=null || carry!=0)
        {
            int sum=carry;
            
            if(num1!=null)
            {
                sum+=num1.data;
                num1=num1.next;
            }
            
            if(num2!=null)
            {
                sum+=num2.data;
                num2=num2.next;
            }
            
            carry =sum/10;
            current.next=new Node(sum%10);
            current=current.next;
        }
        Node result=rev(dummy.next);
        result=rlz(result);
        return result;
    }
    private static Node rev(Node head)
    {
        Node prev=null,curr=head;
        
        while(curr!=null)
        {
            Node nn=curr.next;
            curr.next=prev;
            prev=curr;
            curr=nn;
        }
        return prev;
    }
    private static Node rlz(Node head)
    {
        while(head!=null && head.data==0)
            head=head.next;
            
        return head==null?new Node(0):head;
    }
}