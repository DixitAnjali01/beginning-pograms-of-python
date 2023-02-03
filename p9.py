#TO CHECK WHETHER A GIVEN NUMBER IS PALINDROME OR NOT
num=int(input("Enter the given number:"))
N=num
c=0
a=0
while (N>0):
    a=N%10
    c=c*10+a
    N=N//10
if(c==num):
    print("Number is palindrome!!")
else:
    print("Number is not palindrome")
