# Lab01Queue.py - Timothy Wang
# Implements a Queue using two stacks, one of which has elements reversed from other stack
# Due to having to constantly update stacks after enqueue and dequeue, this is highly inefficient

from random import randint

class Queue:
    """Implements a Queue using two stacks"""
    def __init__(self, n):
        self.stack1 = list()
        self.stack2 = list()
        self.size = 0
        self.MAXIMUM = n
        self.head = None

    def length(self):
        """Returns current amount of elements within queue"""
        return self.size

    def enqueue(self, item):
        """Enqueues object to queue"""
        if self.size < self.MAXIMUM:
            self.stack1 = list(x for x in self.stack2[::-1])
            self.stack1 += [item]
            self.size += 1
            self.stack2 = list(x for x in self.stack1[::-1])
            if self.head is None:
                self.head = self.stack1[-1]
        else:
            print('Overflow')

    def dequeue(self):
        """Dequeues from queue"""
        if self.size > 0:
            self.stack2 = list(x for x in self.stack1[::-1])
            value = self.stack2[-1]
            self.stack2 = self.stack2[:-1]
            self.size -= 1
            self.stack1 = list(x for x in self.stack2[::-1])
            if len(self.stack1) > 0:
                self.head = self.stack1[-1]
            else:
                self.head = None
            return value
        else:
            print('Underflow')

    def get_queue(self):
        """Returns queue contents"""
        return list(x for x in self.stack1)

    def get_size(self):
        """Returns queue size"""
        return self.size

    def get_head(self):
        """Returns head of queue"""
        return self.head
