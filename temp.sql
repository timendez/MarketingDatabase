SELECT Carrier, Month, DeviceModel, COUNT(CustomerID) AS "Number of Customers"
INTO OUTFILE 'report.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
FROM RegistrationsXCustomersXDevices
GROUP BY Carrier, Month, DeviceModel
ORDER BY Carrier;

-- INTO OUTFILE 'report.csv'
-- FIELDS TERMINATED BY ','
-- ENCLOSED BY '"'
-- LINES TERMINATED BY '\n'
