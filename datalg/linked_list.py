class Node:
    def __init__(self, content):
        self.content = content
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        n = 0
        current = self.head

        while current:
            n += 1
            current = current.next
        return n

    def to_python_list(self):
        plist = []
        current = self.head

        while current:
            plist.append(current.content)
            current = current.next
        
        return plist

    def empty(self):
        return self.head == None

    def insert_head(self, content):
        new_head = Node(content)
        new_head.next = self.head
        self.head = new_head

    def insert_tail(self, content):
        current = self.head

        if current == None:
            self.head = Node(content)
        else:
            while current.next:
                current = current.next
            current.next = Node(content)
    
    def insert_nth(self, content, n):
        if (n < 0) or (n > self.__len__()):
            raise "Index out of range"

        if n == 0:
            self.insert_head(content)
        elif n == self.__len__():
            self.insert_tail(content)
        else:
            current = self.head

            for i in range(n-1):
                current = current.next
            new_node = Node(content)
            new_node.next = current.next
            current.next = new_node

    def delete_head(self):
        deleted = self.head
        self.head = self.head.next

        return deleted

    def delete_tail(self):
        current = self.head

        while current.next.next:
            current = current.next
        deleted = current.next
        current.next = None

        return deleted
    
    def delete_nth(self, n):
        if (n < 0) or (n >= self.__len__()):
            raise "Index out of range"

        if n == 0:
            self.delete_head(content)
        elif n == self.__len__() - 1:
            self.delete_tail(content)
        else:
            current = self.head

            for i in range(n-1):
                current = current.next
            deleted = current.next
            current.next = current.next.next

        return deleted
