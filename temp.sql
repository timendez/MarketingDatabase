SELECT MonthName, Month, Year, Carrier, DeviceModel, NumCustomers
INTO OUTFILE 'report.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
FROM AccountDeviceRegistrations
GROUP BY Carrier, MonthName, Month, Year, DeviceModel
ORDER BY Year DESC, Month DESC, Carrier, DeviceModel;


-- INTO OUTFILE 'report.csv'
-- FIELDS TERMINATED BY ','
-- ENCLOSED BY '"'
-- LINES TERMINATED BY '\n'
