#write a program in python to copy data from data9 file called whatever
# importing openpyxl module
#Write a program in python to copy data from data9 file to a new file called 'data10'
path = "data9.xlsx"# give location of the file
data9_object = op.load_workbook(path)#
data9_ws = data9_object.worksheets[0] #this gets the data from the file


data10_file = xlsxwriter.Workbook("data10.xlsx") #creating a workbook using the built in method and assigning a name to the file
sheet=data10_file.add_worksheet("data10.xlsx")
data10_file.close()

#call the new workbook back in
dat10 = op.load_workbook("data10.xlsx")
data10_ws =dat10.worksheets[0]

mr = data9_ws.max_row
mc = data9_ws.max_column

# copying the cell values from source
# excel file to destination excel file
for i in range(1, mr + 1):
    for j in range(1, mc + 1):
        # reading cell value from source excel file
        c = data9_ws.cell(row=i, column=j)

        # writing the read value to destination excel file
        data10_ws.cell(row=i, column=j).value = c.value

    # saving the destination excel file
dat10.save(str("data10.xlsx"))