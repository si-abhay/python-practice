def heap_max_del(l):
    n=len(l)
    i=0
    l[0]=l.pop()
    n-=1

    while i < n:
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2

        if left_idx < n:
            left = l[left_idx]
        else:
            left = float('-inf')  # Negative infinity if left child doesn't exist

        if right_idx < n:
            right = l[right_idx]
        else:
            right = float('-inf')  # Negative infinity if right child doesn't exist

        larger_idx = left_idx if left > right else right_idx

        if l[i] < l[larger_idx]:
            l[i], l[larger_idx] = l[larger_idx], l[i]
            i = larger_idx
        else:
            break

l=[40,30,10,20,15]
heap_max_del(l)
print(l)
