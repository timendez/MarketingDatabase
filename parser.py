# Python 3.4: https://www.python.org/downloads/
# mysql-connector-python: http://dev.mysql.com/downloads/connector/python/
# On unix12 use python3

import csv
# import mysql.connector

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
    print(data['Device Name']) # Replace with something useful

def handle_email(data):
    pass

def main():
    parse('data/CP_Account.csv', handle_account)
    parse('data/CP_Device.csv', handle_device)
    parse('data/CP_Device_Model.csv', handle_device_model)
    parse('data/CP_Email_Final.csv', handle_email)

# try:
#     conn = mysql.connector.connect(user='', password='',
#         host='', database='')
# except mysql.connector.Error as err:
#     print(err)
# else:
#     main()
#     conn.close()
