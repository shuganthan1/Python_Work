#Odd/even list exercise

list3 =[10,13,56,64,33,78,33]
# check whether it is odd or even assing them to diff lists
# all odd numbers shoud go to odd list
# all even numbers go to even list
evenlist = []
oddlist = []
for number in list3:   #use loop to go thru each number
    if number %2 == 0:
     evenlist.append(number)
else:
    oddlist.append(number)
print(evenlist)
print(oddlist)