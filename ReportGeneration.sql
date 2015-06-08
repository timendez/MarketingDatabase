-- Email Campaign Performance --
SELECT CampaignName, Audience, Version, SubjectLine, DeploymentDate, EmailsSent - EmailsBounced AS EmailsDelivered, EmailsOpened, EmailsClicked, EmailsOpened/(EmailsSent - EmailsBounced) AS OpenRate, EmailsClicked/EmailsOpened AS ClickToOpenRate, EmailsClicked/(EmailsSent - EmailsBounced) AS ClickRate, EmailsUnsubscribed/EmailsOpened AS UnsubRate
FROM EmailCampaignPerformance;

-- Account Registration Report --
SELECT State, Month, Permission, COUNT(CustomerID) AS "Number of Customers"
FROM RegistrationsXCustomersXDevices
GROUP BY State, Month, Permission
ORDER BY State;

-- Device Registration Report --
SELECT Carrier, Month, DeviceModel, COUNT(CustomerID) AS "Number of Customers"
FROM RegistrationsXCustomersXDevices
GROUP BY Carrier, Month, DeviceModel
ORDER BY Carrier;