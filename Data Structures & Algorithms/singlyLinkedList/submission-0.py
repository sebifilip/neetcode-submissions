class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = Node(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        for _ in range(index + 1):
            curr = curr.next
        return curr.val

    def insertAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        self.size += 1
        prev = self.head
        for _ in range(index):
            prev = prev.next
        
        node = Node(val)
        node.next = prev.next
        prev.next = node

    def insertHead(self, val: int) -> None:
        self.insertAtIndex(0, val)

    def insertTail(self, val: int) -> None:
        self.insertAtIndex(self.size, val)

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        
        self.size -= 1
        prev = self.head
        for _ in range(index):
            prev = prev.next
        
        prev.next = prev.next.next
        return True

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
