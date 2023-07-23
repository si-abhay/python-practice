#======= Singly Linked List =======#

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class ll:
    def __init__(self):        
        self.head=None

    def print(self):
        current=self.head   
        while(current!=None):
            print(current.data)
            current=current.next
    
    def insert_begin(self,data):                  # insert node at beginning
        new=node(data)
        new.next=self.head
        self.head=new

    def insert_end(self,data):                     # insertion at end
        new=node(data)
        if self.head is None:
            self.head=new
            return
        current=self.head
        while(current.next!=None):
            current=current.next
        current.next=new

    def insert_mid(self,mid,data):              # insert AFTER given node if present
        if mid is None:
            print("No such node")
            return
        new=node(data)
        new.next=mid.next
        mid.next=new
    
    def insert_pos(self, data, position):

        new = node(data)

        if position == 0:
            # Insert at the beginning of the list
            new.next = self.head
            self.head = new
        else:
            current = self.head
            for i in range(position - 1):
                current = current.next

            new.next = current.next
            current.next = new



list=ll()        

first=node(1)
second=node(2)
third=node(3)

list.head=first              
first.next=second
second.next=third
list.insert_begin(0)
list.insert_end(4)
list.insert_mid(third,3.5)
list.insert_pos(2.5,3)              # index at which you want to add
list.print()           