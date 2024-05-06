# #Dictionary
# person={
#     "name": "Lionel Messi",
#     "age":36,
#     "country":"Argentina",
#     "Sport":"Football"
# }

# # Access value
# print(person["name"])
# print(person["age"])

# print(type(person))

# # Update value
# person["age"]+=1

# # Methods
# print(person.keys())
# print(person.values())

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
#task 1
hi_books=[]
for book in books:
    if book["rating"]>=4.7:
        hi_books.append(book["title"])
print(hi_books)
# task 2
hii_books=[book["title"] for book in books if book["rating"]>=4.7]
print(hii_books)