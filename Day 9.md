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