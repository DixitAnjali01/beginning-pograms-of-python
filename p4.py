#TO REMOVE CHARACTERS FROM A STRING AND PRINT A NEW STRING
str=input('Enter the string:')
n=int(input()) 
count=0                  #Here n must be less than length of a string
for i in str:
    count=count+1
print(str[n:count])

