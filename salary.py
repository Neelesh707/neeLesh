d1=dict()
n=int(input("Enter no. of entries : "))
for i in range(n):
    a=input("Enter name : ")
    b=int(input("Enter salary : "))
    c=int(input("Enter house rent : "))
    d=int(input("Enter conveyance : "))
    d1[a]=[b,c,d]
l=d1.keys()
print("\nName",'\t\t',"Net Salary")
for i in l:
    salary=0
    z=d1[i]
    for j in z:
        salary=salary+j
    print(i,'\t\t',salary)
