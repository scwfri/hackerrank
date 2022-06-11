#!/usr/bin/env python

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    node = head.next
    head.next = None
    while node:
        next = node.next
        node.next = head
        head = node
        node = next

    return head
