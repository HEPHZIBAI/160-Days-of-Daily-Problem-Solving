/*
Given the head of two singly linked lists, return the point where these two linked lists intersect.

Note: It is guaranteed that the intersected node always exists.

Custom Input Format:

head1 contains the nodes before intersection in list1
head2 contains the nodes before intersection in list2
CommonList contains the nodes after intersection of list1 and list2.

Examples:

Input: head1 : 4 -> 4 -> 4 -> 4 -> 4, head2 : 4 -> 4 -> 4
 
Output: 4
Explanation: From the above image, it is clearly seen that the common part is 4 -> 4 whose starting point is 4.
Input: head1 : 4 -> 1 -> 8 -> 4 -> 5, head2 : 5 -> 6 -> 1 -> 8 -> 4 -> 5
 
Output: 8
Explanation: From the above image, it is clearly seen that the common part is 8 -> 4 -> 5 whose starting point is 8.
Constraints:
2 ≤ total number of nodes ≤ 2*105
-104 ≤ node->data ≤ 104
*/


class Intersect 
{
    static Node intersectPoint(Node head1, Node head2) 
    {
        Node ptr1=head1;
        Node ptr2=head2;
        
        while(ptr1!=ptr2)
        {
            ptr1=(ptr1==null)?head2:ptr1.next;
            ptr2=(ptr2==null)?head1:ptr2.next;
        }
        return ptr1;
    }
}