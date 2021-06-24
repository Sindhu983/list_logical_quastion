user=input("enter the input :")
user2=list(user)
list=[]
new=''
i=0
while i<len(user2):
    if user2[i]=='':
        new=''
    else:
        new=new+user[i]
    i+=1
list.append(new)
print(list)


        
        


    
