#======= Singly Linked List =======#

class node:
    def __init__(self,data):        #constructor
        self.data=data
        self.next=None

class ll:
    def __init__(self):             #constructor
        self.head=None

    def print(self):
        temp=self.head      #basically temp is a temp node type which is first node now
        while(temp!=None):
            print(temp.data)
            temp=temp.next


list=ll()                           # create a linked list

first=node(1)
second=node(2)
third=node(3)

list.head=first              # head -> first    use list.head not ll.head
first.next=second
second.next=third

list.print()                #list.print() not ll.print()