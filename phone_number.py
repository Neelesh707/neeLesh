phone=dict()
n=int(input("Enter no. of entries : "))
for i in range(n):
    a=input("Enter the name : ")
    b=input("Enter the phone number : ")
    phone[a]=b
l=phone.keys()
x=input("Enter a name to be searched : ")
for i in l:
    if i==x:
        print(x,"phone number is : ",phone[i])
        break
    else:
        print(x, "Does not exists ")
