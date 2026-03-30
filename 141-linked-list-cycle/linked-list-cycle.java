/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode visiter=head,checker=head;
        while(checker!=null && checker.next!=null){
            visiter=visiter.next;
            checker=checker.next.next;
            if(visiter==checker) return true;
        }
    return false;
    }
}