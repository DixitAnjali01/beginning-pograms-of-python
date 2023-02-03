#PROGRAM TO DISPLAY NUMBERS FROM LIST WHICH ARE DIVISIBLE BY 5
List=[]
n=int(input('Enter the number of elements you want in the list:'))
for i in range(n):
    x=int(input())
    List.append(x)
print(List)
print("The elements which are divisible are:")
for i in range(n):
    if(List[i]%5==0):
        print(List[i])
