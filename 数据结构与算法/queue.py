# coding:utf-8
class Queue(object):
    """队列"""
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        """进队列"""
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
if __name__ == "__main__":
    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
