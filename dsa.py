class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def create(arr):
    head=None
    last=None

    for i in arr:
        new=node(i)

        if head is None:
            head=new
            last=head
        else:
            last.next=new
            last=new
    
    return head

def printf(head):
    if head is None:
        return
    print(head.data)
    return printf(head.next)

if __name__ == "__main__":
    arr=[1,2,3,4,5]
    start=create(arr)
    printf(start)