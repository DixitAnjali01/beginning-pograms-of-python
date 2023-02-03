#PROGRAM TO CHECK IF THE LAST ELEMENTS OF TWO LISTS ARE SAME OR NOT
n1=int(input("Enter the number of elements of first list:"))
List1=[]
for i in range(n1):
    ele=int(input())
    List1.append(ele)
n2=int(input("Enter the number of elements of second list:"))
List2=[]
for i in range(n2):
    ele=int(input())
    List2.append(ele)
if(List1[n1-1]==List2[n2-1]):
    print("Yes!! the last elements are equal")
else:
    print("No,they are not equal")
