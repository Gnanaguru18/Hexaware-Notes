# Class
```py
class Car:
    def __init__(self, name, engine, wheels, doors):
        # creating object calls init (constructor)
        # instance variable - self
        self.name = name
        self.engine = engine
        self.wheels = wheels
        self.doors = doors

    # instance method
    def horn(self):
        return "Vroom Vroom"


santro = Car("Santro","Epsilon",4,4)  # object (instance)
nano = Car("nano","v3",4,4)

print(type(santro),type("cool"))
print(santro.name,santro.wheels)

print(santro.horn())
```

### Task 1 : Bank acc
1. acc no
2. name
3. balance
```py

class Bank:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

amisha = Bank(123, "Amisha", 50_000)
mathesh = Bank(124, "Mathesh",70_000)
sai_ganesh = Bank(125,"Sai Ganesh",65_000)

print(amisha.name,amisha.acc_no)
```

### Task 2: To display balance like ₹ 50,000
```py
    def display_balance(self):
        return f"Your balance is: ₹{self.balance}"


print(mathesh.display_balance())
```

### Task 3: To give balance after a withdraw
```py
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            return f"Success {self.display_balance()}"
        else:
            return f"Insufficient funds. {self.display_balance()}"

print(mathesh.withdraw(10000))
```

### Task 4: To add a deposit function
```py
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            return f"{self.display_balance()}"
        else:
            return f"Enter valid amount"

print(mathesh.deposit(10000))
```

### Task 5: To change the balance with respect to the interest rate
```py
class Bank:

    interest_rate = 0.02
    .    
    .    
    def apply_interest(self):
        self.balance+=Bank.interest_rate*self.balance
        return f"Your balance after interest is {self.balance}"


print(mathesh.apply_interest())
print(Bank.interest_rate)

print(mathesh.display_interest())
```

# Static method VS Class method | Both decorators
```py
class Circle:
    pi = 3.14
 
    def __init__(self, radius):
        self.radius = radius
 
    @staticmethod          # can't access cls or instance
    def perimeter(radius):
        return 2 * Circle.pi * radius
 
    @classmethod           # can access cls and cls variables
    def from_diameter(cls, diameter):
        radius= diameter/2
        return cls(radius)
 
    def calculate_area(self):
        return Circle.pi * self.radius**2
 
 
# Normal function but inside class | no access to self
print(Circle.perimeter(2))
 
# Instance method
circle1 = Circle(4)
print(circle1.calculate_area())
 
 
# Class method - to construct the object
circle_from_dia = Circle.from_diameter(10)
print(circle_from_dia.calculate_area())  # 78.5
```
- To change the class variable we need to use class method and not an instance method

### Task : To count the no. of accounts and change the interest rate
```py
class Bank:

    interest_rate = 0.
    no_of_accounts=0

    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        Bank.no_of_accounts+=1        #  Changes made here

    @classmethod
    def update_interest_rate(cls,new_interest_rate):    #  Changes made here
        cls.interest_rate=new_interest_rate
        return cls.interest_rate
    
    @staticmethod                #  Changes made here
    def total_accounts():
        return f"In toatl we have {Bank.no_of_accounts}"


    def display_balance(self):
        return f"Your balance is: ₹{self.balance}"
    
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            return f"Success {self.display_balance()}"
        else:
            return f"Insufficient funds. {self.display_balance()}"
        
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            return f"{self.display_balance()}"
        else:
            return f"Enter valid amount"
        
    def apply_interest(self):
        self.balance+=Bank.interest_rate*self.balance
        return f"Your balance after interest is {self.balance}"

sneha = Bank(123, "Sneha", 50_000)
siva = Bank(124, "Siva",70_000)

Bank.update_interest_rate(0.10)
print(sneha.apply_interest())

print(Bank.total_accounts())
```

# Access Specifiers
1. Private    --> __ (double underscore) 
2. Protected  --> _ (single underscore)
3. Public     --> 

### Task 5: 
```py
class SavingsAccount(Bank4):
    interest_rate=0.1

    def apply_interest(self):
        interest_amt=self._balance * SavingsAccount.interest_rate
        self._balance += interest_amt
        return f"Interest received. {interest_amt}"


# We could use the above code or we could change the apply_interest in the Main class just a little

    def apply_interest(self):                        # This is the function from Bank4 class
        interest_amt=self._balance * self._interest_rate
        self._balance += interest_amt
        return f"Interest received. {interest_amt}"
```

### Task 6:
```py

```
# Magic methods
1. __str__ (human readable)
2. __repr__ (debugging)
3. __init__  --> dunder methods
```py
class Cat:
    def __init__(self, name, speed):
        self.__name = name
        self.__speed = speed
 
    # Override - (human readable)
    def __str__(self):
        # Human readable
        return f"Hi, I am {self.__name} with speed {self.__speed}"
 
    # Override -  (debugging)
    def __repr__(self):
        # Human readable
        return f"Cat('{self.__name}', {self.__speed})"
 
    def __add__(self, other):
        return self.__speed + other.__speed
 
    # Polymorphism:  Method overriding
    def speak(self):
        return "Meow!! 🐈"
 
 
pichu = Cat("pichu", 30)
snowbell = Cat("snowbell", 10)
 
print(pichu)
print(repr(pichu))
print(repr(snowbell))
 
print(pichu + snowbell)
 
```
![](./Images/Screenshot%202024-05-08%20161103.png)

# Import
![](./Images/Screenshot%202024-05-08%20163248.png)

Alternate method   
<br>
![](./Images/Screenshot%202024-05-08%20163932.png)   

- What if the file is in another folder    


![](./Images/Screenshot%202024-05-08%20164431.png)

# Exception Handling
1. try
2. except
3. else
4. finally

```py
try:
    expressionssss

except:
    return bla bla bla
```
- We can be specific by mentioning the type of error faced
```py

def math_divide(n1,n2):
    try:
        result = n1/n2

    except ZeroDivisionError:
        return "No zero buddy"
    
    else:
        # When no error occured
        print f"Division was successful"
    
    finally:                
        # Always executed no matter what
        print f"Operation done"

    return result

```

## Raise
- we can create our own error
```py
if n1<0:
    raise ValueError("Cannot be negative")
except ValueError as e:
    return f"Invalid number: {e}"
```