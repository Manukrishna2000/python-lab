a=[]
for x in range (10):
    num=int(input("enter the input"))
    if(num>100):
        a.append("over")
    else:
        a.append(num)
    print(a)
