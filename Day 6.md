### Task 4
Write a query to calculate the tenure of each employee in complete years as of today.

```sql
select FirstName,DATEDIFF(YEAR,StartDate,GETDATE())
FROM EmployeeData;
```
### Task 5 
Calculate Annual Salary Increase  
-- Assume a yearly salary increase of 3% for each employee.   
-- Write a query to calculate their new salary rounded to the nearest whole number.
```sql
select *,(1.03*salary) as new_salary from employeedata
```


## Equi Join, Natural Join, Inner Join

## Natural Join
- Works only when the key joining two tables have same `Column name`
- Doesn't have any conditions
```sql
SELECT * FROM employee
NATURAL JOIN department;
```

## Equi Join
- Condition always `=` and not like <,>,<=,>=
```sql
SELECT * FROM employee e
INNER JOIN department d
ON e.emp_id=d.emp_id;
```

## Inner Join (with other than =)

```sql
[10:32 AM] Ragav Kumar V (Unverified)
CREATE TABLE Employees (

    EmployeeID INT,

    Name VARCHAR(50),

    Salary DECIMAL(10,2),

    DepartmentID INT

);
 
CREATE TABLE Departments (

    DepartmentID INT,

    DepartmentName VARCHAR(50),

    MinSalary DECIMAL(10,2)

);
 
INSERT INTO Employees VALUES (1, 'John Doe', 50000, 101), (2, 'Jane Smith', 40000, 102);

INSERT INTO Departments VALUES (101, 'HR', 45000), (102, 'Marketing', 35000);
 
Select * from Employees
 
Select * from Departments
 
 
Select Name, Salary, DepartmentName,  MinSalary

From Employees

Inner Join Departments 

on Salary > MinSalary
```

## Create Database with command
```sql
CREATE DATABASE fun;  --Creating
USE fun;     --Switching

Exec sp_renamedb 'fun','cool';         --Renaming

DROP DATABASE cool;   --Drop
```

## Limiting
- Offset is a must while doing limit

### Task 1: To display top 3 purchases

```sql
SELECT * 
FROM orders
ORDER BY purch_amt DESC
OFFSET 0 ROWS
FETCH NEXT 3 ROWS ONLY;  
```
## Link for Microsoft DOCS
https://learn.microsoft.com/en-us/sql/t-sql/functions/format-transact-sql?view=sql-server-ver16

### Task 2: Format Date - 25 Apr 2012
-- Clue: String Functions - Fromat
```sql
SELECT *,FORMAT(Ord_date,'dd MMM yyyy')
FROM orders;
```

## Variable Declaration
```sql
Format :  Declare @variableName <Data Type> = <Value>
```
```sql
DECLARE @d DATE = GETDATE();
SELECT FORMAT(@d,'dd/MM/yyy','en-us');
```

### Task: Modify the statement - Asking new user then number of rows

```sql
DECLARE @t INT = 3;
SELECT *, FORMAT(ord_date, 'dd MMM yyyy')
FROM orders 
Order by purch_amt desc
    OFFSET 0 ROWS  
    FETCH NEXT @t ROWS ONLY;
```

## SET OPERATIONS
- Union
- Intersect - common
- Except - un common   (Order Matters)

### Database
```sql
Create database setoperations;
use setoperations

 
CREATE TABLE Employees (
    EmployeeID INT,
    Name VARCHAR(50),
    Department VARCHAR(50)
);
 
INSERT INTO Employees (EmployeeID, Name, Department) VALUES
(1, 'Alice', 'Engineering'),
(2, 'Bob', 'Marketing'),
(3, 'Charlie', 'Engineering'),
(4, 'Dana', 'HR');
 
 
CREATE TABLE Applicants (
    ApplicantID INT,
    Name VARCHAR(50),
    AppliedFor VARCHAR(50)
);
 
INSERT INTO Applicants (ApplicantID, Name, AppliedFor) VALUES
(5, 'George', 'Engineering'),
(6, 'Helen', 'Marketing'),
(7, 'Ian', 'Marketing'),
(3, 'Charlie', 'Sales');
 
Select * from Employees;
Select * from Applicants;
```
### INTERSECT 
- Gives only the unique value present in both table
- It provides common

```sql
SELECT Department from Employees
INTERSECT
SELECT AppliedFor from Applicants
```

### UNION
- Gives all the unique values present in both table
```sql
SELECT Department from Employees
UNION
SELECT AppliedFor from Applicants
```
### EXCEPT
- Gives only the values that presents in table 1 and not table 2
- It provides difference
- Only here order matters i.e, which statement to put before and after the EXCEPT

```sql
SELECT Department from Employees
EXCEPT
SELECT AppliedFor from Applicants
```
### Task 1: List all distinct products that are either in stock or have been ordered.
```SQL
select productname from Products where InStock like 'yes'
UNION
SELECT productname FROM Products where ProductID in (select ProductID from Orders)
```

### Task 2: Identify products that are both in stock and have been ordered 
```SQL
select productname from Products where InStock like 'yes'
INTERSECT
SELECT productname FROM Products where ProductID in (select ProductID from Orders)
```

### Task 3: Find products that are in stock but have never been ordered.
```SQL
select productname from Products where InStock like 'yes'
EXCEPT
SELECT productname FROM Products where ProductID in (select ProductID from Orders)
```

## DATABASE KEY
1. Primary key
2. Foreign key
3. Composite key
4. Alternate key 
5. Candidate key - They have potential to be primary key
6. Super key - Combination of keys that uniquely identifies a record
- They must be
    - Unique 
    - Not NULL
    
    ![alt text](./Images/Screenshot%202024-04-29%20141059.png)
## ACID PRINCIPLE
A - Atomicity  
C - Consistency  
I - Isolation  
D - Durability  

- Good database is identified by ACID properties

## Database
```sql
CREATE TABLE EmployeeSales (
    EmployeeID INT,
    Region VARCHAR(50),
    Category VARCHAR(50),
    Quarter VARCHAR(10),
    SalesAmount DECIMAL(10,2)
);
 
INSERT INTO EmployeeSales (EmployeeID, Region, Category, Quarter, SalesAmount)
VALUES
    (101, 'North', 'Electronics', 'Q1', 1200.00),
    (101, 'North', 'Electronics', 'Q2', 1500.00),
    (102, 'North', 'Clothing', 'Q1', 800.00),
    (102, 'North', 'Clothing', 'Q2', 950.00),
    (103, 'South', 'Electronics', 'Q1', 1000.00),
    (103, 'South', 'Clothing', 'Q1', 1200.00),
    (104, 'East', 'Electronics', 'Q2', 1150.00),
    (104, 'East', 'Clothing', 'Q2', 500.00),
    (105, 'West', 'Electronics', 'Q1', 1900.00),
    (105, 'West', 'Clothing', 'Q1', 1100.00),
    (105, 'West', 'Electronics', 'Q2', 2100.00),
    (105, 'West', 'Clothing', 'Q2', 1300.00);
```
# COMPOUND SORTING

### Task 1: sort based on region and further sort based on amount in region
```sql
select * from EmployeeSales
order by region,SalesAmount desc;
```
# COMPOUND GROUPING 

### Task 2: 
```sql
select Region,Category,SUM(SalesAmount) from EmployeeSales
group by Region,Category
order by region,Category desc;
```

# GROUPING SETS

-- Grouping sets - R-C,R-Q,R,Q
```sql
select Region,Category,Quarter,SUM(SalesAmount) from EmployeeSales
group by GROUPING SETS(
				(Region,Category),
				(Region,Quarter),
				Region,Quarter
)
Order by GROUPING(Region),GROUPING(Category),GROUPING(Quarter)
```
# Co-Related sub queries

# Self join
```sql
select o.name,o.city,o.commission
from salesman o
INNER JOIN(
	select city, max(commission) as max_comm
	from salesman
	where city is not null
	group by city
)i
on o.commission=i.max_comm;
```
### Database
```sql
CREATE DATABASE projects; -- Creating
 
USE projects; -- Switching
 
 
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50)
);
 
CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100),
    employee_id INT,
    start_date DATE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);
 
 
INSERT INTO employees (employee_id, name, department) VALUES
(1, 'Alice', 'Engineering'),
(2, 'Bob', 'Engineering'),
(3, 'Charlie', 'HR'),
(4, 'David', 'Marketing');
 
INSERT INTO projects (project_id, project_name, employee_id, start_date) VALUES
(101, 'Alpha', 1, '2021-01-10'),
(102, 'Beta', 2, '2021-03-15'),
(103, 'Gamma', 1, '2021-02-20');
```
-- Let's find employees from the engineering department who are working on any project

```sql
select * from employees o
where department = 'Engineering' AND EXISTS(
    select * from projects i
    where o.employee_id=i.employee_id
)
```
## EXISTS - Return boolean value

