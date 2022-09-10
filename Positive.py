n=int(input("Enetr number of elements in list: "))
my=[]
for i in range(n):
    my.append(int(input()))
print(my)
li=[]
for i in range(n):
    if my[i]>0:
        li.append(my[i])
print(li)
