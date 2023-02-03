#RETURN THE COUNT OF A GIVEN SUBSTRING FROM A STRING
str=input("Enter the string:")
sub_str=input("Enter the substring:")
n1=len(str)
n2=len(sub_str)
count = 0
flag=0
j=0
for i in range(n1):
    if(sub_str[j]==str[i]):
        flag=flag+1
        j=j+1
    elif(sub_str[j]!=str[i]):
        flag=0
        j=0
    if(flag==n2):
        count=count+1
        j=0
print("%s appeared %d times"%(sub_str,count))


