def heap_max(list,value):
    n=len(list)
    list.append(value)
    i=n                  # since indexing is from 1 , 0th element is considered as garbage
    while(i>1):
        parent = i//2             # // is floor division
        if list[parent] < list[i]:
            list[i],list[parent]=list[parent],list[i]
            i=parent
        else:
            return

#l=["m",50,30,40,10,5,20,30]
#heap_max(l,60)
l=['m', 60, 50, 40, 30, 5, 20, 30, 10]
heap_max(l,45)
print(l)