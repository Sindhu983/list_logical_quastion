a=(243543)
b=str(a)
c=list(b)
i=-1
list1=[]
while i>=-len(c):
    list1.append(int(c[i]))
    i-=1
print(list1)
