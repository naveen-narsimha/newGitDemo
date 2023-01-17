# dictionary is a unordered collection of data in key:value pair

# dictionary cann be created in many ways

# from pandas import value_counts


# user={
#     "name":"naveen",
#     "age":27,
#     "usn":"1SI19CS086",
#     "college":"SIT,TUMKUR"
# }
# u=dict(name="naveen",age=27,usn="naveen")
# print(user)
# print(u)

# # in dictionary we can store data  like numbers,strings,lists,tuples,dictionary as well
# # how to add data to empty dctionary
# # user_info={}
# # in keyword and looping
# if "age" in user:
#     print("present!!")
# else:
#     print("not present!!")

# # in is used to check the presence of key/

# # while .values of the dictionary is used to check the presence of the value/
# if "naveen" in user.values():
#     print("present!!")
# else:
#     print("not present!!")

# l=list(map(int,input().split(' ')))
# d={i:0 for i in l}
# for i in l:
#     d[i]+=1
# print(d)

# from re import A

# from regex import B


p={12:12,144:21,21:23}
# l=[1,2,2,3,4,4,2,1,2,3,]
# # p.update(d)
# # print(p)

# # to intialize all the values to single comman values use fromkeys method/
# m=dict.fromkeys(l,0)
# print(m)

# print(type(m.get(7)))
# if m.get(7):
#     print("present!!")

# m.clear()
# dd1=m.copy() # this creates a copy of dictionary and both are independent from each other!!
# dd1=m #they are same dictionary operations affect each other!!


# More about get method
# print(p.get(12,"not found"))
# l=5
# d={i:i**3 for i in range(1,l+1)}
# print(d)

# word counter
# s="NaVeEN"
# g={i:(s.lower()).count(i) for i in s.lower()}
# print(g)

# users={
#     'name':'Naveen',
#     'age':21,
#     'fav_movies':['suzhal','avengers','uyare'],
#     'fav_songs':['sanorita','banali badalago'],
# }



# for i in users:
#     print(i,':',users[i])
def swap(s,a,b):
    t=s[a]
    s[a]=s[b]
    s[b]=t

def combine(s,l,r):
    if l==r:
        print(''.join(s))
    for i in range(l,r+1):
        swap(s,l,i)
        combine(s,l+1,r)
        swap(s,l,i)

s='nee'
combine(list(s),0,len(s)-1)
