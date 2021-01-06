t=tuple()
n=int(input("Enter no. of entries : "))
for i in range(n):
    a=input("Enter an element : ")
    t+=(a,)
for i in t:
    print(i)
print("Maximum is : ",max(t))
print("Minimum is : ",min(t))
