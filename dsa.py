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
    
    def insert(self,data):                  # insert node at beginning
        new=node(data)
        new.next=self.head
        self.head=new



list=ll()        

first=node(1)
second=node(2)
third=node(3)

list.head=first              
first.next=second
second.next=third

list.insert(0)
list.print()           