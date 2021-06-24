a=[1,2,3,4,5,6,7,8,9,10]
b=[]
n=int(input("enter the sze of the list :"))
i=0
while i<len(a):
    j=0
    c=[]
    while j<n:
        d=i+j
        c.append(d)
        j+=1
    i+=1
    b.append(c)
print(b)