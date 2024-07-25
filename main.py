def insertion_sort(li):
    for i in range(1, len(li)):
        key = li[i]
        j = i - 1

        while j>=0 and li[j] > key:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = key
    
    return li

print(insertion_sort([5, 4, 3, 2, 1]))