list1=[5,7,19,27,12,16,25,45]
list2=list(set(list1))
print(list2)
list1.remove(max(list1))
print(max(list1))
