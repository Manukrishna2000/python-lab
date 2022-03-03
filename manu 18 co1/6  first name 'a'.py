a=[]
x_count=0
for i in range (3):
        a1=input("enter first name")
        a.append(a1)
for a1 in a:
    count=a1.count("a")
    x_count+=count
print("no. of 'a' are",x_count)
print("-----------------------")
