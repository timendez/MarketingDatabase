CREATE TABLE EmailCampaignPerformance (
    CampaignName VARCHAR(64),
    Audience VARCHAR(64),
    Version VARCHAR(64),
    SubjectLine VARCHAR(4),
    DeploymentDate DATE,
    EmailsSent INT,
    EmailsBounced INT,
    EmailsComplained INT,
    EmailsClicked INT,
    EmailsOpened INT,
    EmailsUnsubscribed INT
);

CREATE TABLE RegistrationsXCustomersXDevices (
    CustomerID INT,
    State CHAR(64),
    Month CHAR(16),
    Year INT,
    Permission BOOLEAN,
    Carrier VARCHAR(64),
    Registrations INT
);
