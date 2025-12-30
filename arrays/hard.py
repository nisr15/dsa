##Write a program to generate Pascal's triangle. Give the nth line of Pascal’s triangle
# TC : O(N*N)
# SC : O(N*N)
from collections import Counter


def nthLineOfPascalTriangleBruteForce(n):
    if n==1:
        return [[1]]
    elif n==2:
        return [[1,1]]
    else:
        l=[[1],[1,1]]
        for j in range(n-2):
            k=l[-1]
            t=len(k)
            p=[1]
            for i in range(t-1):
                p.append(k[i]+k[i+1])
            p.append(1)
            l.append(p)
        return l[-1]

# TC : O(N-1)
# SC : O(N)
def nthLineOfPascalTriangleOptimal(n):
    r=n-1
    c=0
    res=1
    l=[res]
    for i in range(r):
        res=res*(r-i)
        res=res//(i+1)
        l.append(res)
    return l


#Return all elements which appear more than n/3 times in the array

# TC : O(N*N)
# SC : O(1)
def eleMoreThanBruteForce(nums):
    n=len(nums)//3
    ans=[]
    for i in nums:
        if len(ans)==0 or ans[0]!=i:
            c=0
            for j in nums:
                if i==j:
                    c+=1
            if c>n:
                ans.append(i)
        if len(ans)==2:
            break
    return ans

# TC : O(N*logN)  insertion in the map takes logN time, and we are doing it for N elements
# SC : O(N)
def eleMoreThann3Better(nums):
    n = len(nums) // 3
    d = Counter(nums)
    ans = []
    for i, j in d.items():
        if j > n:
            ans.append(i)
    return ans

#TC : O(N)
#SC : O(1)
def eleMoreThann3Optimal(nums):
    n=len(nums)
    r=n//3
    cnt1=0
    cnt2=0
    ele1=0
    ele2=0
    for i in nums:
        if cnt1==0 and ele2!=i:
            ele1=i
            cnt1+=1
        elif cnt2==0 and  ele1!=i:
            ele2=i
            cnt2+=1
        elif ele1==i:
            cnt1+=1
        elif ele2==i:
            cnt2+=1
        else:
            cnt2-=1
            cnt1-=1

    cnt1=0
    cnt2=0
    for i in nums:
        if i==ele1:
            cnt1+=1
        if i==ele2:
            cnt2+=1
    ans=[]
    if cnt1>r:
        ans.append(ele1)
    if cnt2>r and ele1!=ele2:
        ans.append(ele2)
    return ans


# Find unique triplets that add up to give a sum of zero

def threeSumBruteForce(l,n):
    ans=set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if l[i]+l[j]+l[k]==0:
                    p=tuple(sorted([l[i],l[j],l[k]]))
                    ans.add(p)
    return [list(i) for i in ans]


def threeSumBetter(l,n):
    ans=set()
    for i in range(n):
        s=set()
        for j in range(i+1,n):
            r=-l[i]-l[j]
            if r in s:
                p=tuple(sorted([l[i],l[j],r]))
                ans.add(p)
            s.add(l[j])
            # print(s)
    return [list(i) for i in ans]

def threeSumOptimal(l,n):
    ans=set()
    l.sort()
    for i in range(n):
        if i>0 and l[i]==l[i-1]:
            continue
        j=i+1
        k=n-1
        while(j<k):
            if l[i]+l[j]+l[k]==0:
                p=tuple(sorted([l[i],l[j],l[k]]))
                ans.add(p)
                j+=1
                k-=1
                while j<k and l[j]==l[j-1]:
                    j+=1
                while j<k and l[k]==l[k+1]:
                    k-=1
            elif l[j]+l[k]<-l[i]:
                j+=1
            elif l[j]+l[k]>-l[i]:
                k-=1
    return [list(i) for i in ans]





