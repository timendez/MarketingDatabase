# Python 3.4: https://www.python.org/downloads/
# mysql-connector-python: http://dev.mysql.com/downloads/connector/python/
# On unix12 use python3

import csv
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




# Open files, key=TableName
files = {
    'Customers'         : open('build/DB-build-Customers.sql', 'w+'),
    'EmailAddresses'    : open('build/DB-build-EmailAddresses.sql', 'w+'),
    'EmailMessages'     : open('build/DB-build-EmailMessages.sql', 'w+'),
    'EventTypes'        : open('build/DB-build-EventTypes.sql', 'w+'),
    'Events'            : open('build/DB-build-Events.sql', 'w+'),
    'Links'             : open('build/DB-build-Links.sql', 'w+'),
    'EventLinkLookUp'   : open('build/DB-build-EventLinkLookUp.sql', 'w+'),
    'DeviceModels'      : open('build/DB-build-DeviceModels.sql', 'w+'),
    'Devices'           : open('build/DB-build-Devices.sql', 'w+'),
    'Purchases'         : open('build/DB-build-Purchases.sql', 'w+'),
    'Registrations'     : open('build/DB-build-Registrations.sql', 'w+')
}

# Initialize files with "INSERT INTO TableName VALUES"
for f in files.keys():
    init(f)

# Parse the CSV files provided by customer
parse('data/CP_Account.csv', handle_account)
parse('data/CP_Device.csv', handle_device)
parse('data/CP_Device_Model.csv', handle_device_model)
parse('data/CP_Email_Final.csv', handle_email)

# End files with ; before closing
for f in files.values():
    f.seek(f.tell() - 3)
    f.write(';\n')
    f.truncate()
    f.close()

# try:
#     conn = mysql.connector.connect(user='', password='',
#         host='', database='')
# except mysql.connector.Error as err:
#     print(err)
# else:
#     main()
#     conn.close()
