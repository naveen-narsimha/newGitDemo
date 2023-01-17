 #Bit wise xor is best find the single number which is repeated odd numberof times in the given list.
# l=[14,15]
# s=1
# for i in l:  # any multiple of 4 gives same value after xor from 1 to that number.
#     s&=i
# print(s)
# s=1
# print(s&1)

# s=4
# count=0
# while s:
#     s>>=1
#     count+=1
# print(count-1)
# ~ performs 2s complement  

#Add two numbers without using addition operator
# a=61234
# b=51345
# print(a+b)
# print((a|b)+(a&b))

#Swap two number without using third variable

# a=123
# b=321
# print(a,b)
# a=a^b
# b=a^b
# a=a^b
# print(a,b)

# l=[1,2,3,4,5,6,5]
# t=0
# for i in range(1,7):
#     t^=i
# s=0
# for i in l:
#     s^=i
# print(s^t)
# /// subset generation
nums="abc"
n=len(nums)
l=[]
print('0'*3)
print(len(bin(2)))
for i in range(2**n):
    l.append('0'*((n-(len(bin(i))-2)))+bin(i)[2:])
a=[]
subset=[]
for i in l:
    a=[]
    for j in range(n):
        if i[j]=='1':
            a.append(nums[j])
    if len(a)!=0:
        s=''.join(a)
        subset.append(s)
        s=""
subset.sort()
print(subset)