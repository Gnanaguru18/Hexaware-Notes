# person=("Sakura","leaf village",20,20)

# print(person[0],person[1])

# person[0]="Sneha"   ❌  

# Modification is not allowed


# empty_dict={}                # empty dictionary
# tech_gad={"smartphone","laptop","smartwatch"}
# empty_set=set()

# print(type(tech_gad))            # <class 'set'>
# print(type(empty_set))             # <class 'set'>

# print(tech_gad)

# tech_gad.add("Omiscient reader")
# tech_gad.add("laptop")
# print(tech_gad)

colors=["red","blue","red","green","pink","blue"]

unique_color=set()
for color in colors:
    unique_color.add(color)
print(unique_color)