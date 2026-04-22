class Stack:
    def __init__(self):
        self.stackList = []
    
    def push(self, e):
        self.stackList.append(e)
    
    def pop(self):
        return self.stackList.pop()
    def top(self):
        if len(self.stackList) != 0:
            return self.stackList[-1]
        else:
            return "Error"
    def is_empty(self):
        return len(self.stackList) == 0
    def __len__(self):
        return len(self.stackList)