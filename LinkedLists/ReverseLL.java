/*

For Linked list problems, only solved in Leet code no linked list implemention 
as that is a time sink

https://leetcode.com/problems/reverse-linked-list


Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?



*/

public class ReverseLL {



    public ListNode reverseList(ListNode head){

        ListNode prev = null;
        ListNode curr = head;
        
        while(curr != null){
            ListNode temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;

        }

        return prev;

    }

    public ListNode reverseListRecursive(ListNode head){

        if (head == null || head.next == null) return head;
        ListNode prev = reverseListRecursive(head.next);
        head.next.next = head;
        head.next = null;
        return prev;



    }

    private class ListNode {
        int value;
        ListNode next;

        ListNode(){}
        ListNode(int val){this.val = value;}
        ListNode(int val, ListNode next){this.val = val; this.next = next;}
    }
    
}
