import json

bank_data = """
[
    {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "isActive": true,
        "balance": 150.75
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "janesmith@example.com",
        "isActive": false,
        "balance": 500.50
    },
    {
        "id": 3,
        "name": "Emily Jones",
        "email": "emilyjones@example.com",
        "isActive": true,
        "balance": 0.00
    }
]
"""
# Task 1 (normal for loop)
# All Active user's balance should increase by 10%
# Final Output should be JSON format
bank_dic=json.loads(bank_data)

for dic in bank_dic:
    if dic["isActive"] == True:
            dic["balance"]+=dic["balance"]*0.1

bank_json=json.dumps(bank_dic)
print(bank_json)