import sys
from math import gcd


# Given an array, we have to find the largest element in the array.
# TC : O(N)
# SC : O(1)
def largestNum(l):
    maxEle=-sys.maxsize-1
    for i in l:
        if maxEle<i:
            maxEle=i
    print(maxEle)
    return maxEle


# Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.
# TC : O(NlogN + N) -- NlogN for sorting, N for worst case second largest number is not present or at 0 index
# SC : O(1)
def secondLargestNumBF(l):
    if len(l)<2:
        print(-1)
        return -1
    l.sort()
    n=len(l)
    largest=l[n-1]
    secondLargest=0
    for i in range(n-2,-1,-1):
        if l[i]<largest:
            secondLargest=l[i]
            break
    print(secondLargest)

# TC : O(N+N) --  N for 1st pass finiding largest , N for 2nd pass finding second largest
# SC : O(1)
def secondLargestNumBetter(l):
    largest=-sys.maxsize- 1
    for i in l:
        if largest < i:
            largest = i
    secondLargest=-sys.maxsize- 1
    for i in l:
        if i<largest and secondLargest<i:
            secondLargest=i

    print(secondLargest)
    return(secondLargest)

# TC : O(N) -- N for iterating over N to find largest and second largest
# SC : O(1)
def secondLargestNumOptimal(l):
    largest = l[0]
    secondLargest = -sys.maxsize - 1
    for i in l:
        if largest<i:
            secondLargest=largest
            largest=i
        elif i<largest and i>secondLargest:
            secondLargest = i
    print(largest,secondLargest)

# # check if array is sorted
# TC : O(N)
# SC : O(1)
def checkArraySorted(l):
    for i in range(1,len(l)):
        if l[i-1]>l[i]:
            return False
    return True

# # Remove duplicates from sorted array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# TC : O(NlogN+N)  -- NlogN for adding elements into set (Set always stores in ascending order) , N for updating in given array
# SC : O(N)  -- set with size of N
def removeDupSortBF(l):
    s=list(set(l))
    for i in range(len(s)):
        l[i]=s[i]
    print(l)
    return len(s) #unique elemnts

#TC : O(N) - N for iterating over array
#SC : O(1)
def removeDupSortOptimal(l):
    n = len(l)
    i = 0
    j = 0
    while j < n:
        if l[i] < l[j]:
            i += 1
            l[i] = l[j]
        else:
            j += 1
    print(l)
    return i + 1 #unique elemnts


# Left Rotate an array by one place
def leftRotateByOne(l):
    n=len(l)
    ele=l[0]
    for i in range(1,n):
        l[i-1]=l[i]
    l[n-1]=ele
    print(l)

# Given an array of integers, rotating array of elements by k elements either left or right.
# TC : O(k*N) -- Rotating K times , each time rotating complete array N
# SC : O(1)
def RotateByKBF(l,k,side):
    n=len(l)
    k=k%n
    if side=='left':
        for _ in range(k):
            ele=l[0]
            for i in range(1,n):
                l[i-1]=l[i]
            l[n-1]=ele
    else:
        for _ in range(k):
            ele=l[n-1]
            for i in range(n-2,-1,-1):
                l[i+1]=l[i]
            l[0]=ele
    print(l)

# k=3 , n=7 left
# 1 2 3 4 5 6 7
#step 1 : copying the k elements that need to shifted to one end to other end of array in to temp
# temp 1 2 3
#step 2: Shift the remaining elements by k which just shifts to the direction
# 1 2 3 4 5 6 7
# 4 5 6 7 5 6 7 - after shift
#step 3: Now update the k elements using temp that shifted to opposite side
# 4 5 6 7 1 2 3
#TC : O(d+N) - d for step 1, N for step 2 and step 3
#SC : O(d) - temp array
def RotateByKBetter(l,k,side):
    n = len(l)
    k = k % n
    if side == 'left':
        temp=[]
        for i in range(k):
            temp.append(l[i])
        for i in range(k,n):
            l[i-k]=l[i]
        for i in range(n-k,n):
            l[i]=temp[i-(n-k)]
    else:
        temp=[]
        for i in range(n-k,n):
            temp.append(l[i])
        for i in range(n-(k+1),-1,-1):
            l[i+k]=l[i]
        for i in range(k):
            l[i]=temp[i]
    print(l)

#arr          : 9 4 2 7 6   , d=3
#index        : 0 1 2 3 4
#arr          : 9 4 2 7 6
#indv reversed: (4 9) (6 7 2) , reverse the elements from arrlen-d to arrlen and rev the elements 0 to d
#total reverse: 2 7 6 9 4 , will be same as ans
#Shiftted arr : 2 7 6 9 4

def RotateByKBetterTwo(l,k,side):
    n = len(l)
    k = k % n
    # print(arr)
    # print(arr[d-1::-1])
    # print(arr[:d-1:-1])
    l = l[k-1::-1] + l[:k-1:-1]
    print(l[::-1])



#Using cycle that happpens in shifting
#example : for index shifted by 3 in len of 10 will be
#0-> (0+3) -> 3 -> (3+3) -> 6 -> (6+3) -> 9 -> (9+3)=12%10=2 -> 2 -> (2+3) -> 5 -> (5+3) -> 8 -> (8+3)==11%10=1 -> 1 -> (1+3) -> 4 -> (4+3) -> 7 -> (7+3)=10%10=0
# reached where you start , if you observe it covered all index from 0 to 9

#example : for index shifted by 2 in len of 10 will be
#0-> (0+2) -> 2 -> (2+2) -> 4 -> (4+2) -> 6 -> (6+2) -> (8+2)=10%10=0 ---- end , didn't cover all , now start from next  index
#1 -> (1+2) -> 3 -> (3+2) -> 5 -> (5+2) -> 7 -> (7+2) -> 9 -> (9+2)=11%10=1 -- end , covered all by including both

#which started with O covered all index which are having reminder 0 when len divided by d
#which started with 1 covered all index which are having reminder 1 when len divided by d


#example : for index shifted by 8 in len of 12 will be
#0-> (0+8) -> 8 -> (8+8)=16%12=4 -> 4 -> (4+8)=12%12=0 -- end
#1-> (1+8) -> 9 -> (9+8)=17%12=5 -> 5 -> (5+8)=13%12=1 --end
#2-> (2+8) -> 10 -> (10+8)=18%12=6 -> 6 -> (6+8)=14%12=2 --end
#3-> (3+8) -> 11 -> (11+8)=19%12=7 -> 7 -> (7+8)=15%12=3 --end , covered all index till here


#if you observe they are cycle which are exactly equals to gcd(n,(d%n))

# k=2 n=6
# 1 2 3 4 5 6
#     1   3

# 1 2 3 4 5 6
#         1
def RotateByKOptimal(l,k,side):
    n = len(l)
    k = k % n
    r=gcd(n,k)
    if side == 'left':
        for i in range(r):
            p=i
            prev=l[p]
            while True:
                p=(n+(p-k))%n
                if p==i:
                    break
                ele=l[p]
                l[p]=prev
                prev=ele
            l[i] = prev
    else:
        for i in range(r):
            p=i
            prev=l[i]
            while True:
                p=(p+k)%n
                if p==i:
                    break
                ele=l[p]
                l[p]=prev
                prev=ele
            l[i]=prev
    print(l)


# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# TC : O(2N) = O(N+X+(N-X)) -- N copy the nonzeros to temp ,X Replacing non zero ele in given array , (N-X) Replacing zeros ele in given array
# SC : O(N) - temp size N worst case
def moveZerosToLastBF(l):
    n=len(l)
    temp=[]
    for i in range(n):
        if l[i]!=0:
            temp.append(l[i])
    m=len(temp)
    for i in range(m):
        l[i]=temp[i]
    for i in range(m,n):
        l[i]=0
    print(l)

# TC : O(N+X) -- N for iterating and assigning non zero ele , X for replacing ele to zero in end
# SC : O(1)
def moveZerosToLastBetter(l):
    n=len(l)
    i=0
    for j in range(n):
        if l[j]!=0:
            l[i]=l[j]
            i+=1
    while i<n:
        l[i]=0
        i+=1
    print(l)

#TC : O(N) - N iterating over array N
#SC : O(1)
def moveZerosToLastOptimal(l):
    n = len(l)
    i = 0
    for j in range(n):
        if l[i] == 0:
            if l[j] != 0:
                l[i] = l[j]
                l[j] = 0
                i += 1
        elif l[i] != 0:
            i += 1
    print(l)

def linerSearch(l,k):
    n=len(l)
    for i in range(n):
        if l[i]==k:
            print(i)
            break
    print(-1)



# Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.
#TC : O(n1logn+n2logn+n1+n2) = O(n1logn)+O(n2logn)+O(n1+n2)
#     - O(n1logn) - n1 for ele of arr1 , n in logn is size of set, as it is ordered set takes logn  to insert
#     - O(n2logn) - n2 for ele of arr2 , n in logn is size of set, as it is ordered set takes logn  to insert
#     - O(n1+n2) for inserting ele into union list (worst case - all unique)
# SC : O(n1+n2+n1+n2)= O(n1+n2)+O(n1+n2)
#     - O(n1+n2) - for set size while inserting ele from arr1 and arr2
#     - O(n1+n2) - for transerfing ele from set to union list
def unionOfSortedArraysBF(arr1,arr2):
    s=set()
    union=[]
    for i in arr1:
        s.add(i)
    for j in arr2:
        s.add(j)
    print(list(s))

# TC : O(n+m) - iterating over both arr1 and arr2
# SC : O(n+m) - union/temp arr to return
def unionOfSortedArraysOptimal(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    i=0
    j=0
    temp=[]
    while i<n and j<m:
        if arr1[i]<=arr2[j]:
            if len(temp) == 0 or temp[-1] != arr1[i]:
                temp.append(arr1[i])
            i+=1
        elif arr1[i]>arr2[j]:
            if len(temp) == 0 or temp[-1] != arr2[j]:
                temp.append(arr2[j])
            j+=1
    while i<n:
        if len(temp) == 0 or temp[-1] != arr1[i]:
            temp.append(arr1[i])
        i += 1
    while j<m:
        if len(temp) == 0 or temp[-1] != arr2[j]:
            temp.append(arr2[j])
        j += 1
    print(temp)


#Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. Find the number(between 1 to N), that is not present in the given array.
#TC : O(N*N) = N for loop1 and N for loop in it
#SC : O(1)
def missingNumInArrayBF(l):
    n=len(l)
    for i in range(1,n+1):
        flag=0
        for j in l:
            if j==i:
                flag=1
                break
        if flag==0:
            print(i)
            return i

#TC : O(N) = O(N+N) - N for temp array increment , N for checking temp array
#SC : O(N) - temp array
def missingNumInArrayBetter(l,m):
    n=len(l)
    temp=[0 for i in range(m)]
    for i in l:
        temp[i-1]+=1
    for i in range(n):
        if temp[i]==0:
            print(i+1)

#TC : O(N) - for subtracting N elements
#SC : O(1)
def missingNumInArrayOptimal1(l,m):
    n=len(l)
    sm=m*(m+1)//2
    for i in l:
        sm=sm-i
    print(sm)

#TC : O(N) - xor for n elemnts
#SC : O(1)
def missingNumInArrayOptimal2(l):
    n=len(l)
    xor1=0
    xor2=0
    for i in range(n-1):
        xor1=xor1^l[i]
        xor2=xor2^(i+1)
    xor2=xor2^n
    print(xor1^xor2)


# Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array
#TC : O(N) - iterating over array
#SC : O(1)
def countMaxConsOnes(l):
    cnt=0
    maxcnt=0
    for i in l:
        if i==1:
            cnt+=1
        else:
            maxcnt=max(cnt,maxcnt)
            cnt=0
    maxcnt = max(cnt, maxcnt)
    print(maxcnt)


# Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.
#TC : O(N*N) - iterating over array N and array N for each ele
#SC : O(1)
def numAppersOnceBF(l):
    for i in l:
        c=0
        for j in l:
            if i==j:
                c+=1
        if c==1:
            print(i)
            return i

# TC : O(N+maxele+1) - O(N)+O(N)+O(maxnum+1) - finding max and then hashing , O(maxele+1) - for iterating over hashing array
# SC : O(maxele+1) - maxele is max element in array
def numAppersOnceBetter1(l):
    mxnum=max(l)
    cnt=[0 for i in range(mxnum+1)]
    for i in l:
        cnt[i]+=1
    for i in range(mxnum+1):
        if cnt[i]==1:
            print(i)
            return i

#TC : O(NlogM + M) = O(NlogM) - N times inserting into map of size M (logM for inserting) , O(M) iterating to find ele
#SC : O(M) - M which are twice
def numAppersOnceBetter2(l):
    d={i:0 for i in l}
    # print(d)
    for i in l:
        d[i]+=1
    for i in d:
        if d[i]==1:
            print(i)
            return i

#TC : O(N)
#SC : O(1)
def numAppersOnceOptimal(l):
    xor=0
    for i in l:
        xor=xor^i
    print(xor)


# Given an array and a sum k, we need to print the length of the longest subarray that sums to k.
#TC : O(N*N*N) - each loop runs for N
#SC : O(1)
def longestSubarraySumBF1(l,k):
    n=len(l)
    ans=[]
    maxlen=0
    for i in range(n):
        for j in range(i+1,n):
            s=0
            for t in range(i,j+1):
                s+=l[t]
            # print(s,k)
            if s==k:
                print(l[i:j+1],[i, j])
                if j-i+1>maxlen:
                    maxlen = j - i + 1
                    ans=[i,j]
    print('final',ans,l[ans[0]:ans[1]+1])

#TC : O(N*N) - each loop runs for N , carry forward approach
#SC : O(1)
def longestSubarraySumBF2(l,k):
    n = len(l)
    ans = []
    maxlen = 0
    for i in range(n):
        s=l[i]
        for j in range(i + 1, n):
            s+=l[j]
            if s==k:
                print(l[i:j+1],[i, j])
                if j - i + 1 > maxlen:
                    maxlen=j - i + 1
                    ans = [i, j]
    print('final',ans, l[ans[0]:ans[1] + 1])

# Key Idea: Prefix Sum + Hash Map
# Instead of checking every possible subarray (which would be slow), we use:
# A prefix sum to keep track of the running total while iterating.
# A hash map (dictionary) to store the earliest index where each prefix sum occurred.
# This allows us to quickly calculate if a subarray ending at the current index adds up to k.

# Suppose l = [2, 0, 0, 3] and k = 3
# Prefix sums:
# i = 0 → sum = 2
# i = 1 → sum = 2
# i = 2 → sum = 2
# i = 3 → sum = 5
# We want a subarray that adds up to k = 3, so we look for:
# s - k = 5 - 3 = 2
# 2 was first seen at index 0, not at 2 — using the first occurrence gives the subarray [1,2,3] → [0,0,3], length 3.
# That’s why we store only the earliest index where each prefix sum was seen.

# Summary of Logic:
# Keep track of the sum of elements so far.
# At each step, check if:
# The sum from the beginning to now equals k
# The difference between current sum and k was seen before — that would mean the elements in between sum to k.
# Store the first time each sum appears, so we can get the longest possible subarray when we find a match later

# Why do we not update the notebook if the same sum appears again?
# Because the earlier that sum happened, the longer the possible group ending now will be.
# Updating would overwrite that early clue and make the group shorter!

def longestSubarraySumBetter(l,k):
    n=len(l)
    s=0
    maxlen=0
    ans=[]
    d={}
    for i in range(n):
        s+=l[i]
        if s==k:
            print(l[:i+1],[0,i])
            if maxlen<i+1:
                maxlen = i+1
                ans=[0,i]
        t=s-k
        if t in d:
            p=d[t]
            print(l[p+1:i+1],sum(l[p+1:i+1]),[p+1,i])
            if maxlen<i-p:
                maxlen = i-p
                ans=[p+1,i]
        if s not in d:
            d[s]=i
    print('final',ans,l[ans[0]:ans[1]+1])

def longestSubarraySumOptimal(l,k):
