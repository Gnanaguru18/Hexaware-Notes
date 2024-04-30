```sql
CREATE TABLE salesman (
    salesman_id INT PRIMARY KEY,
    name VARCHAR(255),
    city VARCHAR(255),
    commission DECIMAL(4, 2)
);


SELECT * FROM salesman

### Task 1: 

select city
from salesman
where city is not null
group by city
having count(city)=1;

select city,max(commission) as comm
from salesman
where city is not null
group by city
;

### Task 2:
Using sub query

```sql
select name, city, commission
from salesman o
where commission =(
		select max(commission)
		from salesman i
		where o.city=i.city
);
```


### Database
```sql
CREATE TABLE orders (
    ord_no INT PRIMARY KEY,
    purch_amt DECIMAL(10, 2),
    ord_date DATE,
    customer_id INT,
    salesman_id INT
);
 
 
INSERT INTO orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES
(70001, 150.5, '2012-10-05', 3005, 5002),
(70009, 270.65, '2012-09-10', 3001, 5005),
(70002, 65.26, '2012-10-05', 3002, 5001),
(70004, 110.5, '2012-08-17', 3009, 5003),
(70007, 948.5, '2012-09-10', 3005, 5002),
(70005, 2400.6, '2012-07-27', 3007, 5001),
(70008, 5760, '2012-09-10', 3002, 5001),
(70010, 1983.43, '2012-10-10', 3004, 5006),
(70003, 2480.4, '2012-10-10', 3009, 5003),
(70012, 250.45, '2012-06-27', 3008, 5002),
(70011, 75.29, '2012-08-17', 3003, 5007),
(70013, 3045.6, '2012-04-25', 3002, 5001);
```
### Task 1:
```sql
select * from orders
where salesman_id = (select salesman_id from salesman 
					where name='Paul Adam'
					);

select avg(purch_amt)
from orders
where ord_date ='2012-10-10';
```
### Task 2:
```sql
select * from orders
where purch_amt > (select avg(purch_amt)
					from orders
					where ord_date ='2012-10-10');

select avg(purch_amt)
from orders
group by salesman_id;


select * from orders o
where purch_amt>(select avg(purch_amt)
					from orders i
					where o.customer_id=i.customer_id
					);
-- using sub query
select * from orders 
where salesman_id in (select salesman_id
					from salesman
					where city='Paris'
					);
```
### Database
```sql
CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    cust_name VARCHAR(255),
    city VARCHAR(255),
    grade INT NULL,
    salesman_id INT
);
INSERT INTO customer (customer_id, cust_name, city, grade, salesman_id) VALUES
(3002, 'Nick Rimando', 'New York', 100, 5001),
(3005, 'Graham Zusi', 'California', 200, 5002),
(3001, 'Brad Guzan', 'London', NULL, 5005),
(3004, 'Fabian Johns', 'Paris', 300, 5006),
(3007, 'Brad Davis', 'New York', 200, 5001),
(3009, 'Geoff Camero', 'Berlin', 100, 5003),
(3008, 'Julian Green', 'London', 300, 5002),
(3003, 'Jozy Altidor', 'Moscow', 200, 5007);

select * from customer;
SELECT * FROM salesman;
```
select salesman_id
from customer
group by salesman_id
having count(customer_id)>1;

### Step 2:
```sql
select * 
from salesman
where salesman_id in(5001,5002);
```
### Step 3: Replacing Hard coding
```sql
select * from salesman
where salesman_id in (select salesman_id
from customer
group by salesman_id
having count(customer_id)>1);
```
```sql
select *
from customer 
where grade > ALL (select grade
					from customer
					where city='London');

select * from customer;
SELECT * FROM orders;
SELECT * FROM salesman;
```
## Step 1 : Find People in London
```sql
select *
from customer
where city like 'London';   ## 3001,3008
```
## Step 2: Find their min value order
```sql
select *
from orders
where customer_id in (3001,3008);  --lower than this id amt i.e, 250.45
```
## Step 3 : Find the order below that min
```sql
select *
from orders
where purch_amt< 250.45
```
## Step 4 : Hardcoding
```sql
select *
from orders
where purch_amt < any(select purch_amt
						from orders
						where customer_id in (select customer_id
												from customer
												where city like 'London'))
```
### Database
```sql
CREATE TABLE [Professor] (
  [professor_id] Varchar(50),
  [professor_name] Varchar(50),
  [department] Varchar(50),
  PRIMARY KEY ([professor_id])
);

CREATE TABLE [Course] (
  [course_id] Varchar(50),
  [course_name] Varchar(50),
  [professor_id] Varchar(50),
  PRIMARY KEY ([course_id]),
  Foreign key ([professor_id]) references professor([professor_id])
);

CREATE TABLE [Student] (
  [student_id] Varchar(50),
  [student_name] Varchar(50),
  PRIMARY KEY ([student_id])
);

CREATE TABLE [Enrollment] (
  [enroll_id] varchar(50),
  [student_id] Varchar(50),
  [course_id] Varchar(50),
  primary key ([enroll_id]),
  Foreign key ([course_id]) References course([course_id]),
  Foreign key ([student_id]) References student([student_id])
);

INSERT INTO Professor
VALUES ('P001','Dr. Brown','Mathematics'),
		('P002','Dr. Smith','Physics');

Select * from Professor;
 
INSERT INTO Student (student_id, student_name)
VALUES ('S001', 'Alice'),
       ('S002', 'Bob'),
       ('S003', 'Charlie');
 
Select * from Student;
 
Select * from Course;
 
INSERT INTO Course (course_id, course_name, professor_id)
VALUES ('C001', 'Math 101', 'P001'),
       ('C002', 'Physics 101', 'P002');
 
 
INSERT INTO Enrollment (enroll_id, course_id, student_id)
VALUES ('E001', 'C001', 'S001'),
       ('E002', 'C002', 'S002'),
       ('E003', 'C002', 'S001'),
       ('E004', 'C001', 'S003');
 
Select * from Enrollment;
 ```
```sql
CREATE TABLE EmployeeData (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Salary INT,
    StartDate DATE
);
INSERT INTO EmployeeData (EmployeeID, FirstName, LastName, Salary, StartDate) VALUES
(1, 'John', 'Doe', 70000, '2020-05-01'),
(2, 'Jane', 'Smith', 85000, '2018-08-15'),
(3, 'Emily', 'Jones', 94000, '2019-12-30'),
(4, 'Chris', 'Brown', 62000, '2021-03-22');

select * from employeedata
```
## Task 1 : Sort the employees by the length of their first names in descending order.
```sql
select * from EmployeeData
order by len(firstname) desc;
```
## Task 2 : Get the Initials JD,KS,EJ,CB
```sql
select concat(left(firstname,1),left(lastname,1)) 
from EmployeeData;
```
## OR
```sql
select left(firstname,1) + left(lastname,1)
from EmployeeData;
```
## Task 3 : Extract and display the first three letters of each employee's last name and display it in upper case
## Clue : substring


# Example of Date Functions
```sql
select UPPER(LEFT(LastName,3))
from EmployeeData

select upper(substring(LastName,1,3))
from employeedata

select GETDATE()

select DAY(GETDATE())
select Month(GETDATE())

select DATEADD(YEAR,1,GETDATE())

SELECT DATEDIFF(DAY, '2024-04-01','2024-04-05')
```
## Task 4
## Write a query to calculate the tenure of each employee in complete years as of today.

```sql
select FirstName,DATEDIFF(YEAR,StartDate,GETDATE())
FROM EmployeeData;
```
## Example of Math Function
```sql
SELECT ROUND(123.4567,2)
SELECT CEILING(9.5)
SELECT FLOOR(9.5)
```
![alt text](<Screenshot 2024-04-26 172315.png>)
