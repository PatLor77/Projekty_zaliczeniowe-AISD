from typing import Any
class Node:
    def __init__(self, value:Any):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value: Any) -> None:
        if self.head == None:
            o = Node(value)
            self.head = o
            self.tail = o
        else:
            o = Node(value)
            o.next = self.head
            self.head = o

    def append(self, value: Any) -> None:
        if self.head != None:
            o = self.tail
            o.next = Node(value)
            self.tail = o.next
        else:
            self.push(value)

    def node(self, at: int) -> Node:
        if len(self) == 0:
            return False
        if at < 0:
            return False
        if at > len(self)-1:
            return False
        if at == len(self)-1:
            o = self.tail
        if len(self) > at:
            o = self.head
            for x in range(at):
                o = o.next
        return o

    def insert(self, value: Any, after: Node) -> None:
        if after == self.tail:
            self.append(value)
            return
        if after == None:
            return False
        o = Node(value)
        o.next = after.next
        after.next = o

    def pop(self) -> Any:
        if self.head != None:
            o = self.head
            self.head = o.next
            return o.value
        else:
            return False

    def remove_last(self) -> Any:
        o = self.head
        o = self.node(len(self)-3)
        self.tail = o
        o = o.next
        delete = o.next
        o.next = None
        return delete.value

    def remove(self, after: Node) -> Any:
        o = self.head
        if len(self) == 1:
           return False
        if after.next == self.tail:
            delete = self.tail
            self.remove_last()
        else:
            while o.next != after:
                o=o.next
            delete = o.next
            o.next = after.next
        return delete.value

    def __len__(self):
        o = self.head
        count = 0
        while o != None:
            count += 1
            o = o.next
        return count

    def __str__(self):
        display = ""
        o = self.head
        for x in range(len(self)):
            if o.next != None:
                display+=str(o.value)+"->"
            if o.next == None:
                display+=str(o.value)
            o = o.next
        return display

#zadanie 1
print("Zadanie1")
lista = LinkedList()
lista.push(8)
lista.push(9)
lista.push(1)
lista.push(15)
lista.push(5)
lista.append(9)
print(lista.node(2))
lista.insert(2,lista.node(3))
print(lista.pop())
print(lista.remove_last())
lista.remove(lista.node(2))
print(str(lista))
print(len(lista))

class Stack:
    def __init__(self):
       self.storage = LinkedList()

    def push(self, element:Any) -> None:
        self.storage.push(element)

    def pop(self) -> Any:
        if len(self.storage) != 0:
            return self.storage.pop()
        else:
            return False

    def __len__(self):
        return len(self.storage)

    def __str__(self):
        display = ""
        for x in range(len(self.storage)):
            display+=str(self.storage.node(x).value)+"\n"
        return display

#zadanie 2
print("\n"+"Zadanie2")
stack = Stack()
assert len(stack) == 0
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.pop())
print(str(stack))
print(len(stack))

class Queue:
    def __init__(self):
        self.storage = LinkedList()

    def peek(self) -> Any:
        if len(self.storage) != 0:
            return self.storage.tail.value
        else:
            return False

    def enqueue(self, element: Any) -> None:
        self.storage.push(element)

    def dequeue(self) -> Any:
        if len(self.storage) != 0:
            return self.storage.remove_last()
        else:
            return False

    def __len__(self):
        return len(self.storage)

    def __str__(self):
        display = ""
        for x in range(len(self.storage)):
            display += str(self.storage.node(x).value)+" "
        return display

#zadanie 3
print("\n"+"Zadanie 3")
queue = Queue()
assert len(queue) == 0
print(queue.peek())
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
print(queue.peek())
print(queue.dequeue())
print(str(queue))
print(len(queue))