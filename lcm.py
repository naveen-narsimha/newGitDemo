n=5
l=[2,3,4,6,7]
cnt=True
while cnt:
    i=0
    while i<(n-1):
        m=l[i]
        p=l[i+1]
        while p!=0:
            l=p
            p=m%p
            m=l
        hcf=m
        if hcf!=1:
            lcm=(l[i]*l[i+1])/hcf
            del l[i]
            l[i+1]=lcm
            cnt=False
    if cnt==False:
        cnt=True
        
        