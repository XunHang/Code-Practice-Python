class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 借助第三个 list 来将两个有序 list 合并
    def mergeTwoLists(self, l1, l2):
        # l1, l2 中有一个为空时，返回非空的
        if None in (l1, l2):
            return l1 or l2

        lr = ListNode(0)
        lr_buffer = lr
        while l1 and l2:
            if l1.val < l2.val:
                lr.next = l1
                l1 = l1.next
            else:
                lr.next = l2
                l2 = l2.next
            lr = lr.next
        lr.next = l1 if l1 else l2
        return lr_buffer.next

    # 将两个 list 直接合并，不开辟新的空间
    def mergeTwoLists_better(self, l1, l2):
        if None in (l1, l2):
            return l1 or l2
        dummy = cur = ListNode(0)
        dummy.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                tmp = l2.next
                cur.next = l2
                l2.next = l1
                l2 = tmp
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next


slt = Solution()
# l1 = ListNode(1)
# l1_1 = ListNode(2)
# l1_2 = ListNode(4)
# l1.next = l1_1
# l1_1.next = l1_2
# l2 = ListNode(1)
# l2_1 = ListNode(3)
# l2_2 = ListNode(4)
# l2.next = l2_1
# l2_1.next = l2_2

l1 = ListNode(1)
l1.next = ListNode(9)
l2 = ListNode(7)
l2.next = ListNode(8)

result = slt.mergeTwoLists_better(l1, l2)
print(result.val, result.next.val, result.next.next.val,
      result.next.next.next.val)
