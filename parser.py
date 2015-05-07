# Python 3.4: https://www.python.org/downloads/
# mysql-connector-python: http://dev.mysql.com/downloads/connector/python/
# On unix12 use python3

import csv
# import mysql.connector



# Read CSV and send each line to a callback function
def parse(filename, callback):
    with open(filename) as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            callback(row)

# Wrap string value in quotes
def to_string(value):
    return '"%s"' % value

def to_date(value, fmt):
    return 'STR_TO_DATE("%s", "%s")' % (value, fmt)

# If value is not specified, replace with default value
def if_null(value, default):
    if len(value) == 0:
        return default
    else:
        return value

# Write dict of values for insert into DB
def insert_values(table, data):
    files[table].write('(%s),\n' % ','.join(data))




def handle_account(data):
    pass

def handle_device(data):
    # Devices
    if data['SerialNumber']:
        Device = data['SerialNumber']
        if Device not in pk['Devices']:
            insert_values('Devices', [
                to_string(data['SerialNumber']),
                to_string(data['DeviceModel'])
                ])
            pk['Devices'].add(Device)

    # Purchases
    Purchase = (data['CustomerID'], data['DeviceModel'])
    if Purchase not in pk['Purchases']:
        insert_values('Purchases', [
            to_date(data['PurchaseDate'], '%m/%d/%Y'),
            to_string(data['PurchaseStoreName']),
            to_string(data['PurchaseStoreCity']),
            to_string(data['PurchaseStoreState']),
            data['Ecomm'],
            data['CustomerID'],
            to_string(data['SerialNumber']),
            to_string(data['DeviceModel'])
            ])
        pk['Purchases'].add(Purchase)

    # Registrations
    Registration = data['RegistrationID']
    if Registration not in pk['Registrations']:
        insert_values('Registrations', [
            to_date(data['RegistrationDate'], '%m/%d/%Y'),
            data['RegistrationID'],
            data['SourceID'],
            to_string(data['SourceName']),
            to_string(data['DeviceModel']),
            data['CustomerID'],
            to_string(data['SerialNumber'])
            ])
        pk['Registrations'].add(Registration)

def handle_device_model(data):
    # DeviceModels
    DeviceModel = data['Device Model']
    if DeviceModel not in pk['DeviceModels']:
        insert_values('DeviceModels', [
            to_string(data['Device Model']),
            to_string(data['Device Name']),
            to_string(data['Device Type']),
            to_string(data['Carrier'])
            ])
        pk['DeviceModels'].add(DeviceModel)

def handle_email(data):
    pass



# List of all tables (in no particular order)
tables = ['Customers', 'EmailAddresses', 'EmailMessages', 'EventTypes', 'Events', 'Links',
    'EventLinkLookUp', 'DeviceModels', 'Devices', 'Purchases', 'Registrations']
# Dict of files where key=table
files = {}
# Dict of existing primary keys (as a single value or tuple) for each table
pk = {}

# Open files and initialize each table
for t in tables:
    files[t] = open('build/DB-build-%s.sql' % t, 'w+')
    files[t].write('INSERT INTO %s VALUES\n' % t)
    pk[t] = set()

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
