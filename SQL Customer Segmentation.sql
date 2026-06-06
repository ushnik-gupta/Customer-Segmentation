CREATE DATABASE customer_segmentation_db;

USE customer_segmentation_db;

CREATE TABLE customer_data (
Customer_ID VARCHAR(20),
Gender VARCHAR(20),
Age INT,
Annual_Income FLOAT,
Spending_Score FLOAT,
Purchase_Frequency INT
);

INSERT INTO customer_data
VALUES
('C001','Male',22,25000,39,4),
('C002','Female',45,80000,81,12),
('C003','Male',31,42000,6,2),
('C004','Female',29,73000,77,10),
('C005','Female',35,54000,40,5),
('C006','Male',52,92000,92,15),
('C007','Female',27,35000,25,3),
('C008','Male',41,68000,70,9);

SELECT * FROM customer_data;

SELECT
AVG(Annual_Income)
AS Average_Income
FROM customer_data;

SELECT
MAX(Spending_Score)
AS Highest_Spending
FROM customer_data;

SELECT
AVG(Purchase_Frequency)
AS Average_Purchase_Frequency
FROM customer_data;

SELECT
Gender,
AVG(Annual_Income)
AS Average_Income,
AVG(Spending_Score)
AS Average_Spending
FROM customer_data
GROUP BY Gender;

SELECT
Gender,
SUM(Purchase_Frequency)
AS Total_Purchases,
AVG(Spending_Score)
AS Average_Score
FROM customer_data
GROUP BY Gender;

SELECT
Customer_ID,
Annual_Income,
Spending_Score,
CASE
WHEN Spending_Score>=80
THEN 'HIGH VALUE'
WHEN Spending_Score BETWEEN 40 AND 79
THEN 'MEDIUM VALUE'
ELSE 'LOW VALUE'
END AS Customer_Segment
FROM customer_data;

SELECT
Gender,
AVG(Annual_Income)
AS Avg_Income
FROM customer_data
GROUP BY Gender
HAVING AVG(Annual_Income)>50000;

SELECT
Customer_ID,
Annual_Income,
RANK() OVER(
ORDER BY Annual_Income DESC
)
AS Income_Rank
FROM customer_data;

SELECT
COUNT(*) AS Total_Customers,
AVG(Annual_Income) AS Avg_Income,
AVG(Spending_Score) AS Avg_Spending,
MAX(Purchase_Frequency) AS Highest_Purchase_Frequency
FROM customer_data;