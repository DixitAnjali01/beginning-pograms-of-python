#PROGRAM TO CALCULATE SUM OF CURRENT NUMBER AND PREVIOUS NUMBER
range1=int(input('Enter the range till which you want your proggram to run:'))
x=0
y=0
for num in range(range1+1):
    print('Curent number %d; Previous number %d ; SUM =%d'%(x,y,x+y))
    y=x
    x=x+1
