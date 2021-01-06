d1=dict()
n=int(input("Enter no. of entries : "))
for i in range(n):
    a=input("Enter name : ")
    b=input("Enter item bought : ")
    c=input("Enter cost : ")
    d=input("Enter phone no. : ")
    d1[a]=[b,c,d]
l=d1.keys()
print("\nName",'\t\t',"Item Bought",'\t\t',"Cost",'\t\t',"Phone no.")
for i in l:
    print(a,'\t\t\t',b,'\t\t\t\t',c,'\t\t\t\t',d)
