str1 = "I do you do and we all will do" # do replace with done
a=str1.split()
i=0
b=' '
while i<len(a):
    if a[i]=="do":
        b=b+'does'+' '
    else:
        b=b+a[i]+' '
    i+=1
print(b)
