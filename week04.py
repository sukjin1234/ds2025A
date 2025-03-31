import random

class Node:
    def __init__(self,data,link=None):
        self.data = data
        self.link = link

# a = Node("abc")
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.link:
            current = current.link
        current.link = Node(data)

    def search(self,target):
        current = self.head
        while current.link:
            if target == current.data:
                return f"{target}을(를) 찾았습니다."
            else:
                current = current.link
        return f"{target}을(를) 찾지 못했습니다."



    def __str__(self):
        result = ""
        current = self.head
        while current is not None:
            #result += str(current.data) + " -> "
            result += f"{current.data} -> "
            current = current.link
        return result + "end"
        #return "Linked list"

ll = LinkedList()
for _ in range(10):
    ll.append(random.randint(1,20))
print(ll)
print(ll.search(10))
# ll = LinkedList()
# ll.append(8)
# ll.append(10)
# ll.append(-10)
# print(ll)
# print(ll.search(9))
# print(ll.search(10))