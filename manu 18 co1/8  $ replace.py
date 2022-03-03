s=input("enter a word")
for x in s:
    if (x=="o"):
        s=s.replace(x,"$")
        print(s)
else:
    print("there is no o to replace")
