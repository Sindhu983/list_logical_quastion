user=input("enter the input :")
a=list(user)
counsonent_count=0
vowel_count=0
i=0
while i<len(a):
    if a[i]!='':
        if a[i]=='a' or a[i]=='i' or a[i]=='e' or a[i]=='u' or a[i]=='o' or a[i]=='A' or a[i]=='E' or a[i]=='I' or a[i]=='O' or a[i]=='U':
            vowel_count+=1
        else:
            counsonent_count+=1
        i+=1
print("consonents:",counsonent_count)
print("vowel:",vowel_count)