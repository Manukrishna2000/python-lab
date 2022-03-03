cyear =int(input("enter current year"))
fyear=int(input("enter final year"))
for i in range (cyear, fyear):
    if (i % 4==0) and (i % 100!=0) or (i % 400==0):
        print(i)
print("are the leap years")
      
