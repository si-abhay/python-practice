from array import array
l=array('I',[1,2,3,4,5,6])
l.append(11)
l.remove(3)
print(l)

l.reverse()
print(l)

# copying into a new array
new=array(l.typecode,[ele for ele in l])
print(new)