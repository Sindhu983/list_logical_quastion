a=['red','green','blue']
new=[]
i=0
while i<len(a):
    c=a[i].split()
    d=list(c)
    i+=1
    new.append(d)
print(new)
# a=[['red'],['green'],['blue']]
# new=[]
# i=0
# while i<len(a):
#     j=0
#     b=''
#     while j<len(a[i]):
#         b=b+a[i][j]
#         c=list(b)
#         new.append(c)
#         j+=1
#     i+=1
# print(new)