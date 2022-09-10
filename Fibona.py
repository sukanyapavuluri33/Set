f1=0
f2=1
n=int(input("Enter number of elements in series: ")) 
print("FIBONACCI SERIES")
print(f1)
print(f2)
while n-2>0:
    f=f1+f2
    print(f)
    f1=f2
    f2=f
    n=n-1
