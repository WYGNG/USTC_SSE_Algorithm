#include <stdio.h>


struct ListNode {
    int val;
    struct ListNode *next;
};


typedef struct ListNode LN;

struct ListNode *detectCycle(struct ListNode *head) {
    LN* slow = head, * fast = head;
	do {
		if (slow == NULL || fast == NULL || fast -> next == NULL) {
			return NULL;
		}
		fast = fast -> next -> next;
		slow = slow -> next;
	} while (fast != slow);
	LN* node1 = head;
	LN* node2 = slow;
	while (node1 != node2) {
		node1 = node1 -> next;
		node2 = node2 -> next;
	}
	return node1;
}