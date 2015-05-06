# Python 3.4: https://www.python.org/downloads/
# mysql-connector-python: http://dev.mysql.com/downloads/connector/python/
# On unix12 use python3

import csv
import os
# import mysql.connector

def init(table):
    files[table].write('INSERT INTO %s VALUES\n' % table)

def quote(value):
    return '"%s"' % value

def values(table, data):
    files[table].write('(%s),\n' % ','.join(data))

def parse(filename, callback):
    with open(filename) as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            callback(row)

def handle_account(data):
    pass

def handle_device(data):
    pass

def handle_device_model(data):
    values('DeviceModels', [
        quote(data['Device Model']),
        quote(data['Device Name']),
        quote(data['Device Type']),
        quote(data['Carrier'])
        ])

def handle_email(data):
    pass




# Open files
files = {
    'DeviceModels': open('DB-build-DeviceModels.sql', 'w+')
}

for f in files:
    init(f)

parse('data/CP_Account.csv', handle_account)
parse('data/CP_Device.csv', handle_device)
parse('data/CP_Device_Model.csv', handle_device_model)
parse('data/CP_Email_Final.csv', handle_email)

# Close files
for f in files:
    files[f].seek(files[f].tell()-3)
    files[f].write(';\n')
    files[f].truncate()
    files[f].close()

# try:
#     conn = mysql.connector.connect(user='', password='',
#         host='', database='')
# except mysql.connector.Error as err:
#     print(err)
# else:
#     main()
#     conn.close()
