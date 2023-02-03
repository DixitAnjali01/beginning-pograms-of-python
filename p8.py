#PROGRAM TO PRINT A PATTERN LIKE-
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5
for i in range(6):
    if(i>0):
        for j in range(i):
            print(i,end=" ")
        print('\n')