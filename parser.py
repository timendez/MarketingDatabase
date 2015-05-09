import sys
import csv

ROWS_PER_INSERT = 2000

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

# Write dict of values for insert into DB
# Start a new INSERT statement every 32,000 lines
def insert_values(table, data):
    if counts[table] == ROWS_PER_INSERT:
        end_sql(table)
        start_sql(table)
        counts[table] = 0
    else:
        counts[table] += 1
    files[table].write('(%s),\n' % ','.join(data))

def start_sql(table):
    files[table].write('INSERT INTO %s VALUES\n' % table)

def end_sql(table):
    f = files[table]
    f.seek(f.tell() - 3)
    f.write(';\n')
    f.truncate()

def handle_account(data):
    # Customers
    Customer = data['CustomerID']
    if Customer not in pk['Customers']:
        insert_values('Customers', [
            data['CustomerID'],
            data['RegSourceID'],
            to_string(data['RegSourceName']),
            to_string(data['ZIP']),
            to_string(data['State']),
            to_string(data['Gender']),
            to_string(data['IncomeLevel']),
            data['Permission'],
            to_string(data['Language']),
            to_string(data['CustomerTier']),
            ])
        pk['Customers'].add(Customer)

    # EmailAddresses
    EmailAddress = data['EmailID']
    if EmailAddress not in pk['EmailAddresses']:
       insert_values('EmailAddresses', [
          data['EmailID'],
          to_string(data['DomainName']),
          data['CustomerID']
          ])
       pk['EmailAddresses'].add(EmailAddress)


device_id = 0

def handle_device(data):
    global device_id;

    Device = 'NULL'

    if data['SerialNumber']:
        Device = str(device_id)
        device_id += 1

    # Purchases
    insert_values('Purchases', [
        to_date(data['PurchaseDate'], '%m/%d/%Y'),
        to_string(data['PurchaseStoreName']),
        to_string(data['PurchaseStoreCity']),
        to_string(data['PurchaseStoreState']),
        data['Ecomm'],
        data['CustomerID'],
        Device,
        to_string(data['DeviceModel'])
        ])

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
            Device
            ])
        pk['Registrations'].add(Registration)

    # Devices
    if Device != 'NULL':
        insert_values('Devices', [
            Device,
            to_string(data['SerialNumber']),
            to_string(data['DeviceModel'])
            ])

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



# List of all tables (in order of creation)
tables = ['Customers', 'EmailAddresses', 'EmailMessages', 'EventTypes', 'Events', 'Links',
    'EventLinkLookUp', 'DeviceModels', 'Devices', 'Purchases', 'Registrations']

files = {}      # Dict of files where key=table
pk = {}         # Existing primary keys as a single value or tuple
counts = {}     # Row counts - reset to 0 every 32,000 rows

# Open files and initialize each table
for t in tables:
    files[t] = open('build/DB-build-%s.sql' % t, 'w+')
    start_sql(t)
    pk[t] = set()
    counts[t] = 0

# Parse the CSV files provided by customer
print("Parsing: CP_Account.csv")
parse('data/CP_Account.csv', handle_account)

print("Parsing: CP_Device.csv")
parse('data/CP_Device.csv', handle_device)

print("Parsing: CP_Device_Model.csv")
parse('data/CP_Device_Model.csv', handle_device_model)

print("Parsing: CP_Email_Final.csv")
parse('data/CP_Email_Final.csv', handle_email)

# End files with ; before closing
for t in tables:
    end_sql(t)
    files[t].close()
