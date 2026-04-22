class Queue:
    def __init__(self):
        self.q = []
    
    def enqueue(self,e):
        self.q.append(e)
    def dequeue(self):
        try:
            return self.q.pop(0)
        except IndexError:
            raise IndexError
    def first(self):
        try:
            return self.q[0]
        except IndexError:
            raise IndexError
    def is_empty(self):
        return len(self.q) == 0
    def __len__(self):
        return len(self.q)