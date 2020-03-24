# #csv uses
# #importing csv in python
# #managing data from csv
# #basic ETL
# #transforming data and writing to a new csv file
#
# import csv
#
# with open('user_details.csv', newline='') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter = ',')
#
#     #print (csvreader)
#
#     # for row in csvreader:
#     #     print(row[-1])
#
#     # for column in csvreader:
#     #     print(column)
#
# #to utilise some of the builtin method available iter() and next()
#
#     iterable= iter(csvreader)
#     next(iterable)
# #to skip the next line
#     for row in iterable:
#         next(iterable)
#         #skips next line in the loop
#         print(row[-1])
#
# #ETL
#
# #replace any info in your csv file from python file

import csv
def transform_user_details(csv_file_name):
    new_user_data = []

    with open('user_details.csv', newline='') as csvfile:
        user_details_csv = csv.reader(csvfile, delimiter=',')

        for user in user_details_csv:
            transformation = []
            transformation.append(user[1])
            transformation.append(user[2])
            transformation.append(user[-1])
            new_user_data.append(transformation)
    return new_user_data

print(transform_user_details('user_details.csv'))

#create csv file and copy info for user_details.csv to new_user_details.csv

def create_new_user_data_csv(old_user_data_file="user_details.csv", new_file_name='new_user_data.csv'):
    new_user_data = transform_user_details(create_new_user_data_csv)
    new_file = open(new_file_name, 'w')

    with new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_data)

create_new_user_data_csv()
#print (create new_user_data_csv())