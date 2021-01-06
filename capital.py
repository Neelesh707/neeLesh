d1=dict()
n=int(input("Enter no. of entries : "))
for i in range(n):
    a=input("Enter name of the country : ")
    b=input("Enter capital : ")
    c=input("Enter currency : ")
    d1[a]=[b,c]
l=d1.keys()
x=input("Enter country name to be Searched : ")
print("\nCountry",'\t\t'"Capital",'\t\t',"Currency")
for i in l:
    if i==x:
        print(a,'\t\t\t',b,'\t\t\t',c)
        break
    else:
        print("Country not present")

