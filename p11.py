#WRITE A PROGRAM TO EXTRACT EACH DIGIT FROM THE INTEGER IN REVERSE ORDER
num=int(input("Enter the given number:"))
N=num
c=0
a=0
while (N>0):
    a=N%10
    print(a,end=' ')
    c=c*10+a
    N=N//10
