## Database
Cloud is the place where database is stored.

## What is Cloud?
- Renting PC (pay as you go model).
- Just simiply providing online storage cann't be called as cloud
- Some cloud providers are AWS, Azure, Google Cloud Platform

## Use of Linux
- Free
- Open source
    - In case of any hole in the os then the users can come forward to solve the issue
- Secure
- Small footprint
- Automation

>`Alphine Linux` is used more as it uses less resources.

## Scaling
### - Vertical scaling
- Powering up the existing pc
### - Horizontal scaling
- Using another powerful pc
### Auto scaling
They can scale up or down based on the requirement


## Features
1. Frequently asked will have it in the RAM
2. Querying becomes easier
3. CRUD - easy
4. Backups are inbuilt
5. Undo (time limit)
6. Performance

***
<br/>

# NoSQL
Data are represented as graphs
- Ex: MongoDB, Redis, cassandra
<br/><br/>

<https://sqlbolt.com/lesson/select_queries_with_constraints_pt_2>
<br/><br/>

# SQL Queries

# Filtering columns

```sql
SELECT column, another_column, …
FROM mytable;
```

 
For selecting one column

```sql
SELECT Director,Title FROM movies;
```
For selecting multiple coulmns

```sql
SELECT Director,Title FROM movies;
```
For selecting all the columns
```sql
SELECT * FROM movies;
```   
<br/><br/>
## Session 2
   
|Operator       |      Condition      |SQL Example       |
| -------------- | --------------- |------------------|
| =, !=, < <=, >, >=     | Standard numerical operators      |col_name != 4|
| BETWEEN … AND          | Number is within range of two values (inclusive)| col_name BETWEEN 1.5 AND 10.5|
| NOT BETWEEN … AND      | Number is not within range of two values (inclusive)              |col_name NOT BETWEEN 1 AND 10|
| IN (…)                 | Number exists in a list              |col_name IN (2, 4, 6)|
|NOT IN (…)              |Number does not exist in a list|col_name NOT IN (1, 3, 5)|

```sql
SELECT * FROM movies where id=6;
```

Use of in
```sql
SELECT * FROM movies where year in(1995,2007,2010);
```
<br/><br/>
## Session 3
![alt text](<Screenshot 2024-04-24 125250.png>)

`%` will accept even there's no character before or after.  
Ex: Attention is considered when `%At%` is used

```sql
SELECT * FROM movies where title like "Toy story%";
```
<br>

>`_` is cannot be positive for null values

>`IN` is case sensitive  

SELECT * FROM movies where director in("John Lasseter");
SELECT * FROM movies where director = "John Lasseter";

SELECT * FROM movies where director != "John Lasseter";
<br><br>
## Session 4

```sql
Select query with unique results
SELECT DISTINCT column, another_column, …
FROM mytable
WHERE condition(s);
```
```sql
Select query with ordered results
SELECT column, another_column, …
FROM mytable
WHERE condition(s)
ORDER BY column ASC/DESC;
```
```Select query with limited rows
SELECT column, another_column, …
FROM mytable
WHERE condition(s)
ORDER BY column ASC/DESC
LIMIT num_limit OFFSET num_offset;
```
SELECT Distinct Director FROM movies
order by director;

SELECT title FROM movies 
order by year DESC
limit 4;

SELECT title FROM movies 
order by title
limit 5 offset 5;

## Session 5
```sql
SELECT query
SELECT column, another_column, …
FROM mytable
WHERE condition(s)
ORDER BY column ASC/DESC
LIMIT num_limit OFFSET num_offset;
```
#### 2. Order all the cities in the United States by their latitude from north to south
```sql
SELECT * FROM north_american_cities
where Country like "United States"
order by latitude desc
;
```
#### 3. List all the cities west of Chicago, ordered from west to east
```sql
SELECT * FROM north_american_cities
where longitude <-87.629798
order by longitude
;
```
#### 4. List the two largest cities in Mexico (by population)
```sql
SELECT * FROM north_american_cities
where country like "Mexico"
order by Population desc
limit 2
;
```
#### 5. List the third and fourth largest cities (by population) in the United States and their population
```sql
SELECT * FROM north_american_cities
where country like "United states"
order by Population desc
limit 2 offset 2
;
```
<br>

# Normalisation
- Reducing the risk and improve safety by creating sub tables   
- Primary key cann't be null    
- There can be a primary key combined of two other attributes which is called as `Composite primary key`

>A table can only have 1 column as primary 
## Session 6
# Joins
## Inner Join

```sql
Select query with INNER JOIN on multiple tables
SELECT column, another_table_column, …
FROM mytable
INNER JOIN another_table 
    ON mytable.id = another_table.id
WHERE condition(s)
ORDER BY column, … ASC/DESC
LIMIT num_limit OFFSET num_offset;
```
#### 1. Find the domestic and international sales for each movie
```sql
SELECT *
FROM movies inner join boxoffice
on id = movie_id
;
```

#### 2. Show the sales numbers for each movie that did better internationally rather than domestically
```sql
SELECT *
FROM movies inner join boxoffice
on id = movie_id
where international_sales>domestic_sales
;
```
#### 3. List all the movies by their ratings in descending order

```sql
SELECT *
FROM movies inner join boxoffice
on id = movie_id
order by rating desc
;
```
## Session 7
## Outer Joins

```sql
Select query with LEFT/RIGHT/FULL JOINs on multiple tables
SELECT column, another_column, …
FROM mytable
INNER/LEFT/RIGHT/FULL JOIN another_table 
    ON mytable.id = another_table.matching_id
WHERE condition(s)
ORDER BY column, … ASC/DESC
LIMIT num_limit OFFSET num_offset;
```
#### 3. List all buildings and the distinct employee roles in each building (including empty buildings) 

```sql
SELECT distinct Building_name, Capacity, Role
FROM Buildings 
LEFT JOIN Employees  ON Building_name = Building;
```
## Session 8

#### 1. Find the name and role of all employees who have not been assigned to a building 

```sql
SELECT * FROM employees
where building is null;
```

#### 2. Find the names of the buildings that hold no employees
>                                 `Doubt how to do this`
```sql
SELECT building_name FROM buildings 
left join employees
on building_name=building
where building is null;
```

## Session 9

#### 1. List all movies and their combined sales in millions of dollars

```sql
SELECT title, (Domestic_sales+International_sales)/1000000 as combined_sales 
FROM movies inner join boxoffice
on id=movie_id;
```

#### 2. List all movies and their ratings in percent

```sql
SELECT title, (rating*10) as percentage 
FROM movies inner join boxoffice
on id=movie_id;
```

#### 3. List all movies that were released on even number years

```sql
SELECT title
FROM movies 
where year%2 = 0;
```

## Session 10

#### 2. For each role, find the average number of years employed by employees in that role
```sql
SELECT Role, avg(years_employed) FROM employees
GROUP BY Role;
```

#### 3. Find the total number of employee years worked in each building

```sql
SELECT building, sum(years_employed) 
FROM employees
group by building;
```

## session 11

#### 1. Find the number of Artists in the studio (without a HAVING clause) 

```sql
SELECT role,count(role) FROM employees
where role like "artist";
```

#### 2. Find the number of Employees of each role in the studio
```sql
SELECT role, count(role) FROM employees
group by role;
```

#### 3. Find the total number of years employed by all Engineers 
```sql
SELECT role, sum(years_employed) FROM employees
where role like "engineer";
```

## Session 12

#### 1. Find the number of movies each director has directed
```sql
SELECT director,count(title) FROM movies
group by director;
```

#### 2. Find the total domestic and international sales that can be attributed to each director
```sql
SELECT director,sum (Domestic_sales+International_sales)
FROM movies inner join boxoffice
on id=movie_id
group by director;
```


## Session 14

#### 1. The director for A Bug's Life is incorrect, it was actually directed by John Lasseter
```sql
update movies
set director="John Lasseter"
where id=2;
```

#### 2. The year that Toy Story 2 was released is incorrect, it was actually released in 1999

```sql
update movies
set year=1999
where title="Toy Story 2";
```

#### 3. Both the title and director for Toy Story 8 is incorrect! The title should be "Toy Story 3" and it was directed by Lee Unkrich

```sql
update movies
set title="Toy Story 3",
    director="Lee Unkrich"
where title="Toy Story 8";
```

## Session 15

#### 1. This database is getting too big, lets remove all movies that were released before 2005.
```sql
delete from movies
where year<2005;
```

#### 2. Andrew Stanton has also left the studio, so please remove all movies directed by him.
```sql
delete from movies
where director like "Andrew Stanton";
```

## Session 16    'DDL vs DML'

>`DDL` will modify the table   
>`DML` will modify the values of a table   
>`Schema` is called the blue print of the table   
>

#### 1.
```sql
CREATE TABLE Database(
    Name varchar(30),
    Version float,
    Download_count integer
);
```

## Session 17

#### 1. Add a column named Aspect_ratio with a FLOAT data type to store the aspect-ratio each movie was released in.
```sql
ALTER TABLE Movies
ADD COLUMN Aspect_ratio float;
```
#### 2. Add another column named Language with a TEXT data type to store the language that the movie was released in. Ensure that the default for this language is English.
```sql
ALTER TABLE Movies
ADD column Language text
DEFAULT "English";
```

# SSMS

### Sample Input
```sql
INSERT INTO salesman (salesman_id, name, city, commission) VALUES
(5001, 'James Hoog', 'New York', 0.15),
(5002, 'Nail Knite', 'Paris', 0.13),
(5005, 'Pit Alex', 'London', 0.11),
(5006, 'Mc Lyon', 'Paris', 0.14),
(5003, 'Lauson Hen', NULL, 0.12),
(5007, 'Paul Adam', 'Rome', 0.13);
```
#### Task 1: Find the average commision of a saleman from Paris
```sql
Select avg(commission)
from salesman
where city = 'Paris';
```
#### Task 2: Find out if there are cities with only one salesman and list them
```sql
select city
from salesman
where city is not null
group by city
having count(city)=1;
```
#### Task 3: Determine the maximum commission in each city, and list the salesmen who earn this commission  (Clue: Join\)

- #### 3.1 :  Write a query to display all the orders from the orders table issued by the salesman 'Paul Adam'.

    - ```sql
        select * from orders
        where salesman_id = (select salesman_id from salesman 
					where name='Paul Adam'
					);
        ```

- #### 3.2 : Write a query to display all the orders which values are greater than the average order value for 10th October 2012

 

- #### 3.2.1 : Find the average order value for 10th October 2012

    - ```sql
        select avg(purch_amt)
        from orders
        where ord_date ='2012-10-10';
        ```


### Task 6: Write a query to find all orders with order amounts which are above-average amounts for their customers.
```sql
select * from orders o
where purch_amt>(select avg(purch_amt)
					from orders i
					where o.customer_id=i.customer_id
					);
```