# # Online Python compiler (interpreter) to run Python online.
# # Write Python 3 code in this online editor and run it.
# print("Hello world")

lst1=list()
# lst2=[]
# print(lst1,lst2)
# print(tuple(lst1),tuple(lst2))
def search(lst,key):
    for i in range(len(lst)):
        if lst[i]==key:
            return i
    return -1
def binarysearch(lst,key):
    high=len(lst)-1
    low=0
    while(high>low):
        mid=(high+low)//2
        if(lst[mid]==key):
            return mid
        elif(lst[mid]>key):
            high=high-1
        else:
            low=low+1
    return -1
# while(True):
    # x=eval(input("enter numbers:"))
    # if(x<0):
    #     break
    # lst1.append(x)
lst1=list(eval(input("Enter numbers as comma separated values:")))
x=eval(input("Please enter key to search:"))
ind=search(lst1,x)
print(lst1)
if ind!=-1:
    print("Key found at index:",ind)
else:
    print("Key not found!!!")
lst1.sort()
print(lst1)
ind=binarysearch(lst1,x)  # sort function does not return anything!!!!!!
if ind!=-1:
    print("Key found at index:",ind)
else:
    print("Key not found!!!")

