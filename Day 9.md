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
