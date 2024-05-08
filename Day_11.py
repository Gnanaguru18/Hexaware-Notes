# class Car:
#     def __init__(self, name, engine, wheels, doors):
#         # creating object calls init (constructor)
#         # instance variable - self
#         self.name = name
#         self.engine = engine
#         self.wheels = wheels
#         self.doors = doors

#     # instance method
#     def horn(self):
#         return "Vroom Vroom"


# santro = Car("Santro","Epsilon",4,4)  # object (instance)
# nano = Car("nano","v3",4,4)

# print(type(santro),type("cool"))
# print(santro.name,santro.wheels)

# print(santro.horn())

# class Bank:

#     interest_rate = 0.02

#     def __init__(self, acc_no, name, balance):
#         self.acc_no = acc_no
#         self.name = name
#         self.balance = balance

#     def display_balance(self):
#         return f"Your balance is: ₹{self.balance}"
    
#     def withdraw(self,amount):
#         if self.balance>=amount:
#             self.balance-=amount
#             return f"Success {self.display_balance()}"
#         else:
#             return f"Insufficient funds. {self.display_balance()}"
        
#     def deposit(self,amount):
#         if amount>0:
#             self.balance+=amount
#             return f"{self.display_balance()}"
#         else:
#             return f"Enter valid amount"
        
#     def apply_interest(self):
#         self.balance+=Bank.interest_rate*self.balance
#         return f"Your balance after interest is {self.balance}"

# amisha = Bank(123, "Amisha", 50_000)
# mathesh = Bank(124, "Mathesh",70_000)
# sai_ganesh = Bank(125,"Sai Ganesh",65_000)


# mathesh.apply_interest()
# print(Bank.interest_rate)


# class Circle:
#     pi = 3.14
 
#     def __init__(self, radius):
#         self.radius = radius
 
#     @staticmethod
#     def perimeter(radius):
#         return 2 * Circle.pi * radius
 
#     @classmethod
#     def from_diameter(cls, diameter):
#         radius= diameter/2
#         return cls(radius)
 
#     def calculate_area(self):
#         return Circle.pi * self.radius**2
 
 
# # Normal function but inside class | no access to self
# print(Circle.perimeter(2))
 
# # Instance method
# circle1 = Circle(4)
# print(circle1.calculate_area())
 
 
# # Class method - to construct the object
# circle_from_dia = Circle.from_diameter(10)
# print(circle_from_dia.calculate_area())  # 78.5

# class Bank:

#     interest_rate = 0.
#     no_of_accounts=0

#     def __init__(self, acc_no, name, balance):
#         self.acc_no = acc_no
#         self.name = name
#         self.__balance = balance
#         Bank.no_of_accounts+=1

#     @classmethod
#     def update_interest_rate(cls,new_interest_rate):
#         cls.interest_rate=new_interest_rate
#         return cls.interest_rate
    
#     @staticmethod
#     def total_accounts():
#         return f"In toatl we have {Bank.no_of_accounts}"


#     def display_balance(self):
#         return f"Your balance is: ₹{self.__balance}"
    
#     def withdraw(self,amount):
#         if self.__balance>=amount:
#             self.__balance-=amount
#             return f"Success {self.display_balance()}"
#         else:
#             return f"Insufficient funds. {self.display_balance()}"
        
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#             return f"{self.display_balance()}"
#         else:
#             return f"Enter valid amount"
        
#     def apply_interest(self):
#         self.__balance+=Bank.interest_rate*self.__balance
#         return f"Your balance after interest is {self.__balance}"

# sneha = Bank(123, "Sneha", 50_000)
# siva = Bank(124, "Siva",70_000)

# Bank.update_interest_rate(0.10)
# print(sneha.apply_interest())

# print(Bank.total_accounts())









# class Bank4:

#     _interest_rate = 0.02
#     no_of_accounts=0

#     def __init__(self, acc_no, name, balance):
#         self.acc_no = acc_no
#         self.name = name
#         self._balance = balance
#         Bank4.no_of_accounts+=1

#     @classmethod
#     def update_interest_rate(cls,new_interest_rate):
#         cls._interest_rate=new_interest_rate
#         return cls._interest_rate
    
#     @staticmethod
#     def total_accounts():
#         return f"In toatl we have {Bank4.no_of_accounts}"


#     def display_balance(self):
#         return f"Your balance is: ₹{self._balance}"
    
#     def withdraw(self,amount):
#         if self._balance>=amount:
#             self._balance-=amount
#             return f"Success {self.display_balance()}"
#         else:
#             return f"Insufficient funds. {self.display_balance()}"
        
#     def deposit(self,amount):
#         if amount>0:
#             self._balance+=amount
#             return f"{self.display_balance()}"
#         else:
#             return f"Enter valid amount"
        
#     def apply_interest(self):
#         interest_amt=self._balance * self._interest_rate
#         self._balance += interest_amt
#         return f"Interest received. {interest_amt}"

# class SavingsAccount(Bank4):
#     interest_rate=0.1

#     # def apply_interest(self):
#     #     interest_amt=self._balance * SavingsAccount.interest_rate
#     #     self._balance += interest_amt
#     #     return f"Interest received. {interest_amt}"



# class Current


# sabesh = SavingsAccount(131,"Sabesh",80_000)
# priya = Bank4(131,"Priya",1_00_000)

# print(sabesh.apply_interest())
# print(priya.apply_interest())

# print(sabesh.display_balance())
# print(priya.display_balance())

from datetime import datetime
# Calculate age & Handle errors
def calc_age(birth_year):
        
    try:        
        age = datetime.now().year - int(birth_year)
        if int(birth_year)>datetime.now().year:
            raise Exception("Are you from Future?")
        return f"Your age is {age}"
        
    except ValueError:
        return f"Give year in numbers"
    
    except Exception as e:
        return f"Check again {e}"


birth_year = input("Please provide your birth year: ")
print(calc_age(birth_year))

