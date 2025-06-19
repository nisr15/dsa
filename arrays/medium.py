# Given an array of integers arr[] and an integer target.
# 1st variant : return yes or no
# 2nd variant : return indexs

#both 1st and 2nd BF
#TC : O(N*N)
#SC : O(1)
def sumOfTwoNumbersBF(l,k):
    n=len(l)
    for i in range(n):
        for j in range(i+1,n):
            if l[i]+l[j]==k:
                print(i,j)
                return [i,j]
    print(-1,-1)

#better for 1st
#Optimal for 2nd
#TC : O(N) - unordered map -- worst case when we have mutiple colisions O(N*N)
# O(NlogN) - ordered map
# SC : O(N) - map
def sumOfTwoNumbersBetter(l,k):
    n=len(l)
    d={}
    for i in range(n):
        t=k-l[i]
        if t in d:
            print(i,d[t])
            return [i,d[t]]
        if l[i] not in d:
            d[l[i]]=i
    print(-1,-1)

#Optimal for 1st
#not optimal and not prefered for 2nd variant
#TC : O(NlogN+N) - NlogN - sorting , N - two pointers
#SC : O(1)
def sumOfTwoNumbersOptimal(l,k):
    n=len(l)
    l.sort()
    i=0
    j=n-1
    while (i<j):
        if l[i]+l[j]<k:
            i+=1
        elif l[i]+l[j]>k:
            j-=1
        else:
            print(l[i],l[j])
            return [l[i],l[j]]

        
