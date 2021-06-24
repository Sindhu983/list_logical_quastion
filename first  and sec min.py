# num=int(input('enter the length'))
# i=0
# min=0
# sec=0
# list=[]
# while i<num:
#     n=int(input('enter the number '))
#     list.append(n)
#     if list[i]<min:
#         min=list[i]
#     i+=1
#     # j=0
#     # while j<len(list):
#     #     if min<list[j]<sec:
#     #         sec=list[i]
#     #     j+=1
# print(min)


list=[12,47,87,98,45,2,56]
min=list[0]
sec=list[1]
i=0
while i<len(list):
    if list[i]<min:
        sec=min
        min=list[i]
    elif min<list[i]<sec:
        sec=list[i]
    i+=1

print("minimum is :",min)
print("second minimum is :",sec)

    