list=['a','b','c','d','e','f','g','h']
i=0
a=[]
while i<len(list):
    j=i
    b=[]
    while j<len(list):
        c=list[j]
        b.append(c)
        j+=3
    a.append(b)
    i+=1
print(a)