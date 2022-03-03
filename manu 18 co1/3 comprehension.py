a=[1,-1,2,3,-4]
print(a)
for x in a:
    if x>0:
        print(x)
for x in a:
    c=x*x
    print(c)
    print("----------")
b="hello"
print(b)
c=["a","e","i","o","u"]
z=[y for y in c if y in b]
print("vowels are",z)
print("----------")
q="python"
list=[ord(o) for o in q]
print(list)
