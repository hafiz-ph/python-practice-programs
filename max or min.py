def findmax_min(l,n):
    if n==1:
        return l[0],l[0]

    minv,maxv=findmax_min(l,n-1)
    c=l[n-1]
    if c<minv:
        minv=c
    if c>maxv:
        maxv=c
    return minv,maxv
l=list(map(int,input("arr:").split()))
minv,maxv=findmax_min(l,len(l))
print("minmum",minv)
print("maximun",maxv)
