#CREATING A NEW LIST FROM THE TWO LISTS
list1=[]
n=int(input("Enter the number of elements you want in the lists:"))
for i in range(n):
    x=int(input())
    list1.append(x)
print("The first list is =",end=' ')
print(list1)
list2=[]

for i in range(n):
    x=int(input())
    list2.append(x)
print("The second list is =",end=' ')
print(list2)
list3=[]
for i in range(n):
    if(list1[i]%2!=0):
        list3.append(list1[i])
    if(list2[i]%2==0):
        list3.append(list2[i])
print("The third list is :",end=' ')
print(list3)
