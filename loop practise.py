0
i = 0
while i <= 10:
    print(i)
    i += 1

#Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for item in list1:
    if (item > 150):
        break
    if(item % 5 == 0):
        print(item)

#Accept n number from user and print its multiplication table
n = int(input("Enter number to calculate multiplication table"))
for i in range(1, 11, 1):
    product = n*i
    print(product)

#pattern
print("Second Number Pattern ")
lastNumber = 6
for row in range(1, lastNumber):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")

#Given a number count the total number of digits in a number
num = 75869
count = 0
while num != 0:
    num //= 10
    count+= 1
print("Total digits are: ", count)