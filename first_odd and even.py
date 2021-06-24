a=[9,3,56,20,65,17,13,45,97,346]
i=0
even=[]
odd=[]
while i<len(a):
    if a[i]%2==0:
        even.append(a[i])
        even.sort()
    else:
        odd.append(a[i])
        odd.sort()
    i+=1
print(even[0])
print(odd[0])