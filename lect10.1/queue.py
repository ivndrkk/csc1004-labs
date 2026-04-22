class Queue:
    def __init__(self):
        self.q = []
    
    def enqueue(self,e):
        self.q.append(e)
    def dequeue(self):
        if len(self.q) != 0:
            return self.q.pop(0)
        else:
            return "Error"
    def first(self):
        return self.q[0]
    def is_empty(self):
        return len(self.q) == 0
    def __len__(self):
        return len(self.q)