class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


stack = Stack()

print(stack.is_empty())

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.is_empty())

print(stack.peek())

queue = Queue()

print(queue.is_empty())

queue.enqueue("Один")
queue.enqueue("Два")
queue.enqueue("Три")
queue.enqueue("Четыре")



print(queue.is_empty())
print(queue.size())
print(queue.dequeue())
print(queue.size())
