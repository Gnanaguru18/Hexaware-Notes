# out_act={"Hiking","Cycling","Swimming"}
# in_act={"Gaming","Reading","Cycling"}

# # print(out_act.union(in_act))
# # print(out_act.intersection(in_act))
# # print(out_act.difference(in_act))
# print(out_act.symmetric_difference(in_act))

# all_tech_gadgets={"remote","time machine"}
# new_tech={"charge","watch"}

# all_tech_gadgets.update(new_tech)
# print(all_tech_gadgets)
# all_tech_gadgets.discard("remote")
# print(all_tech_gadgets)

# t1,t2,*t3=(1,2,3,4,5,6,7,8,9)
# print(t1,t2,t3)
# print(type(t3))
# coordinates= [(5,4),(1,1),(6,10),(9,10)]
# distance=[]
# # for a,b in coordinates:
# #     distance.append((a**2+b**2)**0.5)
# #


# distance=[round((a**2 + b**2)**0.5, 2) for a,b in coordinates ]
# print(distance)

# person = {
#     "name": "Lionel Messi",
#     "age": 36,
#     "address": {
#         "city": "rosario",
#         "country": "Argentina",
#     },
#     "sport": "football",
# }

# # print(person["address"])
# # print(person["address"]['city'])

# print(type(person.get("stats",{})))

# # print(person.get("stats").get("city")) 

# person = {
#     "name": "Lionel Messi",
#     "age": 36,
#     "address": {
#         "city": "rosario",
#         "country": "Argentina",
#     },
#     # "stats": {"goals": 300, "assists": 500},
#     "sport": "football",
#     # "height": 168,
# }
 
# # print(person["stats"]["goals"]) # KeyError: 'stats'
# # print(person.get("stats").get("goals")) # 'NoneType' object has no attribute 'get'
 
# # Default value - person.get(key, default value)
# print(person.get("height", 174))
# print(person.get("stats", {}).get("goals"))  # None
# print(person.get("stats", {"goals": 0}).get("goals"))  # None

# employees = [
#     {"name": "Sneha", "experience": 2},
#     {"name": "Manju"},
#     {"name": "Sai Subash", "experience": 4},
#     {"name": "Manasa"},
# ]
 
 
# # Task: After 1 experience
 
 
# for i in employees:
#     i["experience"]=i.get("experience",0)+1
#     if i.get("experience")>=5:
#         i["status"]="Senior"
#     elif i.get("experience")<3:
#         i["status"]="Junior"
#     else:
#         i["status"]="Mid-level"
# print(employees)

# t1=[80,90]
# t2=[50,60]

# t3=[*t1,*t2]

# print(t3)

# movie={"name":"John wick","year":2014}

# mv1= {**movie, "actor":"Keanu Reeves","year":2015}

# print(mv1)
# print(movie)

# library_list = [
#     {
#         "title": "Python Programming",
#         "author": "Eric Matthes",
#         "year": 2019,
#         "available": True
#     },
#     {
#         "title": "Automate the Boring Stuff with Python",
#         "author": "Al Sweigart",
#         "year": 2020,
#         "available": True
#     },
#     {
#         "title": "Learning Python I",
#         "author": "Mark Lutz",
#         "year": 2013,
#         "available": False
#     },
#     {
#         "title": "Fluent Python",
#         "author": "Luciano Ramalho",
#         "year": 2015,
#         "available": True
#     },
#     {
#         "title": "Adavance Python",
#         "author": "Mark Lutz",
#         "year": 2015,
#         "available": False
#     },
# ]

# book = {"title": "Fluent Python II", "author": "Alex", "year": 2016, "available": True}


# def add_book(library, title):
#     for book in library:
#         if book["title"]==title:
#             if(book["available"]=="True"):
#                 book["available"]="False"
#                 return f"Book available"
#             else:
#                 return f"Someone else has it" 
#     return f"No such book"
  
# print(add_book(library_list,"abc"))
# Import package 



# movies = [
#     {"title": "Inception", "ratings": [5, 4, 5, 4, 5]},
#     {"title": "Interstellar", "ratings": [5, 5, 4, 5, 4]},
#     {"title": "Dunkirk", "ratings": [4, 4, 4, 3, 4]},
#     {"title": "The Dark Knight", "ratings": [5, 5, 5, 5, 5]},
#     {"title": "Memento", "ratings": [4, 5, 4, 5, 4]},
# ]

# def cal_avg(movie):
#     return sum(movie["ratings"])/len(movie["ratings"])
 
# def get_movies_avg_rating(movies):
#     for movie in movies:
#         movie["average rating"]=cal_avg(movie)
#     return movies

# pprint(get_movies_avg_rating(movies))


 
# Task 2 - break it into 2 functions
from pprint import pprint
 
def own_max(*nums):
    big=nums[0]
    for i in nums:
        if big<i:
            big=i
    return big
 
 
pprint(own_max(5, 6, 10))
pprint(own_max(5, 6, 10, 7, 80, 60))