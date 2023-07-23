class node():
    def __init__(self,data):
        self.data=data
        self.next=None

class ll():
    def __init__(self):
        self.head=None
    
    def middle(self):
        slow=self.head
        fast=self.head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        return slow



list=ll()
f=node(1)
s=node(2)
t=node(3)
#fo=node(4)

list.head=f
f.next=s
s.next=t
#t.next=fo

new=list.middle()
print(new.data)

