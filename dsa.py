class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class ll:
    def __init__(self):
        ll.head=None
        ll.prev=None            # addition
    
    def printf(self):
        head=self.head
        while head is not None:
            print(head.data)
            head=head.next

    def printb(self):
        temp=self.prev
        while temp is not None:
            print(temp.data)
            temp=temp.prev



list=ll()
first=node(1)
second=node(2)
third=node(3)
fourth=node(4)

list.head=first
first.next=second
second.prev=first
second.next=third
third.prev=second
third.next=fourth

fourth.prev=third
list.prev=fourth

list.printf()
print()
list.printb()