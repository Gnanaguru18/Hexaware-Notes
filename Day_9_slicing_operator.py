# # print(quote[<strat>:<end>: <skip>])

# quote="Dream is something"
# print(quote[1:3])
# print(quote[-1])
# print(quote[-4:-1])

# print(quote[1:10:2])     # prints characters by skipping one value
# print(quote[1:10:1])     # prints characters between 1-10 without skipping
# print(quote[::-1])       # gnihtemos si maerD
# print(quote[-1:-4:-1])   # gni

# Task 1: After the 🔑 print the remaining characters in uppercase and compare it with code

# message="     🐫🕑🕝🔑secret_code✌️"
# code="SECRET_CODE✌️"
# position=message.find("🔑")+1
# output=message[position:].upper()

# if(output==code):
#     print("you are an hacker")
# else:
#     print("Try again")


# Task 2: remove junk [ * , ( ] to find the secret code
message="         🔗⌨️😁😏🔑*****secret_code✌️((("
code="SECRET_CODE✌️"
position=message.find("🔑")+1
output=message[position:].upper().strip("*").strip("(")

if(output==code):
    print("you are an hacker")
else:
    print("Try again")