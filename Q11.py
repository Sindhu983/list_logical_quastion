list1=[1,2,3,4,5,6]
i=0
new=[]
while i<len(list1)-1:
    c=list1[i],list1[i+1] # c=list1[i+1],list1[i]
    d=list(c)
    new.append(d)
    i+=1
print(new)

