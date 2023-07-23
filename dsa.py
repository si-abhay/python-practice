#======= Singly Linked List =======#

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class ll:
    def __init__(self):        
        self.head=None

    def print(self):
        temp=self.head    
        while(temp!=None):
            print(temp.data)
            temp=temp.next

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev



list=ll()  

first=node(1)
second=node(2)
third=node(3)

list.head=first        
first.next=second
second.next=third

list.reverse()   
list.print()          