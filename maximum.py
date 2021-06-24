list=[]
max=0
num=int(input("enter the length:"))
i=1
while i<=num:   
    list.append(i)
    j=0
    while j<len(list):
        if list[j]>max:
            max=list[j]
        j=j+1
    i+=1
print(list)
print("maximum is",max)