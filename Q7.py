list=[1, 1, 2, 3, 4, 4, 5, 1]
#[[2, 1], 2, 3, [2, 4], 5, 1]
i=0
new=[]
list2=[]
while i<len(list):
    if list[i]==list[i]:
        new.append(list[i])
        c=(2,new[i])
        if c not in list2:
            list2.append(c)
        i+=1
print(list2)


