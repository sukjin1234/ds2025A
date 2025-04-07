class Node:
    def __init__(self,data,link=None):
        self.data = data
        self.link = link

class Stack:
    def __init__(self):
        self.top = None

    def push(self,data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.link = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            return "Stack is empty!"
            #raise IndexError("스택이 비어 있습니다.")
        popped_node = self.top
        self.top = self.top.link
        popped_node.link = None
        return  popped_node.data

s1 = Stack()
print(s1.pop())
s1.push("Data Struct")
s1.push("DataBase")
print(s1.pop())
print(s1.pop())
print(s1.pop())
