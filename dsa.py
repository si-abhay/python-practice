queue=[]

def empty(queue):
    return len(queue)==0

def enqueue(queue,ele):
    #queue.append(ele)
    queue.insert(0,ele)             # for queue insertion at front(left end) and pop from right end
    return queue

def dequeue(queue):
    if empty(queue):
        return
    #return queue.pop(0)             #here pop(0)
    return queue.pop()

def len_q(queue):
    return len(queue)

enqueue(queue,1)
enqueue(queue,2)
enqueue(queue,3)
print(queue)
print(dequeue(queue))
print(len_q(queue))