list=[[1,2,3],[3,2,4]]
i=0
sum=0
mul=1
while i<len(list):
    j=0
    while j<len(list[i]):
        if i==0:
            sum=sum+list[i][j]
        elif i==1:
            mul=mul*list[i][j]
        j+=1
    i+=1
print(sum)
print(mul)