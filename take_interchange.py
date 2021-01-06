t1=tuple()
t2=tuple()
for i in range(1):
    a1=input("Enter a value : ")
    a2=input("Enter a value : ")
    t1+=(a1,)
    t2+=(a2,)
#print
print("First value : ",t1)
print("Second value : ",t2)
#interchange
t1,t2=t2,t1
print("After interchanging")
print(t1)
print(t2)
#compairing
if t1>t2:
    print(t1," : is greater than : ",t2)
elif t2>t1:
    print(t2," : is greater than : ",t1)
else:
    print(t1, " : is equal to :",t2)
