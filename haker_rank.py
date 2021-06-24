# num=int(input("enter the number :"))
# if num%2==0:
#     print("weird")
# elif 2<=num<=5:
#     print("not weird")
# elif 6<=num<=20:
#     print("weird")
# elif num%2==0 and num>=20:
#     print("not weird")


n=int(input("enter the num :"))
if n%2!=0:
    print("weird")
elif n%2==0 and n>=2 and n<=5:
    print("not weird")
elif n%2==0 and n>=6 and n<=20:
    print("weird")
elif n>20:
    print("not weird")