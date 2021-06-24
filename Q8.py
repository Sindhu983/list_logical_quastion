a=int(input("enter the number :"))
b=int(input("enter the number :"))
c=int(input("enter the number :"))
d=[]
d.append(a)
d.append(b)
d.append(c)
i=0
while i<3:
    j=0
    while j<3:
        k=0
        while k<3:
            if (i!=j & j!=k & k!=i):
                print(d[i],d[j],d[k])
            k+=1
        j+=1
    i+=1