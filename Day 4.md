## Task 7: Write a query to find all orders attributed to a salesman in Paris
By using JOIN
```sql
select * from orders o
inner join salesman s
on o.salesman_id=  s.salesman_id
where s.city = 'Paris';
```
By using SUB QUERY
```sql
select * from orders 
where salesman_id in (select salesman_id
					from salesman
					where city='Paris'
					);
```
> We are using `IN` as the sub query provides two or more values and IN acts as an `OR` operator

## Task 8: Write a query to find the name and id of all salesmen who had more than one customer
Step 1: Getting the required id i.e, id with more than 1 customers
```sql
select salesman_id
from customer
group by salesman_id
having count(customer_id)>1;
```
Step 2:
```sql
select * 
from salesman
where salesman_id in(5001,5002);
```
Step 3: Replacing Hard coding
```sql
select * from salesman
where salesman_id in (select salesman_id
from customer
group by salesman_id
having count(customer_id)>1);
```

# ALL & ANY Operator

Task 1: Want all orders which are greater than Poojitha's order


Using ALL:
```sql
select *
from orders 
where purch_amt > all (select purch_amt
					from orders
					where customer_id=3005)
```
Using GROUP BY:

```sql
select *
from orders 
where purch_amt > (select MAX(purch_amt)
					from orders
					where customer_id=3005);
```

Using ANY:
```sql
select *
from orders 
where purch_amt > any (select purch_amt
					from orders
					where customer_id=3005)
```

> ### ALL is used to give MAX
> ### ANY is used to give MIN

## Task 9 : Write a query to display only those customers whose grade are, in fact, higher than every customer in New York.
--- All or Any

```sql
select *
from customer 
where grade > ALL (select grade
					from customer
					where city='New York');
```
## Task 10 : Write a query to find all orders with an amount smaller than any amount for a customer in London.

-- Step 1 : Find People in London
```sql
select *
from customer
where city like 'London';   -- 3001,3008
```

-- Step 2: Find their min value order
```sql
select *
from orders
where customer_id in (3001,3008);  --lower than this id amt i.e, 250.45
```

-- Step 3 : Find the order below that min
```sql
select *
from orders
where purch_amt< 250.45
```
-- Step 4 : Hardcoding (Using ANY)
```sql
select *
from orders
where purch_amt < any(select purch_amt
						from orders
						where customer_id in (select customer_id
												from customer
												where city like 'London'))
```

Using MIN
```sql
select *
from orders
where purch_amt < (select min(purch_amt)
						from orders
						where customer_id in (select customer_id
												from customer
												where city like 'London'))
```

# Entity Relation Diagram ERD
- It's makes even the non coders to understand what's going with the tables   
- Helps to `Normalise` tables   
- Using `Cardinality` we relate the tables
- https://lucid.co/try-now Website to create an ERD
    - Span = Ctrl + space
    - `ON DELETE CASCADE` is used to delete all the values related to that foreign key
- `[ ]` is used to get column names so that we can include   
- Required arrow indications
![alt text](<Screenshot 2024-04-30 183827.png>)

# Inbuilt Functions
- String function
- Math function
- Date function

Ex: SELECT UPPER('abraka') as NAME;

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
![alt text](<Screenshot 2024-04-26 172729.png>)