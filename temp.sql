SELECT Carrier, MonthName, Month, Year, DeviceModel, NumCustomers
INTO OUTFILE 'report.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
FROM AccountDeviceRegistrations
GROUP BY Carrier, MonthName, Month, Year, DeviceModel
ORDER BY Carrier, Year DESC, Month DESC;


-- INTO OUTFILE 'report.csv'
-- FIELDS TERMINATED BY ','
-- ENCLOSED BY '"'
-- LINES TERMINATED BY '\n'
