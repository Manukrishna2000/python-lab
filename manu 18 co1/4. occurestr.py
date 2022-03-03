str="every day is a good day today is a good day"
print(str)
a=str.split(" ")
print(a)
count=0
for i in range (0,len(a)):
    if(a[i]=="day"):
        count+=1
print("the occurence times of day :",count) 
