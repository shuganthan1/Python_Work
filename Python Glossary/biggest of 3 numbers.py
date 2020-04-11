#Biggest of 3 number exercise
a= input('give a number: ')
b = input('give the second number: ')
c = input('give the third number: ')
if (a>b and a>c):
    print ('A is the bigger than {},{}'.format(b,c))
elif (b>a and b>c):
    print('B is the bigger than {},{}'.format(a,c))
else:
    print('C is the bigger than {},{}'.format(a,b))