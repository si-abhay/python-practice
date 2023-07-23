class node():
    def __init__(self,data):
        self.data=data
        self.next=None

class ll():
    def __init__(self):
        self.head=None
    
    def middle(self):
        current=self.head
        count=0
        while(current is not None):
            count+=1
            current=current.next
        mid=(count//2)+1
        mid-=1

        current=self.head               # re initialise to start
        while(mid>0):
            mid-=1
            current=current.next

        return current



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

