d1=dict()
n=int(input("Enter no. of students : "))
for i in range(n):
    c=input("Enter student name : ")
    t=input("Enter percentage name : ")
    d1[c]=t
print("Original Dictionary")
print(d1)
print("New dictionary ")
x=input("Enter a student name to be deleted : ")
del d1[x]
print(d1)
