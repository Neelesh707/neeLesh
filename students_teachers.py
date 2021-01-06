d1=dict()
n=int(input("Enter no. of classes : "))
for i in range(n):
    c=input("Enter class name : ")
    t=input("Enter class teacher name : ")
    d1[c]=t
l=d1.keys()
x=input("Enter class name to be searched : ")
for i in l:
    if i==x:
        print(x," : class teacher is : ",d1[i])
        break
    else:
        print("There is no class with this name")
