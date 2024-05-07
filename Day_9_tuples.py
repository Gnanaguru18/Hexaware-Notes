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

# colors=["red","blue","red","green","pink","blue"]

# unique_color=set()
# for color in colors:
#     unique_color.add(color)
# print(unique_color)



# 

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
coordinates= [(5,4),(1,1),(6,10),(9,10)]
distance=[]
for a,b in coordinates:
    #a,b=points
    distance.append((a**2+b**2)**0.5)
print(distance)
