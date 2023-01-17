# # l=[1,2,3,3,2,1]
# from operator import methodcaller
# from os import remove
# import re


# k=[1,5,3,2,5,6]
# # m=k+l
# # print(m)
# # k.extend(l)
# # print(k)
# # print(l)
# # n=int(input())
# # m=[]
# # l=[]
# # while n:
# #     l=input().split('\n')
# #     l=l.split()
# #     m.append(l)
# #     n-=1
# # print(m)

# # k.pop()#removes last element from the list
# # print(k)
# # print(k.pop(2)) #this is usefull if u know the index to delete
# # print(k)
# # del k[2] #
# # print(k)
# # # print(del k[0])
# # # del k
# # for i in k:
# #     print(i,end=" ")
# #     k.remove(k[-1])
# # print(k)
# # k.remove(k[-1])
# # print(k)

# # some more list methods

# # sort method
# nums=['sf','uewu','jh','ahfh']
# mims=nums
# kims=[]
# kims.extend(nums) ////////////////////////////////////////////////////////////////////
# # nums.sort()# sort method sorts the given list permanently
# # print(nums)
# # print(sorted(kims)) # sorted function can be used to temporaraly sort the list
# # print(kims)
# print(kims.count('uewu'))
# kims.clear() #removes all the elements 
# print(kims) 
# mims.append("naveenjj")
# print(mims[-1::-1])
# # mims.sort(reverse=True)
# # print(mims)
# print(sorted(mims,reverse=True))
# print(mims)
# #
# k=l=[1,2,3,4,5,6,7]
# # k=[4,2,1,7,6,3,5]
# if l==k:
#     print("YES")
# else:
#     print("NO")
# print(k is l)

# split method ////////////////////////////
# user=input()
# u=user.split(' ')
# l=[]
# for i in u:
#     l.append(int(i))
# print(l)
# k=[]
# k='232425627829'
# m=k.split('2')
# print('2'.join(m))
# print(k)



# list are mutable and string are immutable

# s="naVveEn"
# b=s.replace('v','b',2)
# part=s.partition('v')
# slices=s.swapcase()
# print(s.casefold())
# print(s[2])
# print(s)
# print(b)
# print(part)
# print(slices)
# a=[12,3,3,4,4]
# print(a.pop(1))

# a='A'
# for i in range(12):
#     print(str(a),end=" ")
#     b=int(a)
#     b+=1
#     a=b

# import string


# for letter in string.ascii_lowercase:
    # print(letter,end=" ")

# def square(l):
#     l=[i*i for i in l]
#     return l

# def rev(l):
#     p=[]
#     for i in range(len(l)):
#         p.append(l.pop())
#     return p
# l=[1,2,3,4,5,6,7,8,9]
# m=l[::-1]
# print(rev(l))
# print(m)

# l=[input().split('\n')]
# m=[l[i].split(' ') for i in len(l)]
# from itertools import count


# l=[1,2,3,[3,2,4,5],[1],[133,42,2],1,2,3]
# count=0
# for i in l:
#     if type(i) is list:
#         count+=1
# print(count)
# print(l)
# m=list(map(int,input().split(' ')))

# for i in range(len(l)):
#     l[i]=l[i][::-1]
# print(l)
# p=[]
# m=[]
# for i in l:
#     if (int(i))%2==1:
#         p.append(i)
#     else:
#         m.append(i)
# del l
# l=[p,m]      
# # l.append(p)
# # l.append(m)
# print(l)
# res=[]
# for i in range(len(l)):
#     for j in range(len(m)):
#         if l[i]==m[j]:
#             if l[i] not in res:
#                 res.append(l[i])
#             break
# print(res)

# print(max(l)-min(l))
# past_Ind=0
# last=1
# l=[2,3,1,1,2,4,2,0,1,1]
# N=len(l)
# cnt=0
# while last<N:
#     if(past_Ind==last):
#         break
#     m=max(l[past_Ind:last])
#     if m==0:
#         cnt=-1
#         break
#     past_Ind=l.index(m)+1
#     last=past_Ind+m
#     cnt+=1
# print(cnt)
p=[0]*10
print(p)