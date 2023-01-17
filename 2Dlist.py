# m=[]
# r=eval(input("enter the row size: "))
# c=eval(input("enter the column size: "))
# for i in range(r):
#     l=list(int(i) for i in input().split())
#     m.append(l)
# # print(m)

# p=tuple()
# print(p)
# print('address: ',id(p))
l=1,2,3,3
# m=() #empty tuple intialization
# d={}  #empty dictionary intialization
# print('type of d:',type(d))
# print('type of m:',type(m))
# print(l)
# print(type(l))
# p=l # this statement makes p to take the reference of l
# print('address: ',id(p))
# print('address: ',id(l))

# l=[1,2,1,1]
# print('Address of l:',id(l))
# q=l #if copy l to q then only q takes the reference of l i.e modify l with q  
# print('Address of q:',id(q))
# q.append(12)
# print('Address of q:',id(q))
# print('Address of l:',id(l))
# print(l)  

# print(l.count(1))
# print(l.index(2))
# print(len(l))
p=1, # is a tuple  whereas 1 is an int type
print(type(p)) #return type of any function is tuple.
print(p,'Type:',type(p))

# import random
# l=list(random.randint(i,12) for i in range(5))
# print(l)
# print(l[-2:2])
# print(l[2:2])
# print(l[-2:2])
# print(l[-2:-4])
# print(l[-4:-2]) # always slicing happens from left to right
# print(l[2:4])

# l=1,2,3,4
# print(l[2:]) #slicing is possible with respect to tuple

# lst=list(l)
# lst.append(23)
# lst.insert(1,1)
# m=lst.copy()
# print(lst)
# print('Address of m:',id(m))
# print('Address of lst:',id(lst))

# l=list(input().split()) # split the string  1   1 1 1 1 1    1 2 3 23 
# #                                           1_1_1_1_1_1_1_2_3_23

# print('_'.join(l))

# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset) 
import random

s=list()
for i in range(20):
    s.append(random.randint(1,20))
print(s)

l=[i for i in range(15) if i%2==0]
p=set(l)
s=set(s)
print('s:',sorted(list(s)))
print('p:',sorted(list(p)))
print('s difference p',s.difference(p))
print('s-p:',s-p)
print('s intersection p:',s.intersection(p))
print('s union p:',s.union(p))
#print('s intersection_update p:',s.intersection_update(p))
print('s:',sorted(list(s)))


