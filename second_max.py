list=[]
num=int(input("enter the length:"))
i=0
while i<num:
    n=int(input("enter the num:"))
    list.append(n)
    list.sort()
    i+=1
print(list[num-2])
