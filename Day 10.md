# Working across sets
1. Union
2. Intersection
3. Difference (except)
```py
out_act={"Hiking","Cycling","Swimming"}
in_act={"Gaming","Reading","Cycling"}

print(out_act.union(in_act))
#{'Gaming', 'Hiking', 'Swimming', 'Reading', 'Cycling'}

print(out_act.intersection(in_act))
#{'Cycling'}

print(out_act.difference(in_act))
#{'Hiking', 'Swimming'}

print(out_act.symmetric_difference(in_act))   # Opposite of intersection
#{'Swimming', 'Reading', 'Hiking', 'Gaming'}
```


# Multiple variable assignment

a=b=c=10
print(a,b,c)

# Unpacking / Destructuring
```py
poojitha,shivam,samar=("Black current","Choco","Butter") 
# Even if we didn't give bracket it will take as tuple
# like 
poojitha,shivam,samar="Black current","Choco","Butter" 


print(shivam)

# By lists
movies=["Mission Impossible","JJK","Avengers"]
mathesh,nandhini,devesh=movies
```
Unequal element assignment gives Error
```py
t1,t2,t3=[1,2,3,4]   # Errors out
```
To make the programmers understand that we skipped the value we use `-`
```py
t1 , t2 , t3 , _ =[1,2,3,4]
print(t1,  t2 ,t 3 , _ )
```
# Unpacking Operator
```py
t1,t2,*t3=[1,2,3,4,5,6,7,8,9]
print(t1,t2,t3)      # 1 2 [3, 4, 5, 6, 7, 8, 9]
print(type(t3))      # <class 'list'>
```
Even if we use tuple to declare the output assigned will be in list

```py
t1,t2,*t3=(1,2,3,4,5,6,7,8,9)
print(t1,t2,t3)      # 1 2 [3, 4, 5, 6, 7, 8, 9]
print(type(t3))      # <class 'list'>
```
## Another method
```py
marks=[ 70, 80, 60]
marks2=[ *marks, 75, 68]

marks3 = [100,60, * marks,50]
```
### Task : merge the lists
```py
t1=[80,90]
t2=[50,60]

t3=[*t1,*t2]

print(t3)
```

###  Task: Find the distance for each point from origin
coordinates= [(5,4),(1,1),(6,10),(9,10)]
### Task 1.1 : For loop
```py
coordinates= [(5,4),(1,1),(6,10),(9,10)]
distance=[]
for points in coordinates:
    a=points[0]
    b=points[1]
    distance.append((a**2+b**2)**0.5)
print(distance)
```

### Task 1.2 : For + unpacking
```py
coordinates= [(5,4),(1,1),(6,10),(9,10)]
distance=[]
for points in coordinates:
    a,b=points
    distance.append((a**2+b**2)**0.5)
print(distance)
```
OR
```py
for a,b in coordinates:
    distance.append((a**2+b**2)**0.5)
```

### Task 1.3 : list comprehension + unpacking
```py
distance=[round((a**2 + b**2)**0.5, 2) for a,b in coordinates ]
print(distance)
```
# Loop in dictionary
```py
for key in person:
    print(key,person[key])
```
OR
```py
for k,v in person.items():       # items gives both key and value
    print(k,v)
```
## Unpacking in Dictionary -> ** Dict
```py
movie={"name":"John wick","year":2014}

mv1= {**movie, "actor":"Keanu Reeves","year":2015}  # when providing multiple values for the same key the last value will be taken

print(mv1)          # {'name': 'John wick', 'year': 2015, 'actor': 'Keanu Reeves'}
print(movie)        # {'name': 'John wick', 'year': 2014}
```
# Nested Dictionary Access
```py
person = {
    "name": "Lionel Messi",
    "age": 36,
    "address": {
        "city": "rosario",
        "country": "Argentina",
    },
    "sport": "football",
}

print(person["address"])
print(person["address"]['city'])
```
Give Error when tried to access unavailable data
```py
print(person["stats"])   # KeyError
```
## Safer way to Access value get()
Syntax:
```py
person.get(key,default value)
```
By using get() it provides None if the value is not present
```py
print(person.get("stats"))      # None

print(person.get("address").get("city")) 

# If we try to access a nested value with is not present it gives Error even in get()
print(person.get("stats").get("goals"))


# To avoid those error we can use like

print(person.get("stats", {}).get("goals"))  # None
print(person.get("stats", {"goals": 0}).get("goals"))  # None
```

### Task: 
employees = [  
    {"name": "Sneha", "experience": 2},  
    {"name": "Manju"},  
    {"name": "Sai Subash", "experience": 4},  
    {"name": "Manasa"},  
]  
 
 
### Task 1: After 1 experience
 Output  
[
    {"name": "Sneha", "experience": 3},  
    {"name": "Manju",  "experience": 1},  
    {"name": "Sai Subash", "experience": 5},  
    {"name": "Manasa", "experience": 1},  
]  

```py
for i in employees:
    i["experience"]=i.get("experience",0)+1
print(employees)
```

### Task 2: Senior 5 or more, Mid-Level 3 to 5, Junior < 3
Output
[   
    {"name": "Sneha", "experience": 3, "status": "Mid-Level"},   
    {"name": "Manju", "experience": 1, "status": "Junior"},   
    {"name": "Sai Subash", "experience": 5, "status": "Senior"},   
    {"name": "Manasa", "experience": 1, "status": "Junior"},   
]   
```py
for i in employees:
    i["experience"]=i.get("experience",0)+1
    if i.get("experience")>=5:
        i["status"]="Senior"
    elif i.get("experience")<3:    # can also 
        i["status"]="Junior"
    else:
        i["status"]="Mid-level"
print(employees)
```

# Function

def function_name(parameters):
    expressions

```py
def add(a,b):
    return a+b
```
```py
def driving_test(name,age,car="Dezire"):  
    if age>=18:
        return f"{name} eligible in {car}"
    else:
        return "Not eligible"

print(driving_test("Sai Subash",20,"Creata"))
print(driving_test("Sai Ganesh",20))          # It will take the default argument from the function
```
## Types of argument
1. Position argument
2. Keyword argument

### Position argument
```py
print(driving_test("Sai Subash",20,"Creata"))
```
### keyword argument
```py
print(driving_test(age=20,name="Abishek"))
```
- We can also combine both keyword and position argument
```py
print(driving_test("abishek",car="Honda",age=20))
```
- But the position argument must be provided before keyword argument
### Task:
```py
library_list = [
    {
        "title": "Python Programming",
        "author": "Eric Matthes",
        "year": 2019,
        "available": True
    },
    {
        "title": "Automate the Boring Stuff with Python",
        "author": "Al Sweigart",
        "year": 2020,
        "available": True
    },
    {
        "title": "Learning Python I",
        "author": "Mark Lutz",
        "year": 2013,
        "available": False
    },
    {
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "year": 2015,
        "available": True
    },
    {
        "title": "Adavance Python",
        "author": "Mark Lutz",
        "year": 2015,
        "available": False
    },
]

book = {"title": "Fluent Python II", "author": "Alex", "year": 2016, "available": True}
```
### Task 1: Add Book Function: Write a function add_book(library, new_book)
```py
def add_book(library, new_book):
    library.append(new_book)

add_book(library_list,book)
print(library_list)
```
### Task 2: Search Books by Author Function: Write a function search_by_author(library, author_name)
```py
def add_book(library, author_name):
    b=[]
    for book in library:
        if(book["author"]==author_name):
            b.append(book)
    print(b)

print(add_book(library_list,"Mark Lutz"))


# OR
def add_book(library, author_name):
    return [book for book in library if book["author"] == author_name]

```

### Task 3: Check Out Book Function: Write a function check_out_book(library, title) that marks a book as not available if it exists and is available in the library.
```py
def add_book(library, title):
    exists=False
    for book in library:
        if book["title"]==title:
            if(book["available"]=="True"):
                book["available"]="False"
                print("Book available")
                exists=True
            else:
                exists=True
                print("Someone else has it")
                
    if exists==False:
        print("No such book")
  

add_book(library_list,"Learning Python I")


# OR 


def add_book(library, title):
    for book in library:
        if book["title"]==title:
            if(book["available"]=="True"):
                book["available"]="False"
                return f"Book available"
            else:
                return f"Someone else has it" 
    return f"No such book"
  
print(add_book(library_list,"abc"))
```

# Inbuilt Functions
1. sum
2. max
3. min

```py
print(sum([1,2,3,4]))


```

### Task 1: Get_movies_avg_rating
```py
movies = [
    {"title": "Inception", "ratings": [5, 4, 5, 4, 5]},
    {"title": "Interstellar", "ratings": [5, 5, 4, 5, 4]},
    {"title": "Dunkirk", "ratings": [4, 4, 4, 3, 4]},
    {"title": "The Dark Knight", "ratings": [5, 5, 5, 5, 5]},
    {"title": "Memento", "ratings": [4, 5, 4, 5, 4]},
]

```
```py
def get_movies_avg_rating(movies):
    for movie in movies:
        movie["average rating"]=sum(movie["ratings"])/len(movie["ratings"])
    return movies

pprint(get_movies_avg_rating(movies))

```

### Task 2: Break it into 2 functions
```py
def cal_avg(movie):
    return sum(movie["ratings"])/len(movie["ratings"])
 
def get_movies_avg_rating(movies):
    for movie in movies:
        movie["average rating"]=cal_avg(movie)
    return movies

pprint(get_movies_avg_rating(movies))
```



## Import package 
```py
from pprint import pprint
```
### Task : create max function
```py
def own_max(*nums):
    big=nums[0]
    for i in nums:
        if big<i:
            big=i
    return big
 
print(own_max(5, 6, 10))
print(own_max(5, 6, 10, 7, 80, 60))
```
## Arbitrary keyword Arguments
```py
def party(**people):
    return ",".join(people.value())

print(party(p1="Abdul",p2="Rasheed",p3="Jagan",p4="Nafil"))
```
# Lambda Function
