def sum_str(a,b):
  if a=="" and b=="":
    return str(0)
  elif a!="" and b=="":
    return a
  elif a=="" and b!="":
    return b
  else:
    sum=int(a)+int(b)
    c=str(sum)
  return c
a=(input("enter the number :"))
b=(input("enter the numbrer :"))
print(sum_str(a,b))