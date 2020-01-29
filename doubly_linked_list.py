class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.next = None
            new_node.prev = cur
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
    def add_after_node(self, key, data):
        """
        Add new node after an existed node based on the given key.
        :param key:
        :param data:
        :return:
        """
        cur = self.head
        while cur:
            if cur.data == key:
                if cur.next is None:
                    self.append(data)
                    return
                new_node = Node(data)
                new_node.next = cur.next
                cur.next.prev = new_node
                cur.next = new_node
                new_node.prev = cur
                return
            else:
                cur = cur.next
    def add_before_node(self, key, data):
        """
        Add new node before an existed node based on the given key.
        :param key:
        :param data:
        :return:
        """
        cur = self.head
        while cur:
            if cur.data == key:
                if cur.next is None:
                    self.append(data)
                    return
                new_node = Node(data)
                cur.prev.next = new_node
                new_node.prev = cur.prev
                cur.prev = new_node
                new_node.next = cur
                return
            else:
                cur = cur.next
    def delete(self, key):
        """
        Four cases:
            1. Deleting the only exist node
            2. Deleting Head node
            3. Deleting node other than head where cur.next is not None
            4. Deleting node other than head where cur.next is None
        :param key:
        :return:
        """
        cur = self.head
        while cur:
            if cur.data == key:
                if cur.prev is None and cur.next is None:
                    self.head = None
                    cur = None
                    return
                if cur.prev is None:
                    cur.next.prev = None
                    self.head = cur.next
                    cur = None
                    return
                if cur.next is None:
                    cur.prev.next = None
                    cur = None
                    return
                else:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    cur = None
                    return
            else:
                cur = cur.next
    def reverse(self):
        temp = None
        cur = self.head
        while cur:
            temp = cur.prev
            cur.prev = cur.next
            cur.next = temp
            cur = cur.prev
        if temp:
            self.head = temp.prev


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(0)
dllist.add_after_node(2,5)
dllist.add_before_node(2,6)
dllist.delete(1)
dllist.delete(0)
dllist.delete(4)
dllist.delete(2)
dllist.delete(6)
dllist.delete(5)
dllist.delete(3)
dllist.print_list()

# Exercise
# 1. Solution for remove duplicates

# 2. Solution for Pairs and Sums Quiz

