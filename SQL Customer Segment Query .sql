USE sales_dashboard_db;

CREATE TABLE Customer_Segmentation (
    Customer_ID VARCHAR(10) PRIMARY KEY,
    Gender VARCHAR(10),
    Age INT,
    Annual_Income INT,
    Spending_Score INT,
    Purchase_Frequency INT
);

INSERT INTO Customer_Segmentation
(Customer_ID, Gender, Age, Annual_Income, Spending_Score, Purchase_Frequency)
VALUES
('C001', 'Male', 22, 25000, 39, 4),
('C002', 'Female', 45, 80000, 81, 12),
('C003', 'Male', 31, 42000, 6, 2),
('C004', 'Female', 29, 73000, 77, 10),
('C005', 'Female', 35, 54000, 40, 5),
('C006', 'Male', 52, 92000, 92, 15),
('C007', 'Female', 27, 35000, 25, 3),
('C008', 'Male', 41, 68000, 70, 9);

SELECT * FROM Customer_Segmentation;