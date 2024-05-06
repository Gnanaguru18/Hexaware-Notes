# INTRO TO PYTHON
- `Guido van Rossum` is a Dutch programmer best known as the creator of the Python programming language, for which he was the `benevolent dictator for life (BDFL)`
- It's a High level language which is in human understandable language


## Major Milestone
- It uses Garbage Colletion(GC) (2000) which automatically collects garbage values unlike c,c++ in which we had to do it manually
- python 3 was introduced in 2008 but python 2 was still in field until 2020
- Python 3 was not preferred by python 2 users as it was `not backward compactable`

## Applications of Python
- Web development 
- Data Analysis
- Automation
- Scientific and Numeric calculation 


The "zen of python" is like Thirukural for tamil

# Getting into coding

Declaration - Naming a variable Ex: int a;
Assignment - Giving it value Ex: a=3;   

Python does declaration and assignment in a single statement Ex: name = "Guru"   

The data type is infered from the value   

- `Ctrl + /' -> to comment or uncomment

## To get the datatype of a variable

```py
type(variable_name) 
```

## To get Input
```py
name=input()
```
```py
name=input("Enter your name: ")
print("hello "+name)
```

## Type conversion
```py
faren = int(input())
c=str(faren)
```
Now the value of faren is stored as string in c
### Program to convert Farenheit to celcius
```py
faren = int(input())
cel = (faren*1.8+32)
print("The equivalent of " + str(faren) + " °F is " + str(cel) + " °C")
```
In the above example we will face error in the print part if typecasting is not used inside the print as faren and cel are not in type string

## F string 
It is used to make the code more readable compared to `+`
```py
name=input()
print(f"Hello, {name}!")
```
- `{}` is called as interpolation  
- We can have expressions inside of interpolation  
- The converted string of the above example is
```py
print(f"The equivalent of  {str(faren)}°F is  {str(cel)}  °C")
```

## REPL
Read, Evaluate, Print and Loop

To open Repl type `pyton` on shell and press enter

```py
>>> nice="super cool"
>>> nice
'super cool'
>>> nice*2
'super coolsuper cool'
```

##  Task 2: Find age of the person given the birth year
```py
year = int(input("Enter the year you were born: "))
age = 2024 - year
print(f"Your age is {age}")
```
## Task 3: Print the area of circle , given the radius
```py
radius=float(input("Enter the radius"))
area=3.14*radius**2
print(f"Area of the circle is {area}")
```
## Task 4: Build a loader
Input: 70   
Output: [=======   ] 70%   
Input: 23   
Output: [==        ] 23%

```py
percentage_completed=int(input())

percent_part= percentage_completed//10

print(f"[{'='*percent_part}{' '* (10-percent_part)}] {percentage_completed}%")
```

# Conditionals
- Relational and logical operators will give boolean result

### Task : Compare two persons height
```py
u=int(input())
u_name=input()
l=int(input())
l_name=input()
if(u>l):
  print(f"{u_name} is taller than {l_name}")
else:
  print(f"{l_name} is taller than {u_name}")
  ```

### The relational operator will compare two strings in `lexographical order`
Ex: '174'>'11111'  
It compares the first word of each string one by one and come to a result   
1>1 fails   
7>1 true  
Then it prints true for '174'>'11111'   

### Task : Find wether the asked flavor is available
```py
stock1="vanilla"
stock2="lime"
stock3="chocolate"
user=input("What flavour do you want? ")
if (user==stock1 or user==stock2 or user==stock3):
  print("Yes, we have it")
else:
  print("No, we ran out of stock")
```
## IN Operator
- It is a membership operator
- Used to find a substring within a string
- Ex: 
```py
>>> 'cool' in 'this is cool'  #gives true
```
### Using ternary operator
```py
stock="vanilla,lime,chocolate"
user=input("What flavour do you want? ")
print("Yes, we have it" if user in stock else "No, we ran out of stock")
```
```py
stock="vanilla,lime,chocolate"
user=input("What flavour do you want? ")
output="Yes, we have it" if user in stock else "No, we ran out of stock"
print(output)
```

## 5 Pillars of Code Quality
1. Readability
2. Maintainablity
3. Extendability
4. Testability
5. Performance

# String operators

- Strings are immutable data (we can't change its value )
```py
msg='Hi,all'

print(msg.upper())   
print(msg.lower())
print(msg.title())         # capitalize every first character in a word
print(msg.capitalize())    # capitalize the first letter of a sentence
```
```py
quote = "      Dream is not something that you see in sleep, Dream is something that does not let you sleep"

print(quote)            
print(quote.strip())     # strips space at the start and end


quote1 = "----Dream is not something-that you see in sleep, Dream is something that does not let you sleep----"
print(quote1.strip("-"))
print(quote1.lstrip("-"))       # strips '-' from left
print(quote1.rstrip("-"))       # strips '-' from right
```

```py
quote = "Dream is not something that you see in sleep, Dream is something that does not let you sleep"

print(quote.find("something"))
print(quote.find("Dream"))
print(quote.find("naraka"))
```
```py
print(quote.replace("dream","😎"))
```
### Slicing operator `:`