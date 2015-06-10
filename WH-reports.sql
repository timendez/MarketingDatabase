-- Email Campaign Performance --
SELECT CampaignName, Audience, Version, SubjectLine, DeploymentDate,
    (EmailsSent - EmailsBounced) AS EmailsDelivered,
    EmailsOpened,
    EmailsClicked,
    (EmailsOpened / (EmailsSent - EmailsBounced)) AS OpenRate,
    (EmailsClicked / EmailsOpened) AS ClickToOpenRate,
    (EmailsClicked / (EmailsSent - EmailsBounced)) AS ClickRate,
    (EmailsUnsubscribed / EmailsOpened) AS UnsubRate
FROM EmailCampaignPerformance
ORDER BY OpenRate DESC, ClickToOpenRate DESC, CampaignName;

-- Account Registration Report --
SELECT MonthName, Month, Year, State, Permission, NumCustomers
FROM AccountDeviceRegistrations
GROUP BY State, MonthName, Month, Year, Permission
ORDER BY Year DESC, Month DESC, State, Permission;

-- Device Registration Report --
SELECT MonthName, Month, Year, Carrier, DeviceModel, NumCustomers
FROM AccountDeviceRegistrations
GROUP BY Carrier, MonthName, Month, Year, DeviceModel
ORDER BY Year DESC, Month DESC, Carrier, DeviceModel;
