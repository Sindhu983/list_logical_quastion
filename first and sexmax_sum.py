list=[12,47,87,98,45,2,56]
max=0
sec=0
i=0
while i<len(list):
    if list[i]>max:
        max=list[i]
    i+=1
    j=0
    while j<len(list):
        if sec<list[j]<max:
            sec=list[j]
        j+=1
#print("Maximun number is ",max)
print("Second maximun number is",sec)
#print("sum of max and sec max :",max+sec)
