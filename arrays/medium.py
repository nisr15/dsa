# Given an array of integers arr[] and an integer target.
# 1st variant : return yes or no
# 2nd variant : return indexs
import sys


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

# Given an array consisting of only 0s, 1s, and 2s.
# Write a program to in-place sort the array without using inbuilt sort functions. ( Expected: Single pass-O(N) and constant space)

#TC : O(NlogN)
#SC : O(1)
def sortingArrayOf012BF(arr):
    #merge sort
    pass

#TC : O(n+n)  - n for counting , n for updating arr
#SC : O(1)
def sortingArrayOf012Better(arr,arrlen):
    cnt0=0
    cnt1=0
    cnt2=0
    for i in arr:
        if i==0:
            cnt0+=1
        elif i==1:
            cnt1+=1
        else:
            cnt2+=1
    k=0
    for i in range(cnt0):
        arr[k]=0
        k+=1
    for i in range(cnt1):
        arr[k]=1
        k+=1
    for i in range(cnt2):
        arr[k]=2
        k+=1
    return arr

# TC : O(N)  only iterates once over array by 3 pointers
# SC : O(1) no extra space
def sortingArrayOf012Optimal(arr,arrLen):
    i=0  # points to starting of 1
    j=0  # points to ending of 1 + 1 (starting unsorted numbers)
    k=arrLen-1 # points to starting of 2 -1 (end of unsorted numbers)
    while k>=j:
        if arr[j]==1:
            j+=1
        elif arr[j]==0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j+=1
        elif arr[j]==2:
            arr[j],arr[k]=arr[k],arr[j]
            k-=1
    return arr


# Given an array of N integers, write a program to return an element that occurs more than N/2 times in the given array.
# You may consider that such an element always exists in the array.

#TC : O(N*N) two for loops
#SC : O(1)
def majorityEleBF(arr,arrLen):
    for i in arr:
        c=0
        for j in arr:
            if i==j:
                c+=1
        if c>(arrLen/2):
            return  i

#TC : O(NlogN) merge sort
#SC : O(1)
def majorityEleBetter1(arr,arrLen):
    #merge sort or any sort which takes nlogn
    arr.sort()
    return arr[arrLen//2]

#TC : O(N+N/2)=O(N) n - iterated over arr for to populate dict , (n/2)-to find the number
#SC : O(N) size of dict
def majorityEleBetter2(arr,arrLen):
    d={}
    for i in arr:
        if d.get(i):
            d[i]+=1
        else:
            d[i]=1
    for i in d.keys():
        if d[i]>arrLen//2:
            return i

#moores voting algo
# when maxele is always n/2 so when we cancel count of max and other ele we will get atleast 1
# so here we assume 1st ele as ans and traverse if you see same ele increase cnt
# if you see different ele sub cnt , once cnt reaches 0, we realise it may not be ans , but one it made 0 may be
# so we update that as ans and cnt=1
#TC : O(N) iterating only once
#SC : O(1)
def majorityEleOptimal(arr,arrLen):
    c=1
    ans=arr[0]
    for i in range(1,arrLen):
        if ans==arr[i]:
            c+=1
        else:
            c-=1
            if c==0:
                ans=arr[i]
                c=1
    return ans


#Given an integer array arr, find the contiguous subarray (containing at least one number)
# which has the largest sum and returns its sum and prints the subarray

#TC:O(N*N*N)
#SC:O(1)
def largestSumSubArrayBF(arr,arrlen):
    maxSum=-sys.maxsize-1
    startIndex=0
    endIndex=0
    for i in range(arrlen):
        for j in range(i,arrlen):
            s=0
            for k in range(i,j+1):
                s+=arr[k]
            if s>maxSum:
                maxSum=s
                startIndex=i
                endIndex=j
    print(startIndex,endIndex,maxSum)

#TC:O(N*N)
#SC:O(1)
def largestSumSubArrayBetter(arr,arrlen):
    maxSum = -sys.maxsize-1
    startIndex = 0
    endIndex = 0
    for i in range(arrlen):
        s=0
        for j in range(i,arrlen):
            s+=arr[j]
            if s>maxSum:
                maxSum=s
                startIndex=i
                endIndex=j
    print(startIndex, endIndex, maxSum)

# when ever prefix sum becomes <0 basicaly it becomes burden to next integer if they are positive, as this decrease there value
# so we make s=0 when we get prefix sum<0 and start from there
#TC:O(N)
#SC:O(1)
def largestSumSubArrayOptimal(arr,arrLen):
    s=0
    maxSum=-sys.maxsize-1
    for i in range(arrLen):
        s+=arr[i]
        if maxSum<s:
            maxSum = s
        if s<0:
            s=0
    print("maxSub array sum",maxSum)

#TC:O(N)
#SC:O(1)
def largestSumSubArrayOptimalExtended(arr,arrLen):
    s=0
    start=0
    startIndex = -1
    endIndex = -1
    maxSum=-sys.maxsize-1
    for i in range(arrLen):
        s+=arr[i]
        if maxSum<s:
            maxSum = s
            startIndex=start
            endIndex=i
        if s<0:
            s=0
            start=i
    print(startIndex+1,endIndex,maxSum)


#You are given an array of prices where prices[i] is the price of a given stock on an ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

#TC:O(N*N)
#SC:O(1)
def stockBuyAndSellBF(arr,arrLen):
    maxProf=0
    for i in range(arrLen):
        for j in range(i+1,arrLen):
            if arr[j]-arr[i]>maxProf:
                maxProf=arr[j]-arr[i]
    print(maxProf)

#TC:O(N)
#SC:O(1)
def stockBuyAndSellOptimal(arr,arrLen):
    low=sys.maxsize
    high=sys.maxsize
    maxProf=0
    for i in range(arrLen):
        if arr[i]<low:
            low=arr[i]
            high=arr[i]
        elif arr[i]>high:
            high=arr[i]
        maxProf=max(maxProf,high-low)
    print(maxProf)


#There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements.
# Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.
#Note: Start the array with positive elements.

#TC:O(N+N), N - for populating arrays , N - for changing the array
#SC:O(N), N - pos + neg storing arrays
def rearrangeArrayEleBySignBF(arr,arrLen):
    pos=[]
    neg=[]
    for i in range(arrLen):
        if arr[i]<0:
            neg.append(arr[i])
        else:
            pos.append(arr[i])
    i=0
    j=0
    for k in range(arrLen):
        if k%2:
            arr[k]=neg[i]
            i+=1
        else:
            arr[k]=pos[j]
            j+=1
    print(arr)

#TC:O(N), N - traversing the array once and substituting positives and negatives simultaneously using pointers
#SC:O(N), N - storing the rearranged array
def rearrangeArrayEleBySignOptimal(arr,arrLen):
    ans=[0]*arrLen
    j=0
    k=1
    for i in range(arrLen):
        if arr[i]<0:
            ans[k]=arr[i]
            k+=2
        else:
            ans[j]=arr[i]
            j+=2
    print(ans)


# Type2
# Same as above ,The leftover elements should be placed at the very end in the same order as in array A.

#TC:O(N+N), N - for populating arrays , N - for changing the array
#SC:O(N), N - pos + neg storing arrays
def rearrangeArrayEleBySignType2BF(arr,arrLen):
    pos=[]
    neg=[]
    for i in range(arrLen):
        if arr[i]<0:
            neg.append(arr[i])
        else:
            pos.append(arr[i])
    i=0
    j=0
    k=0
    while i<len(neg) and j<len(pos):
        if k%2:
            arr[k]=neg[i]
            i+=1
        else:
            arr[k]=pos[j]
            j+=1
        k+=1
    for p in range(i,len(neg)):
        arr[k]=neg[p]
        k+=1
    for p in range(j,len(pos)):
        arr[k]=pos[p]
        k+=1
    print(arr)


def nextPermutation(arr,arrLen):
    pass

# TC: O(N*N) - 2 for loops
# SC : O(N) - for storing ans
def leadersInArrayBF(arr,arrLen):
    ans=[]
    for i in range(arrLen):
        f=0
        for j in range(i+1,arrLen):
            if arr[i]<arr[j]:
                f=1
                break
        if f==0:
            ans.append(arr[i])
    print(ans)

# TC: O(N) - for loop
# SC : O(N) - for storing ans
def leadersInArrayOptimal(arr,arrLen):
    ans=[arr[arrLen-1]]
    for i in range(arrLen-1,-1,-1):
        if (arr[i]>ans[-1]):
            ans.append(arr[i])
    print(ans)


# You are given an array of ‘N’ integers.
# You need to find the length of the longest sequence which contains the consecutive elements.

#TC : O(N*N*N) N - for loop , N - checking for i+1 of each element , N - for linear search
# SC : O(1)
def longConsSeqinArrBF(arr,arrLen):
    ans=1
    def linearsearch(r):
        for i in arr:
            if r==i:
                return r
        return None

    for i in arr:
        c=1
        k=i
        while(linearsearch(k+1)!=None):
            c+=1
            k+=1
        ans=max(c,ans)
    print(ans)
    return ans

# TC : O(NlogN + N)  - NlogN - sorting , N - for loop
# SC : O(1)
def longConsSeqinArrBetter(arr,arrLen):
    arr.sort()
    if arrLen==0:
        return 0
    c=1
    ans=1
    for i in range(1,arrLen):
        if arr[i]-arr[i-1]==1:
            c+=1
        elif arr[i]==arr[i-1]:
            pass
        else:
            ans=max(c,ans)
            c=1
    ans = max(c, ans)
    print(ans)
    return ans

# TC: O(N+N+N) N - for populating set , N - for loop , N - for while (for overall ele in array while sums up to N)
#SC : O(N)
def longConsSeqinArrOptimal(arr,arrLen):
    s=set(arr)
    ans=1
    for i in arr:
        if i-1 not in s:
            c=1
            k=i+1
            while k in s:
                c+=1
                k+=1
            ans=max(ans,c)
    print(ans)
    return ans

#Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.

#TC : O((N*M)+(N*M))  - (N*M) - 2 for loops , (N*M) - worst case if all zeros all will be added to l
#SC : O(N*M) - (N*M) - worst case if all zeros l will be (N*M)
def setMarixZeroBF(arr,n,m):
    l=[]
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                l.append([i,j])
    # print(l)
    for i in l:
        for _ in range(n):
            arr[_][i[1]]=0
        for _ in range(m):
            arr[i[0]][_]=0
    print(arr)

#TC : O((N*M)+(N*M))  - (N*M) - 2 for loops , (N*M) - 2 for loops
#SC : O(N+M) - N for rows and M for col
def setMarixZeroBetter(arr,n,m):
    row = [0] * n
    col = [0] * m
    # print(arr)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                row[i] = 1
                col[j] = 1
    # print(row,col)
    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                arr[i][j] = 0
    print(arr)

#TC : O((N*M)+(N*M))  - (N*M) - 2 for loops , (N*M) - 2 for loops
#SC : O(1) - constant or no space used

#Using 1st row of array as col arr and 1st col of array as row arr as we used in better approach
#And at (0,0) row and col array clash , lets use col0 var to store col0 state
def setMarixZeroOptimal(arr,n,m):
    col0=1
    #stores the row,col array as we did in better approch
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][0]=0
                if j==0:
                    col0=0
                else:
                    arr[0][j]=0

    # print(arr)
    #now iterates over matrix from 1st row and 1st col (1,1) as before index are used for storing values
    for i in range(1,n):
        for j in range(1,m):
            if arr[i][0]==0 or arr[0][j]==0:
                arr[i][j]=0

    #to fix the missed 0th row and 0th col of matrix
    if arr[0][0]==0:
        for j in range(m):
            arr[0][j]=0
    if col0==0:
        for i in range(n):
            arr[i][0]=0
    print(arr)


