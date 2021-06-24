# list=[[1,2,3],[4,5,6]]
# new=[]
# i=0
# j=0
# sum=0
# while i<len(list)-1:
#     j=0
#     while j<len(list[i]):
#         sum=(list[i][j])+(list[i+1][j])
#         new.append(sum)
#         j+=1
#     i+=1
# print(new)

list=[[1,2,3],[4,5,6],[7,8,9]]
new=[]
i=0
sum=0
while i<len(list)-1:
    j=0
    while j<len(list[i]):
        k=0
        while k<len(list[i])-3:
            sum=(list[i][0]+list[i+1][j]+list[i+2][k])
            new.append(sum)
            k+=1
        j+=1
    i+=1
print(new)

    

    