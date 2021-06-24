list=[2,3,4,5,6,7,8]
i=0
while i<len(list):
    if list[i]%2==0:
        print(list[i]**2)
    else:
        print(list[i]**3)
    i+=1