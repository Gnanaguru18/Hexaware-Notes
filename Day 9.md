## Expression vs Statement
- Expression - Returns a value
    - EX: nice= (9*8)
- Statement - Doesn't reutrn a value
    - Ex: if( 5 > 7 )

```pymessage = "secret_code"
print(message[0])
# message[0]="T"      # Error cause strings are immutable

message="cool"
print(message)        # No error here cause the address is switched when assigning different string to the variable
```

# Slicing Operator `:`
```py
print(quote[<strat>:<end>: <skip>])
```
```py
quote="Dream is something"
print(quote[1:3])
print(quote[-1])
print(quote[-4:-1])

print(quote[1:10:2])     # prints characters by skipping one value
print(quote[1:10:1])     # prints characters between 1-10 without skipping

```
To reverse a string
```py
print(quote[::-1])       # gnihtemos si maerD
```
```py
print(quote[-1:-4:-1])   # gni Here the start is greater than end to do reverse operation
```

## Task 1: After the 🔑 print the remaining characters in uppercase and compare it with code
```py
message="     🐫🕑🕝🔑secret_code✌️"
code="SECRET_CODE✌️"
position=message.find("🔑")+1
output=message[position:].upper()

if(output==code):
    print("you are an hacker")
else:
    print("Try again")
```

## Task 2: remove junk [ * , ( ] to find the secret code
```py
message="         🔗⌨️😁😏🔑*****secret_code✌️((("
code="SECRET_CODE✌️"
position=message.find("🔑")+1
output=message[position:].upper().strip("*").strip("(")

if(output==code):
    print("you are an hacker")
else:
    print("Try again")
```
- We can add on .function() continuously 


# Lists
- Lists are mutable

```py
marks=[98,75,80,40,90,45,80,60]

print(type(marks))
print(len(marks))

print(marks[:4])    # prints first 4 elements

print(marks[::-1])     # To reverse the list
```
## Insertion
### To add additional values
```py 
marks.append(25)
```
### To insert inbetween
```py
marks.insert(3,60)      # It will add 60 in the position 3 
```
### Combining two  lists
```py
marks1=[1,2,3,4]
marks2=[5,6,7,8]

marks3=marks1+marks2
print(marks3)
```
## Deleting 
### pop
Removes the element in the position
```py
marks3.pop()
print(marks3)

marks3.pop(1)      # can also provide index of value to be deleted
```
### Remove
Removes the element given
```py
h1=[1,2,3]
h1.remove(1)
```
### Copy by Reference
```py
pl=[1000,1500,400]
plc=pl                      # The plc and pl are connected by address
pl1=[1000,1500,400]
plc.append(600)
pl.append(700)
pl1.append(800)

print(pl,plc,pl1)    # [1000, 1500, 400, 600, 700] [1000, 1500, 400, 600, 700] [1000, 1500, 400, 800]
```

### Copy by Value
```py
p1=[1000,1500,400]
p2=p1.copy()

print(id(p1),id(p2))
```
Or
```py
p3=p1[:]
```
### Repetition
```py
cloned_treasure=["Gold coin"]*3
print(cloned_treasure)
```

### SPLIT  (str->list)
```py
shop_stock="vanilla,lime,chocolate"
shop_list=shop_stock.split(",")

print(shop_list,shop_list[2])
```

### JOIN 
```py
avatar = ["fire","water","earth","air"]
print(",".join(avatar))
print("|".join(avatar))
```
 ## Task: scrambled_message = "world the save to time no is there"
 ```py
 scrambled_message = "world the save to time no is there"
scrambled_list=scrambled_message.split(" ")[::-1]
print(" ".join(scrambled_list))
```
### Guess the output
```py
avatar = ["fire","water","earth","air"]
avatar[1:3]=["Diamond","platinum","gold"]
print(avatar)     # ['fire', 'Diamond', 'platinum', 'gold', 'air']
```

# LOOPS
## While Loop
```py
while(condition):
    expression
```
To print 5 numbers
```py 
countdown=1
while countdown<6:
    print(countdown)
    countdown+=1
```
### Task: Print * pattern
```py
count=1
n=int(input("Enter number"))
while count<n+1:
    print("✨"*count)
    count+=1
```

## For Loop
```py
range(<start>,<stop>,<skip>)

for i in range():
    experssion
```
### Task : print * pattern
```py
n=int(input())
for i in range(1,n+1):
    print("✨"*i)
```

### Task : Double up each element in an array
```py
stats=[10,20,30]
for i in range(len(stats)):
    stats[i]*=2
print(stats)
```
To do it without changing the actual array
```py
stats=[10,20,30]
new_stats=[]
for i in range(len(stats)):
    new_stats.append(stats[i]*2)
print(stats)
print(new_stats)
```

To access the value without using index
```py
player_stats=[10,20,30]
new_stats=[]
for stat in player_stats:
    new_stats.append(stat*2)
print(player_stat)
print(new_stats)
```

# List Comprehenshion - copy of the result
![](./Images/list%20comprehension.png)
```py
powered_stat = [stat * 2 for stat in player_stats]  # Double the stat for each stat in stats
print(powered_stat)
print(player_stats)
```
### Task 4: 
    avengers = [
    "Hulk",
    "Iron man",
    "Black widow",
    "Captain america",
    "Spider man",
    "Thor"]   
    Output : [4, 8, 11, 15, 10, 4]
 
 ### Task 4.1 - for loop
 ```py
 length=[]
for avenger in avengers:
    length.append(len(avenger))
print(length)
```

### # Task 4.2 - List comprehension
```py
length=[len(avenger) for avenger in avengers]

# To display only 15 and 11
new_length=[count for count in length if count>10]
```
### Task: 5  Find avengers who have more than 10 characters
Output: ["Black widow","Captain america"]
### Task: 5.1  with for loop
```py
big_name=[]
for avenger in avengers:
    if len(avenger)>10:
        big_name.append(avenger)
print(big_name)
```

### Task: 5.2   with list comprehension
```py
big_name1=[avenger for avenger in avengers if len(avenger)>10 ]
print(big_name1)
```
If we need to UPPER CASE all the characters 
```py
big_name1=[avenger.upper() for avenger in avengers if len(avenger)>10 ]
print(big_name1)
```

# Dictionary
```py
#Dictionary
person={
    "name": "Lionel Messi",
    "age":36,
    "country":"Argentina",
    "Sport":"Football"
}

# Access value
print(person["name"])
print(person["age"])

print(type(person))

# Update value
person["age"]+=1

# Methods
print(person.keys())
print(person.values())

```
### Task:
```py
books = [
    {
        "title": "Infinite Jest",
        "rating": 4.5,
        "genre": "Fiction"
    },
    {
        "title": "The Catcher in the Rye",
        "rating": 3.9,
        "genre": "Fiction"
    },
    {
        "title": "Sapiens",
        "rating": 4.9,
        "genre": "History"
    },
    {
        "title": "A Brief History of Time",
        "rating": 4.8,
        "genre": "Science"
    },
    {
        "title": "Clean Code",
        "rating": 4.7,
        "genre": "Technology"
    },
]
```

### Task 1: Highly rated books | 4.7 or more   (for loop)
```py
hi_books=[]
for book in books:
    if book["rating"]>=4.7:
        hi_books.append(book["title"])
print(hi_books)
```
### Task 2: with list comprehension
```py
hii_books=[book["title"] for book in books if book["rating"]>=4.7]
print(hii_books)
```
# TUPLE
- They are `immutable`
- They only use `index` no `find`
```py
person=("Sakura","leaf village",20,20)

print(person[0],person[1])

# person[0]="Sneha"   ❌      can't change value

# Modification is not allowed
# like remove(),pop(),append(),insert()

## Allowed function
print(person.count(20))
print(person.index("Sakura"))
```


## index vs find
- Index points out error if not found
- Find returns `-1` when not found

# SETS
1. Mutable
2. Unique
3. No order(cannot access with index)   

```py
empty_dict={}                # empty dictionary
tech_gad={"smartphone","laptop","smartwatch"}
empty_set=set()

print(type(tech_gad))            # <class 'set'>
print(type(empty_set))             # <class 'set'>

print(tech_gad)
```
Methods
```py
tech_gad.add("Omiscient reader")
tech_gad.add("laptop")       # when we add an already existing element it doesn't add it again
```

### Task : Find unique colors
colors=["red","blue","red","green","pink","blue"]
```py
unique_color=set()
for color in colors:
    unique_color.add(color)
print(unique_color)
```

