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
# TC : O(N3) -- N*N*N - for 3 for loops ,
# SC : O(2*k) -- k= list of unique triplets stored in ans on is for set and other for list
def threeSumBruteForce(l,n):
    ans=set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if l[i]+l[j]+l[k]==0:
                    p=tuple(sorted([l[i],l[j],l[k]]))
                    ans.add(p)
    return [list(i) for i in ans]

# TC : O(N2) -- N*N - for 2 for loops ,
# SC : O(2*k+N) -- k= list of unique triplets stored in ans on is for set and other for list, N - for set
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

# TC : O(NlogN + N2) -- NlogN - sorting , N*N - for 1 for loop and a while loop with 2 points
# SC : O(k) -- k= list of unique triplets stored in ans
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

# Find unique 4 numbers that add up to give a sum of target
# TC : O(N4) -- N*N*N*N - for 4 for loops ,
# SC : O(2*k) -- k= list of unique triplets stored in ans on is for set and other for list
def fourSumBruteforce(nums,target):
    n = len(nums)
    ans = set()
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                for d in range(c + 1, n):
                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        p = tuple(sorted([nums[a], nums[b], nums[c], nums[d]]))
                        ans.add(p)
    return [list(i) for i in ans]

# TC : O(N3) -- N*N*N - for 3 for loops ,
# SC : O(2*k+N) -- k= list of unique triplets stored in ans on is for set and other for list ,  N - for set
def fourSumBetter(nums,target):
    n = len(nums)
    ans = set()
    for a in range(n):
        for b in range(a + 1, n):
            mp = set()
            for c in range(b + 1, n):
                r = target - nums[a] - nums[b] - nums[c]
                if r in mp:
                    p = tuple(sorted([nums[a], nums[b], nums[c], r]))
                    ans.add(p)
                mp.add(nums[c])
    return [list(i) for i in ans]

# TC : O(N3) -- N*N - for 2 for loops ,N - for while loop with 2 pointers
# SC : O(k) -- k= list of unique triplets stored in ans on is for set and other for list
def fourSumOptimal(nums,target):
    n = len(nums)
    nums.sort()
    ans = []
    for a in range(n):
        if a > 0 and nums[a] == nums[a - 1]:
            continue
        for b in range(a + 1, n):
            if b > a + 1 and nums[b] == nums[b - 1]:
                continue
            r = target - nums[a] - nums[b]
            j = b + 1
            k = n - 1
            while j < k:
                if nums[j] + nums[k] == r:
                    ans.append([nums[a], nums[b], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                if nums[j] + nums[k] < r:
                    j += 1
                if nums[j] + nums[k] > r:
                    k -= 1
                # print(ans)
    return ans

# find the length of the longest subarray with the sum of all elements equal to zero.
# TC : O(N*N) - 2 for loops
# SC : O(1) - no extra space
def largestSubArraySumWithZeroBruteforce(l,n):
    maxLen=0
    for i in range(n):
        s=0
        for j in range(i,n):
            s+=l[j]
            if s==0:
                maxLen=max(maxLen,j-i+1)
    return maxLen

#TC : O(N) - 1 for loop
# SC : O(N) - hash map/dict
def largestSubArraySumWithZeroOptimal(l,n):
    s=0
    d={}
    maxLen=0
    for i in range(n):
        s+=l[i]
        if s==0:
            maxLen=max(maxLen,i+1)
        else:
            if s in d.keys():
                k=d[s]
                maxLen=max(maxLen,i-k)
            d[s]=d.get(s,i)
    return maxLen


#Find the total number of subarrays having bitwise XOR of all elements equal to k.
#TC - O(N*N) - 2 for loops
#SC - O(1)
def noOfSubarraysHavingBitwiseXORBruteforce(l,target):
    n=len(l)
    c=0
    for i in range(n):
        s=0
        for j in range(i,n):
            s=s^l[j]
            if s==target:
                c+=1
    return c

#TC - O(N) - 1 for loop
#SC - O(N) - hash map/dict
def noOfSubarraysHavingBitwiseXOROptimal(l,target):
    n=len(l)
    c=0
    s=0
    d={}
    for i in range(n):
        s=s^l[i]
        if s==target:
            c+=1
        else:
            k=s^target
            if k in d.keys():
                c+=d[k]
            else:
                d[s]=d.get(s,0)+1
    # print(c)
    return c

# merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

# TC : O(NlogN + 2N) NlogN - for sorting , N - while merging, N - after merging
# SC : O(N) - worst case all are diff intervals
def mergeIntervalsBetter(l):
    l.sort()
    n=len(l)
    ans=[]
    for i in range(n):
        start=l[i][0]
        end=l[i][1]
        if len(ans) and end<=ans[-1][1]:
            continue
        for k in range(i+1,n):
            if l[k][0]<=end:
                end=max(end,l[k][1])
            else:
                break
        ans.append([start,end])
    return ans


# TC : O(NlogN + N) NlogN - for sorting , N - N=while merging
# SC : O(N) - worst case all are diff intervals
def mergeIntervalsBetter2(l):
    l.sort()
    n = len(l)
    ans = []
    i=0
    while(i<n):
        start = l[i][0]
        end = l[i][1]
        j=i+1
        while(j<n):
            if l[j][0] <= end:
                end = max(end, l[j][1])
                j+=1
            else:
                break
        ans.append([start, end])
        i=j
    return ans

# TC : O(NlogN + N) NlogN - for sorting , N - N=while merging
# SC : O(N) - worst case all are diff intervals
def mergeIntervalsOptimal(l):
    l.sort()
    n=len(l)
    ans=[]
    for i in range(n):
        start=l[i][0]
        end=l[i][1]
        if len(ans)==0 or ans[-1][1]<start:
            ans.append(l[i])
        else:
            ans[-1]=[ans[-1][0],max(end,ans[-1][1])]
    return ans


# merge both the arrays into a single array sorted in non-decreasing order.
# The final sorted array should be stored inside the array nums1 and it should be done in-place.

# TC : O(N+M)
# SC : O(1) 
def mergeTwoSortedArraysWithoutExtraSpace(nums1,nums2,m,n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while (i >= 0 and j >= 0):
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while (j >= 0):
        nums1[k] = nums2[j]
        k -= 1
        j -= 1
    # print(nums1,nums2)
    return nums1


#Given an integer array nums of size n containing values from [1, n] and each value appears exactly once in the array, except for A, which appears twice and B which is missing.

#TC : O(N*N)
#SC : O(1)
def repeatingAndMissingNumbersBruteforce(l):
    n=len(l)
    for i in range(n):
        c=0
        for j in l:
            if i==j:
                c+=1
        if c==2:
            rn=i
        if c==0:
            mn=i
    return [rn,mn]



def repeatingAndMissingNumbersBruteforce(l):
    n=len(l)
    s=sum(l)
    r=(n*(n+1))//2
    for i in range(n):
        c=0
        for j in l:
            if i==j:
                c+=1
                if c>1:
                    rn=j
                    return [rn,r-s+rn]

#TC : O(N+N)
#SC : O(N)
def repeatingAndMissingNumbersBetter(l):
    n=len(l)
    cntArr=[0 for i in range(n)]
    for i in l:
        cntArr[i-1]+=1
    for i in range(n):
        if cntArr[i]==2:
            rn=(i+1)
        if cntArr[i]==0:
            mn=(i+1)
    return [rn,mn]

#TC : O(N)
#SC : O(N)
def repeatingAndMissingNumbersBetter2(l):
    n=len(l)
    p=set()
    s = sum(l)
    r = (n*(n+1))//2
    for i in l:
        if i in p:
            return [i,r-s+i]
        else:
            p.add(i)

#TC : O(N)
#SC : O(1)
def repeatingAndMissingNumbersOptimal(l):
    n = len(l)
    s = (n * (n + 1)) // 2
    s2 = (n*(n+1)*((2*n)+1))//6
    s1 = 0
    s21 = 0
    for i in l:
        s1+=i
        s21=s21+(i*i)
    val1=s1-s
    val2=(s21-s2)//val1
    rn=(val1+val2)//2
    mn=rn-val1
    return [rn,mn]

# TC : O(N) - N - one for loop
# SC : O(1)
# https://www.youtube.com/watch?v=2D0D8HE6uak
def repeatingAndMissingNumbersOptimal2(l):
    n=len(l)
    xr=0
    for i in range(n):
        xr=xr^l[i]
        xr=xr^(i+1)
    k=1<<xr.bit_length()-1
    ans1=0
    ans2=0
    for i in range(n):
        if l[i]&k==k:
            ans1=ans1^l[i]
        else:
            ans2=ans2^l[i]
        if (i+1)&k==k:
            ans1=ans1^(i+1)
        else:
            ans2 = ans2^(i+1)
    c=0
    for i in l:
        if ans1==i:
            c+=1
    if c==2:
        return [ans1,ans2]
    else:
        return [ans2,ans1]


#Given an array of N integers, count the inversion of the array (using merge-sort).

def countInversion(l,n):
    c=0
    for i in range(n):
        for j in range(i+1,n):
            if l[i]>l[j]:
                c+=1
    return c