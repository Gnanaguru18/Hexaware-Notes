# countdown=1
# while countdown<6:
#     print(countdown)
#     countdown+=1

# count=1
# n=int(input("Enter number"))
# while count<n+1:
#     print("✨"*count)
#     count+=1

# n=int(input())
# for i in range(1,n+1):
#     print("✨"*i)

# stats=[10,20,30]
# new_stats=[]
# for i in stats:
#     new_stats.append(i*2)
# print(stats)
# print(new_stats)
avengers = ["Hulk","Iron man","Black widow","Captain america","Spider man","Thor"]   
length=[]
# for i in avengers:
#     length.append(len(i))
# print(length)

# new_length=[count for count in length if count>10]
# print(new_length)

# big_name=[]
# for avenger in avengers:
#     if len(avenger)>10:
#         big_name.append(avenger)
# print(big_name)

big_name1=[avenger for avenger in avengers if len(avenger)>10 ]
print(big_name1)