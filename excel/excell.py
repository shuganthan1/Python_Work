#create an excel file using phython
#this lesson includes
#introduction to the openpyxl and xlswriter libraries
#using these libraries to write  to excel and read from the same files

import xlsxwriter
#creates a workbook using the builtin method and assigning a name to the file
data9 = xlsxwriter.Workbook('data9.xlsx')#name of workbook
#change file name below if needed
worksheet = data9.add_worksheet('data_9.xlsx')#name of worksheet

#note - rows and columns are zero indexed
#first cell in worksheet A1 is (0,0), B1 is (0,1)

worksheet.write('A1','data9')
worksheet.write('A2','hello')

worksheet.name = 'data9team' #change name of sheet in excel
#this inserts name under the data9 column
# row = 2
# column = 0
#
# content = ['shugs','cj','gigi']
#
# for name in content:
#     worksheet.write(row,column,name)
#     row += 1
#creates and saves the excel file
data9.close()


#workbook.close()
#total_number_of _rows
# print(row)
# print(column)
# print(content)
# print(workbook)